## DWeb-Monitoring-Tool

#### Problem Statment
 The problem at hand is to design and implement an effective Dark Web Monitoring System that can identify and track illegal activities, sensitive information leaks, and potential security threats on hidden online platforms. The Dark Web Monitoring System aims to:

* [Web Crawler and Data Collection](/docs/web-crawling.md): Develop an intelligent web crawler capable of navigating the Dark Web and collecting relevant data from hidden sources.
* Anomaly Detection: Implement machine learning algorithms to identify anomalies and patterns associated with illicit activities, such as the sale of illegal goods or services.
* Real-time Alerting: Establish real-time alerting mechanisms to promptly notify relevant authorities or organizations about potential security breaches or emerging threats.
* Data Analysis and Visualization: Create tools for analyzing and visualizing data collected from the Dark Web to gain actionable insights and identify trends.
* Collaboration with Law Enforcement: Facilitate data sharing and collaboration with law enforcement agencies to aid in investigations and crackdowns on criminal activities.

### Background of problem statement
The Dark Web, an anonymous and hidden part of the internet, has become a hub for illegal activities, including the sale of stolen data, drugs, weapons, and other illicit services. These activities pose significant risks to individuals, businesses, and governments. To mitigate these risks and ensure online security, there is a need to develop a robust Dark Web Monitoring System that can proactively detect, monitor, and respond to illicit activities on the Dark Web.

### Challenge involved in solving the problem

  1. Accessing the darknet through TOR/I2P/ZeroNet.onion domains/.i2P domains.
  2. [Traffic through relays](/docs/Tor-relay.md)
  3.  Less understanding of search engine tools for the dark web (e.g., Katana, Onion search, Ahmia search engine, Darksearch).
  4.  Regularly evolving features and tools to get onion links from the darkweb (OnionScan, Onioff, Onion-nmap) and scrap Darkweb (TorBot, TorCrawl, OnionIngestor).

### Solution required
The task is to develop a tool that could search for keywords across dark net search engines, along with an alerting mechanism.

### Expectation from the solution/tool
1. Must be a simple interface/Console which must connect to VPN and then help to find the details rather than police searching for websites, links, platforms on dark web.
2. Must also be able to fetch data from different browsers like TOR, TAILS, I2P, Freenet etc. Participants must develop a simple interface/console that automatically latched to a VPN and then connect through Dark Net Browser/Deep Net browser.
3. And then it should be able to filter data based upon Keyword (like Murder, Arms, Drugs, etc.), Geo-location, state, district, date, etc.
4. Extension: Expose IP details of dark net sites & users.
5. Tool which could identify a seller of any product and provide ways to track down the person. It should be able to gather/crawl details about all websites, chat rooms, shopping sites & other information related to dark web. It should be a handy intelligence and data collection tool on the dark web.
6. Web archive time-based proxy with easy User interface for access, Geolocation identification, TOR Keyword Search, Dark Web Crawlers. 

### Setting up project
1. environment setup
```
python -m venv venv 
```
2. Activate environment
```
source venv/bin/activate   # On Linux/macOS 
venv\Scripts\activate      # On Windows
```
3. install dependency
```
pip install -r requirements.txt
```

4. Add modules to the requirements
'''
pip freeze > requirements.txt
'''
5. deactivate after done
'''
deactivate

'''

6. request for socks
'''
pip install requests[socks]
'''
