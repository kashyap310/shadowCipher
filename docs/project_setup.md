## Project setup

1. Clone the repository
```
git clone https://github.com/kashyap310/RJPOLICE_HACK_473_Imperial_11.git
```
2. Activate Venv
``` 
source Venv/bin/activate #for linux
```
3. install requirement
``` 
pip install -r requirements.txt
pip install requests[socks]
```
4. Run tor proxy tool
```
 python3 src/tor_proxy_tool/tor_proxy.py
```
5. Extract Onion site from Ahima search engine
```
python3 src/query_site_extractor/Ahima_site_fetcher.py
```
6. Crawl data from this scraped site
``` 
python3 src/tor_searcher/torSearcher.py
```
7. Deactivate virtual environment
```
deactivate
```
