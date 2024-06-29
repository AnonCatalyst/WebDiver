import asyncio
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
from tqdm.asyncio import tqdm_asyncio
from aiohttp import ClientSession
from colorama import init, Fore, Style
import src.core  # Assuming src.core is your module

# Initialize colorama for colored terminal output
init(autoreset=True)

async def fetch_html(url, session, retries=3):
    """Fetch HTML content from a URL asynchronously."""
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.text()
    except Exception as e:
        if retries > 0:
            await asyncio.sleep(2)
            return await fetch_html(url, session, retries - 1)
        else:
            return None

def get_links(html, base_url):
    """Extract internal and external links from HTML."""
    try:
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
                    external_links.add(absolute_url)

        return internal_links, external_links
    except Exception as e:
        return set(), set()

async def crawl_website(url, session, visited_urls, all_external_links):
    """Crawl a website and gather information asynchronously."""
    try:
        if url in visited_urls:
            return None
        
        visited_urls.add(url)
        
        async with session.get(url) as response:
            response.raise_for_status()
            html = await response.text()
            
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.title.string.strip() if soup.title else "No title"
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        description = meta_desc.get('content').strip() if meta_desc else "No description"
        
        internal_links, external_links = get_links(html, url)
        all_external_links.update(external_links)
        
        return {
            'url': url,
            'title': title,
            'description': description,
            'internal_links': internal_links
        }
    
    except Exception as e:
        print(Fore.RED + f"An error occurred while crawling {url}: {e}")
        return None

async def extract_external_links(urls):
    """Extract external links from a list of URLs."""
    all_external_links = set()
    try:
        async with ClientSession() as session:
            for url in tqdm_asyncio(urls, desc=Fore.CYAN + "Extracting External Links", unit=Fore.CYAN + " page"):
                html = await fetch_html(url, session)
                if html:
                    soup = BeautifulSoup(html, 'html.parser')
                    base_url = urlparse(url)
                    for link in soup.find_all('a', href=True):
                        absolute_url = urljoin(url, link['href'])
                        parsed_url = urlparse(absolute_url)
                        if parsed_url.scheme in ('http', 'https') and parsed_url.netloc != base_url.netloc:
                            all_external_links.add(absolute_url)
    except Exception as e:
        print(Fore.RED + f"An error occurred while extracting external links: {e}")
    
    return all_external_links

async def main():
    """Main entry point of the crawler."""
    try:
        visited_urls = set()
        all_external_links = set()
        
        print(Style.BRIGHT + Fore.YELLOW + "♤ Welcome to WebDiver - Website Crawler")
        target_url = input(Fore.GREEN + "》Enter target URL: ").strip()
        target_url = 'http://' + target_url if not target_url.startswith(('http://', 'https://')) else target_url
        
        print(Style.BRIGHT + Fore.CYAN + "~~~ Initiating Crawling Process ~~~\n")
        
        async with ClientSession() as session:
            crawl_results = await crawl_website(target_url, session, visited_urls, all_external_links)
            if crawl_results:
                print(Fore.YELLOW + f"~~~ Crawling Result for {target_url} ~~~")
                print(Fore.YELLOW + f"♦ URL: {crawl_results['url']}")
                print(Fore.YELLOW + f"♦ Title: {crawl_results['title']}")
                print(Fore.YELLOW + f"♦ Description: {crawl_results['description']}")
                
                print(Style.BRIGHT + Fore.GREEN + "\n☆ Internal links:")
                for link in crawl_results['internal_links']:
                    print(Fore.GREEN + f"  • {link}")
                
                external_links = await extract_external_links(crawl_results['internal_links'])
                print(Style.BRIGHT + Fore.RED + "\n☆ External Links Found:")
                for ext_link in external_links:
                    print(Fore.RED + f"  • {ext_link}")
    
        print(Style.BRIGHT + Fore.YELLOW + "\n~~~ Crawling Process Complete ~~~\n")
        
        print(Style.BRIGHT + Fore.CYAN + "~~~ Executing src.core ~~~")
        src.core.main()
        print(Style.BRIGHT + Fore.CYAN + "~~~ src.core Execution Complete ~~~")

    except Exception as e:
        print(Style.BRIGHT + Fore.RED + f"An error occurred during crawling: {e}")

if __name__ == "__main__":
    asyncio.run(main())
