import asyncio
import aiohttp
from fake_useragent import UserAgent
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
from tqdm.asyncio import tqdm
import os
import sys

# Import core.py from src directory
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
import core

# Global variables to track visited URLs and external links
visited_urls = set()
all_external_links = {}
visited_external_links = set()

async def fetch_html(url, session, retries=3):
    """Fetch HTML content from a URL with retries in case of failure."""
    try:
        ua = UserAgent()
        headers = {'User-Agent': ua.random}
        
        async with session.get(url, headers=headers) as response:
            response.raise_for_status()  # Raise HTTPError for bad responses
            return await response.text()
    except aiohttp.ClientError as e:
        print(f"Error fetching {url}: {e}")
        if retries > 0:
            print(f"Retrying {retries} more times...")
            await asyncio.sleep(2)  # Adjust the sleep time as per your needs
            return await fetch_html(url, session, retries - 1)
        else:
            print("Max retries exceeded. Skipping.")
            return None

def get_title_and_description(html):
    """Extract title and description meta tag from HTML."""
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.title.string.strip() if soup.title else "No title"
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    description = meta_desc.get('content').strip() if meta_desc else "No description"
    return title, description

def get_links(html, base_url):
    """Extract internal and external links from HTML."""
    soup = BeautifulSoup(html, 'html.parser')
    internal_links = set()
    external_links = set()
    parsed_base_url = urlparse(base_url)
    base_domain = parsed_base_url.netloc

    for link in soup.find_all('a', href=True):
        href = link['href']
        absolute_url = urljoin(base_url, href)
        parsed_url = urlparse(absolute_url)
        
        if parsed_url.scheme in ('http', 'https'):
            if parsed_url.netloc == base_domain:
                internal_links.add(absolute_url)
            else:
                if absolute_url not in visited_external_links:
                    visited_external_links.add(absolute_url)
                    external_links.add(absolute_url)

    return internal_links, external_links

async def crawl_website(url, session):
    """Crawl a website starting from the given URL."""
    global visited_urls, all_external_links
    
    # Check if URL has been visited already
    if url in visited_urls:
        return None
    
    # Fetch HTML content of the URL
    html = await fetch_html(url, session)
    if html:
        visited_urls.add(url)
        title, description = get_title_and_description(html)
        internal_links, external_links = get_links(html, url)
        
        # Update global external links set with source URL
        for ext_link in external_links:
            if ext_link not in all_external_links:
                all_external_links[ext_link] = []
            all_external_links[ext_link].append(url)
        
        return {
            'url': url,
            'title': title,
            'description': description,
            'internal_links': internal_links
        }
    return None

async def extract_external_links(urls):
    """Extract external links from a list of URLs using threading and tqdm for progress."""
    global all_external_links
    
    async with aiohttp.ClientSession() as session:
        # Initialize tqdm progress bar
        async for url in tqdm(urls, desc="Extracting External Links", unit=" page"):
            try:
                html = await fetch_html(url, session)
                if html:
                    _, ext_links = get_links(html, url)
                    # Update external links globally with source URL
                    for ext_link in ext_links:
                        if ext_link not in all_external_links:
                            all_external_links[ext_link] = []
                        all_external_links[ext_link].append(url)
            except Exception as e:
                print(f"Exception occurred for {url}: {e}")

    return all_external_links

def print_divider():
    """Print a divider line."""
    print("~" * 80)

def print_header(text):
    """Print a header with a title."""
    print_divider()
    print(text)
    print_divider()

async def main():
    # Welcome message and input for target URL
    print_header("♤ Welcome to WebDiver - Website Crawler")
    target_url = input("》Enter target URL: ").strip()
    print_divider()

    # Execute core.py with the target URL
    core.main(target_url)

    crawl_results = []

    async with aiohttp.ClientSession() as session:
        # Crawl the initial target URL
        print(f"■ Crawling {target_url}...")
        result = await crawl_website(target_url, session)
        if result:
            crawl_results.append(result)

        # Recursively crawl internal links
        while crawl_results:
            current_page = crawl_results.pop(0)
            print(f"- URL: {current_page['url']}")
            print(f"- Title: {current_page['title']}")
            print(f"- Description: {current_page['description']}")
            print_divider()
            
            print("☆ Internal links:")
            print_divider()
            for link in current_page['internal_links']:
                print(link)

            # Add internal links to crawl_results if not visited
            for link in current_page['internal_links']:
                if link not in visited_urls:
                    visited_urls.add(link)
                    result = await crawl_website(link, session)
                    if result:
                        crawl_results.append(result)

    # Extract external links from all visited pages using threading and tqdm
    all_external_links = await extract_external_links(visited_urls)

    # Print all accumulated external links after crawling all pages
    print_header("☆ External Links Found:")
    if all_external_links:
        for link, sources in all_external_links.items():
            print(f"• {link} (Found in: {', '.join(sources)})")
    else:
        print("No external links found.")

if __name__ == "__main__":
    asyncio.run(main())
