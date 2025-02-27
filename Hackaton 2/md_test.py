from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import markdownify
import requests
import time
from urllib.parse import urljoin, urlparse
from requests.exceptions import RequestException

# Set up Chrome WebDriver
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Uncomment to run in headless mode
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the main website
url = "https://www.fib.upc.edu/"
driver.get(url)
driver.set_page_load_timeout(30)  # Timeout for loading pages

# Get rendered HTML
soup = BeautifulSoup(driver.page_source, "html.parser")

# Extract all links from the page
links = set()
for link in soup.find_all("a", href=True):
    print("Found link...")
    href = link.get("href")
    full_url = urljoin(url, href)  # Get full URL
    links.add(full_url)

# Function to scrape content from a URL and convert to markdown with retries
def scrape_to_markdown(url, retries=3, delay=5):
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url, timeout=10)  # Add a timeout to avoid long waits
            response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
            page_soup = BeautifulSoup(response.text, "html.parser")
            md_content = markdownify.markdownify(page_soup.prettify(), heading_style="ATX")
            return md_content
        except RequestException as e:
            attempt += 1
            print(f"Error fetching {url}: {e}. Retrying {attempt}/{retries}...")
            time.sleep(delay)
    return f"# Error: Could not fetch {url}\n"

# Initialize a string to hold all Markdown content
all_md_content = f"# Scraped Content from {url}\n\n"

# Add the content of the main page
all_md_content += scrape_to_markdown(url)

# Iterate through all links and scrape them as well
for link in links:
    # Avoid re-scraping the same domain
    if urlparse(link).netloc == urlparse(url).netloc:
        all_md_content += f"\n\n# Content from {link}\n\n"
        all_md_content += scrape_to_markdown(link)

# Save the content to a .md file
with open("website_content.md", "w", encoding="utf-8") as f:
    f.write(all_md_content)

driver.quit()

print("Markdown file created: website_content.md")
