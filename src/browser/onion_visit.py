import requests
#from database.database import *
from rich.console import Console

def web_visitor(site_url,id):
    console = Console()
    site = site_url  # Rename site_url to site for clarity

    if not site.startswith(('http://', 'https://')):
        site = 'http://' + site

    session = requests.session()
    
    # Tor uses the 9050 port as the default socks port
    session.proxies = {'http': 'socks5h://127.0.0.1:9050',
                       'https': 'socks5h://127.0.0.1:9050'}

    try:
        result = session.get(site,timeout=25).text
        
    except requests.RequestException as e:
        console.print(f"[red] Error during request")
        #delete_query = "DELETE FROM master_table WHERE id = %s"
        #para =(id,)
        #execute_query(delete_query, para)
        return  # Exit the function if there's an error

    #update_query = "UPDATE master_table SET result = %s WHERE id = %s"
    #para =(result,id)
    console.print(f"[green] Adding to DB")
    #execute_query(update_query, para)

# Example usage
