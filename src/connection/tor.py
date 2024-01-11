import subprocess
import time
from stem import Signal
from stem.control import Controller

TOR_PROXY_PORT = 9050  # Tor SOCKS proxy port

def restart_tor():
    try:
        subprocess.call(["sudo", "service", "tor", "restart"])
        print("Tor restarted.")
    except Exception as e:
        print(f"Error restarting Tor: {e}")

def set_tor_proxy(enable=True):
        settings =[]
        proxy_setting = f"socks5://127.0.0.1:{TOR_PROXY_PORT}"
        if enable:
            subprocess.run(["gsettings", "set", "org.gnome.system.proxy", "mode", "'manual'"])
            #subprocess.run(["gsettings", "set", "org.gnome.system.proxy", "socks", proxy_setting])
            #subprocess.run(['sudo', 'tee', '/etc/apt/apt.conf.d/80proxy'], input=f"Acquire::socks::proxy \"{proxy_setting}\";", text=True)
            print('\n')
            #print("Proxy enabled.")
            settings.insert(0,proxy_setting)
            settings.insert(1,True)
            return settings
        else:
            try:
                subprocess.run(['sudo', 'service', 'tor', 'stop'])
                subprocess.run(['gsettings', 'set', 'org.gnome.system.proxy', 'mode', 'none'])
                subprocess.run(['sudo', 'rm', '/etc/apt/apt.conf.d/80proxy'])
                subprocess.run(['sudo', 'service', 'tor', 'stop'])
               # print("Proxy disabled.")
                settings.insert(1,False)
                return settings
            except Exception as e:
                error ="Error disabling proxy :" + e
                settings.insert(2,error)
                return settings
                

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