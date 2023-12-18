import subprocess
import time
from stem import Signal
from stem.control import Controller

TOR_PROXY_PORT = 9050  # Tor SOCKS proxy port

class TorProxyTool:
    @staticmethod
    def restart_tor():
        try:
            subprocess.call(['sudo', 'service', 'tor', 'restart'])
            print("Tor restarted.")
        except Exception as e:
            print(f"Error restarting Tor: {e}")

    @staticmethod
    def set_proxy(enable=True):
        proxy_setting = f"socks5://127.0.0.1:{TOR_PROXY_PORT}"
        if enable:
            subprocess.run(["gsettings", "set", "org.gnome.system.proxy", "mode", "'manual'"])
            subprocess.run(["gsettings", "set", "org.gnome.system.proxy", "socks", proxy_setting])
            subprocess.run(['sudo', 'tee', '/etc/apt/apt.conf.d/80proxy'], input=f"Acquire::socks::proxy \"{proxy_setting}\";", text=True)
            print("Proxy enabled.")
        else:
            try:
                subprocess.run(['sudo', 'service', 'tor', 'stop'])
                subprocess.run(['gsettings', 'set', 'org.gnome.system.proxy', 'mode', 'none'])
                subprocess.run(['sudo', 'rm', '/etc/apt/apt.conf.d/80proxy'])
                subprocess.run(['sudo', 'service', 'tor', 'stop'])
                print("Proxy disabled.")
            except Exception as e:
                print(f"Error disabling proxy: {e}")

    @staticmethod
    def setup_tor_http_proxy():
        try:
            subprocess.run(["sudo", "apt-get", "install", "socat"])
            subprocess.Popen(["socat", "TCP-LISTEN:8118,fork", "SOCKS4A:127.0.0.1:localhost:9050,socksport=9050"])
            print("Tor HTTP Proxy set up with socat.")
        except Exception as e:
            print(f"Error setting up Tor HTTP Proxy: {e}")

    @staticmethod
    def renew_identity():
        try:
            subprocess.run(['sudo', 'chmod', 'o+rx', '/run/tor/control.authcookie'])
            with Controller.from_port(port=9051) as controller:
                controller.authenticate()
                controller.signal(Signal.NEWNYM)
                time.sleep(2)  # Introduce a short delay
                print("Identity renewed.")
        except Exception as e:
            print(f"Error renewing identity: {e}")

if __name__ == "__main__":
    tor_proxy_tool = TorProxyTool()

    while True:
        print("1. Enable Tor Proxy")
        print("2. Disable Tor Proxy")
        print("3. Set up Tor HTTP Proxy")
        print("4. Renew Tor Identity")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            tor_proxy_tool.set_proxy(enable=True)
            tor_proxy_tool.restart_tor()
        elif choice == "2":
            tor_proxy_tool.set_proxy(enable=False)
        elif choice == "3":
            tor_proxy_tool.setup_tor_http_proxy()
        elif choice == "4":
            tor_proxy_tool.renew_identity()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

        time.sleep(1)
