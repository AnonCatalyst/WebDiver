import os
import sys
import platform

def install_package(package_name):
    try:
        os.system(f"pip install --upgrade --break-system-packages {package_name}")
        print(f"Successfully installed {package_name}")
    except Exception as e:
        print(f"Error installing {package_name}: {e}")
        return False
    return True

# Try installing fake-useragent first
if not install_package("fake-useragent"):
    # If that fails, try installing fake_useragent
    install_package("fake_useragent")

# Install the rest of the requirements
requirements = [
    "aiohttp==3.9.4",
    "async-timeout==4.0.3",
    "beautifulsoup4==4.10.0",
    "colorama==0.4.4",
    "ipwhois==1.2.0",
    "jsonschema==4.5.0",
    "tqdm==4.66.3"
]

for requirement in requirements:
    install_package(requirement)

print("All requirements installed successfully!")