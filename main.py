### Importing Streamlit for the frontend interface
import streamlit as st

### Importing functions from the scrape.py module
from scrape import (scrape_website, 
                    split_dom_content, 
                    clean_body_content, 
                    extract_body_content)

# Setting the title of the Streamlit app
st.title("AI Web Scraper")

# Creating an input field for the user to enter a website URL
url = st.text_input("Enter a Website URL: ")

# If the 'Scrape site' button is clicked
if st.button("Scrape site"):
    st.write("Scraping the website")  # Inform the user that scraping is in progress
    
    # Call the scrape_website function with the entered URL
    result = scrape_website(url)
    
    # Extract the body content from the HTML
    body_content = extract_body_content(result)
    
    # Clean the extracted body content (e.g., removing scripts, styles, etc.)
    cleaned_content = clean_body_content(body_content)
    
    # Store the cleaned content in the Streamlit session state for persistent storage
    st.session_state.dom_content = cleaned_content
    
    # Display the cleaned DOM content in an expandable text area
    with st.expander("View DOM Content"):
        st.text_area("Content", cleaned_content, height=300)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you need ??")
    
    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content")
            
            dom_chunks = split_dom_content(st.session_state.dom_content)