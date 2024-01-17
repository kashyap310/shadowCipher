import requests

# Set the I2P proxy configuration
proxy_address = "http://127.0.0.1:4444"  # Default I2P proxy address
proxies = {"http": proxy_address, "https": proxy_address}

# Replace the following URL with the .i2p address of the site you want to connect to
i2p_site_url = "http://stats.i2p/cgi-bin/partvtunnels-day.cgi"

try:
    # Make a request through the I2P proxy
    response = requests.get(i2p_site_url, proxies=proxies)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print(f"Successfully connected to {i2p_site_url}")
        print(response.text)
    else:
        print(f"Failed to connect to {i2p_site_url}. Status code: {response.status_code}")

except requests.RequestException as e:
    print(f"Error connecting to {i2p_site_url}: {e}")
