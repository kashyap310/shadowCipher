import subprocess
import time
import requests

I2P_PROXY_URL = "http://127.0.0.1:4444"

def start_i2p_proxy():
    try:
        # Start I2P router
        subprocess.run(["i2prouter", "start"])
        
        # Wait for the router to start (adjust the sleep duration as needed)
        time.sleep(10)

        print("I2P proxy started.")
    except Exception as e:
        print(f"Error starting I2P proxy: {e}")

def get_i2p_proxy_url():
    return I2P_PROXY_URL

def close_i2p_proxy():
    try:
        # Stop I2P router
        subprocess.run(["i2prouter", "stop"])

        print("I2P proxy stopped.")
    except Exception as e:
        print(f"Error stopping I2P proxy: {e}")
    
if __name__ == "__main__":
    # Start I2P proxy
    start_i2p_proxy()

    # Get I2P proxy URL
    proxy_url = get_i2p_proxy_url()
    print(f"I2P Proxy URL: {proxy_url}")

    # Example: Use the proxy URL with another crawler (replace with your own logic)
   # response = requests.get("http://example.onion", proxies={"http": proxy_url, "https": proxy_url})
    #print("Response from I2P:", response.text)

    # Close I2P proxy
    #close_i2p_proxy()
