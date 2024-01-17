import requests
import socket
from rich.console import Console

def trace_route_to_tor_site(site_url):
    console = Console()
    site = site_url  # Rename site_url to site for clarity

    if not site.startswith(('http://', 'https://')):
        site = 'http://' + site

    session = requests.session()

    # Tor uses the 9050 port as the default socks port
    session.proxies = {'http': 'socks5h://127.0.0.1:9050',
                       'https': 'socks5h://127.0.0.1:9050'}

    try:
        # Use the session to make the request
        response = session.get(site, timeout=25)

        # Extract the IP address from the response URL
        parsed_url = response.url.split('/')
        if len(parsed_url) >= 3:
            ip_address = parsed_url[2]
            console.print(f"[green]Tracing route to {site}")
            console.print(f"{ip_address} ({response.url} - {response.elapsed.total_seconds() * 1000:.2f} ms)")

    except requests.RequestException as e:
        console.print(f"[red]Error during request: {e}")

# Example usage
onion_site_url = "http://ze2f2gus5s2hftnyrzanmuybgjw55br7wmdp6mhzl6ntwbcp6jvrceqd.onion"
trace_route_to_tor_site(onion_site_url)
