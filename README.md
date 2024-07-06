# WebDiver - Website Crawler

WebDiver is a Python-based website crawler designed for extracting comprehensive information from web pages. It facilitates tasks such as web analysis, Open Source Intelligence (OSINT) gathering, competitive analysis, and more.

## Features

- **Data Extraction**: WebDiver systematically retrieves data from websites, including titles, descriptions, internal links, and external links. This information is crucial for understanding the structure and content of a website.

- **Link Analysis**: Identifies relationships between different web pages through internal and external links, providing insights into information flow and dependencies within a site.

- **Metadata Retrieval**: Extracts metadata such as titles, descriptions, and other meta tags, which are indicative of a website's focus, content, and possibly its owners or creators.

- **Email Extraction**: Finds and extracts email addresses from web pages, aiding in contact discovery or further analysis.

- **Error Handling and Logging**: Implements robust error handling and logging mechanisms to track and manage encountered issues during crawling.

- **IP Information Retrieval**: Fetches and displays IP geolocation information for websites, enhancing the depth of analysis with network-related details.

- **Asynchronous Processing**: Utilizes asyncio for concurrent HTTP requests and data extraction, optimizing performance and efficiency.

- **Progress Monitoring**: Utilizes the `tqdm` library to display a progress bar during the extraction of external links, offering real-time feedback on task completion.

### Usage Instructions

1. **Prerequisites**:
   - Ensure Python 3 is installed on your system. If not, download it from [python.org](https://www.python.org/downloads/) and follow the installation instructions.

2. **Running the Script**:
   - Navigate to the directory containing `webdiver.py` using a terminal or command prompt.
   - Execute the script by running:
     ```bash
     git clone https://github.com/AnonCatalyst/WebDiver && cd WebDiver
     pip install -r requirements.txt --break-system-packages
     python3 webdiver.py
     ```
     Replace `python3` with `python` if `python3` command is not recognized on your system.

3. **On-screen Instructions**:
   - Enter the target URL (`Enter target URL:`) when prompted. This specifies the starting point for the website crawling process.
   - The script will initiate crawling from the specified URL, extracting information and displaying progress using the progress bar.

### Notes

- Customize the script as per specific requirements or enhancements needed for your web crawling and analysis tasks.
- Ensure internet connectivity during script execution to fetch web pages and extract information effectively.

WebDiver enhances the ability to gather, analyze, and interpret web-based data, making it a valuable tool for researchers, investigators, cybersecurity professionals, and businesses interested in understanding online activities and trends.
