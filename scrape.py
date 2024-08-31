### Selenium specific Packages and Chrome Drivers
from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection

### BeautifulSoup4 : HTML Parser support
from bs4 import BeautifulSoup

### Webdriver API Keys
SBR_WEBDRIVER = 'https://brd-customer-hl_b8b6d8c1-zone-scraping_browser:famlkfsj3d2x@brd.superproxy.io:9515'



### Scraping logic:
def scrape_website(website):
    print("Launching chrome browser...")
    
    ## Remote connection with respect to Brightdata API key
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        driver.get(website)
        
        ## Code for Captcha solver so IPs does not get stripped
        print('Waiting captcha to solve...')
        
        solve_res = driver.execute(
            'executeCdpCommand', 
            {
             'cmd': 'Captcha.waitForSolve',
             'params': {'detectTimeout': 10000},
            },  
        )
        
        print('Captcha solve status:', solve_res['value']['status'])
        print('Navigated! Scraping page content...')
        html = driver.page_source
        
        ## Returning the Contents present in the browser: HTML document
        return html
    
### Extracting body content from HTML
def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser") 
    body_content = soup.body
    
    ## If HTML has contents
    if body_content:
        return str(body_content)
    
    ## Else; Return an empty string
    return ""



def clean_body_content(body_content):
    """
    This function takes a string of HTML content as input, parses it using BeautifulSoup,#+
    and then removes all script and style tags from the HTML. After that, it extracts all#+
    the text from the remaining HTML and returns it as a single string, with each paragraph#+
    separated by a newline character.#+

    Parameters:
    body_content (str): A string containing the HTML content to be cleaned.
    
    Returns:
    str: A string containing the cleaned text from the HTML content.#+
    """
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    # Output -> Get all of the Text and then separate it with a newline    #+
    cleaned_content = soup.get_text(separator="\n")
    
    # any leading or trailing whitespace will be removed
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content

def split_dom_content(dom_content, max_length = 6000):
    
    return [
        dom_content[i : i + max_length]
        for i in range(0, len(dom_content), max_length)
    ]
        
