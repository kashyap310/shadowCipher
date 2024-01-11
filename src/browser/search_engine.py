import random
import re

import requests

def Ahima_scraper(engine_url,query, proxy):
    if " " in query:
        query = query.replace(" ", "+")
    query_url = engine_url.format(query)
    ua_list = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19577",
        "Mozilla/5.0 (X11) AppleWebKit/62.41 (KHTML, like Gecko) Edge/17.10859 Safari/452.6",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2656.18 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36",
        "Mozilla/5.0 (Linux; U; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13",
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; zh-cn) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
    ]
    ua = random.choice(ua_list)
    headers = {"User-Agent": ua}
    request = requests.get(query_url, headers=headers)
    content = request.text
    regexquery = r"\w+\.onion"

    # Regex query for finding onion links
    mineddata = re.findall(regexquery, content)

    # Remove duplicates while maintaining order
    mineddata = list(dict.fromkeys(mineddata))

    return mineddata
    
def Torch_Scraper(engine_url,query):
    proxies = {
    'http': 'socks5h://localhost:9050',
    'https': 'socks5h://localhost:9050'
}
    if " " in query:
        query = query.replace(" ", "+")
    query_url = engine_url.format(query)

    request = requests.get(query_url,proxies=proxies)
    content = request.text
    regexquery = r"\w+\.onion"

    # Regex query for finding onion links
    mineddata = re.findall(regexquery, content)

    # Remove duplicates while maintaining order
    mineddata = list(dict.fromkeys(mineddata))

    return mineddata