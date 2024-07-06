import socket
import ipwhois
import json
import asyncio

async def resolve_ip(target_url):
    try:
        return socket.gethostbyname(target_url)
    except socket.gaierror as e:
        raise Exception(f"DNS resolution error for {target_url}: {str(e)}")

async def fetch_ip_info(target_url):
    try:
        ip_address = await resolve_ip(target_url)
        obj = ipwhois.IPWhois(ip_address)
        results = obj.lookup_rdap()
        
        ip_info = {
            'ip_address': ip_address,
            'asn': results.get('asn', ''),
            'asn_cidr': results.get('asn_cidr', ''),
            'asn_country_code': results.get('asn_country_code', ''),
            'network': results['network']['name'] if 'network' in results else ''
        }
        
        return ip_info
    
    except (ipwhois.IPDefinedError, ipwhois.IPWhoisLookupError, socket.gaierror) as e:
        raise Exception(f"Error retrieving IP information for {target_url}: {str(e)}")
    
    except Exception as e:
        raise Exception(f"Unexpected error retrieving IP information for {target_url}: {str(e)}")

async def get_ip_info(target_url):
    try:
        ip_info = await fetch_ip_info(target_url)
        return json.dumps(ip_info)
    
    except Exception as e:
        return f"Error: {str(e)}"