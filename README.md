# AI Web Scraper

AI Web Scraper is a Python-based tool that combines web scraping capabilities with AI-powered analysis to extract and process information from websites.

## Features

- Web scraping using BeautifulSoup and requests libraries
- AI-powered text analysis and processing
- Customizable scraping parameters
- Data export functionality

## Project Structure

- `main.py`: Main script for running the web scraper
- `requirements.txt`: List of project dependencies
- `scraper/`: Directory containing scraper-related modules
- `ai/`: Directory for AI-related modules
- `utils/`: Utility functions and helper modules

## Technologies Used

- Python 3.12
- BeautifulSoup4
- Requests

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/raghulchandramouli/AI-Web-Scraper.git
   cd AI-Web-Scraper
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the AI Web Scraper:

```
- `-u, --url`: Specify the URL to scrape (required)
- `-d, --depth`: Set the crawling depth (default: 1)
- `-o, --output`: Specify the output file name (default: output.json)
- `-f, --format`: Choose the output format (json, csv, txt) (default: json)
- `-a, --ai`: Enable AI analysis (default: False)
```

### Examples:

1. Basic scraping of a single page:
   ```bash
   python main.py -u https://example.com
   ```

2. Scrape with depth 2 and save as CSV:
   ```bash
   python main.py -u https://example.com -d 2 -o results.csv -f csv
   ```

3. Scrape with AI analysis enabled:
   ```bash
   python main.py -u https://example.com -a
   ```


## Configuration


The AI Web Scraper can be configured using a `config.yaml` file in the project root directory. Here's an example configuration:

## AI Capabilities

The AI Web Scraper incorporates advanced artificial intelligence features to enhance the scraping process and provide valuable insights from the collected data. Here are the key AI capabilities:

1. Text Classification
   - Automatically categorizes scraped content into predefined categories
   - Uses a fine-tuned BERT model for accurate classification
   - Supports multi-label classification for content that fits multiple categories

2. Named Entity Recognition (NER)
   - Identifies and extracts named entities such as persons, organizations, locations, etc.
   - Utilizes a custom-trained spaCy model for domain-specific entity recognition
   - Provides confidence scores for each identified entity

## Data Export

The AI Web Scraper provides flexible options for exporting the scraped and analyzed data. This allows you to easily integrate the results into your workflow or other tools for further processing.

### Export Formats

1. JSON (JavaScript Object Notation)
   - Default export format
   - Preserves nested data structures
   - Ideal for web applications and data interchange
  
2. CSV (Comma-Separated Values)
   - Tabular format, easily importable into spreadsheet software
   - Flattens nested structures
   - Suitable for data analysis in tools like Excel or pandas



## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- BeautifulSoup4: https://www.crummy.com/software/BeautifulSoup/
- Requests: https://docs.python-requests.org/
