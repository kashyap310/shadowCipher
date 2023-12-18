import requests
from ..tor_proxy_tool.tor_proxy import TorProxyTool

# Replace 'http://example.onion' with the actual .onion site you want to scrape
url = 'http://of3fshsmkrtrapgbsd5pueyqrydwir2yc7om44s2zjs3bjfomd232uqd.onion'

# Configure requests to use the Tor SOCKS proxy
if __name__ == "__main__":
    tormanager = TorProxyTool()
    tormanager.restart_tor
    proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050',
    }

    response = requests.get(url, proxies=proxies)

    # Print the HTML content
    print(response.text)
