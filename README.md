# WebDiver - Website Crawler

WebDiver is a Python-based tool designed for extracting and analyzing comprehensive information from websites. It caters specifically to the needs of the Open Source Intelligence (OSINT) community, providing robust capabilities for web data extraction, link analysis, metadata retrieval, and more.

## Features

### Data Extraction
WebDiver systematically retrieves and analyzes data from web pages, including titles, descriptions, internal links, and external links. This capability is crucial for understanding the structure and content of target websites.

### Link Analysis
The tool identifies relationships between different web pages through internal and external links. This analysis provides insights into information flow, dependencies within a site, and potential connections to other web entities.

### Metadata Retrieval
WebDiver extracts metadata such as titles, descriptions, and other meta tags from web pages. This information helps in understanding a website's focus, content, and possibly its ownership or creator details.

### Email Extraction
It automatically finds and extracts email addresses embedded within web pages. This feature aids in discovering contact information or conducting further investigations related to email communications.

### Error Handling and Logging
WebDiver implements robust error handling mechanisms to manage encountered issues during the crawling process. Errors are logged comprehensively, providing transparency and facilitating troubleshooting.

### IP Information Retrieval
The tool fetches detailed IP information for target URLs, including ASN (Autonomous System Number), ASN CIDR (Classless Inter-Domain Routing), country, city, latitude, and longitude. This feature enhances the understanding of server locations and network infrastructure associated with a website.

### Asynchronous Processing
Utilizing asyncio, WebDiver performs asynchronous web crawling and data extraction. This approach optimizes performance by allowing concurrent operations, improving speed and efficiency in data retrieval tasks.

### Progress Monitoring
The integration of `tqdm` provides a visual progress bar during the extraction of external links. This feature offers real-time feedback on task completion, enhancing user experience and task management.

## Usage Instructions

1. **Prerequisites**:
   - Ensure Python 3 is installed on your system. If not, download it from [python.org](https://www.python.org/downloads/) and follow the installation instructions.

2. **Running the Script**:
   - Navigate to the directory containing `webdiver.py` using a terminal or command prompt.
   - Execute the script by running:
     ```bash
     git clone https://github.com/AnonCatalyst/WebDiver && cd WebDiver
     python3 install.py
     python3 webdiver.py
     ```
     Replace `python3` with `python` if `python3` command is not recognized on your system.

3. **On-screen Instructions**:
   - Enter the target URL (`Enter target URL:`) when prompted. This specifies the starting point for the website crawling process.
   - WebDiver initiates crawling from the specified URL, extracting comprehensive information and displaying progress using the progress bar.

## Notes

- Customize the script to meet specific requirements or enhancements needed for your OSINT investigations or web analysis tasks.
- Ensure internet connectivity during script execution to fetch web pages and extract information effectively.

WebDiver enhances the ability to gather, analyze, and interpret web-based data, making it an invaluable tool for researchers, investigators, cybersecurity professionals, and businesses interested in understanding online activities and trends.
