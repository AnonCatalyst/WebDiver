# WebDiver - Website Crawler

WebDiver is a Python-based website crawler designed for extracting comprehensive information from web pages. It facilitates tasks such as web analysis, Open Source Intelligence (OSINT) gathering, competitive analysis, and more.


## TO-DO
- Extraction of Emails during traversal
- IP and Website detailed information
- META extractions for more detailed output about the website
- Extracting usernames from external links

### Features

- **Data Extraction**: WebDiver systematically retrieves data from websites, including titles, descriptions, internal links, and external links. This information is crucial for understanding the structure and content of a website.

- **Link Analysis**: It identifies relationships between different web pages through internal and external links, providing insights into information flow and dependencies within a site.

- **Metadata Retrieval**: Extracts metadata such as titles and descriptions, which are indicative of a website's focus, content, and possibly its owners or creators.

- **Progress Monitoring**: Utilizes the `tqdm` library to display a progress bar during the extraction of external links, offering real-time feedback on task completion.

- **OSINT Capabilities**: Supports OSINT activities by gathering and analyzing publicly available data from websites, aiding in research, investigation, and intelligence gathering.

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
