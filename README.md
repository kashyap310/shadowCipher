### Dark web monitoring

* Simple tool for finding the darkweb sites from different types of browsers 
* Crawling through different sites and collect response to the Postgresql database
* Processing HTML content and finding useful informations
* Upcoming features are Pawn?? , Web archive etc..

### Project Structure:

```
Dark-web-monitoring tool
├── src/
│   ├── analysis/
│   │   └── analysis.py
│   ├── browser/
│   │   ├── onion_visit.py
│   │   └── search_engine.py
│   ├── connection/
│   │   └── tor.py
│   ├── database/
│   │   ├── config.py
│   │   ├── database.ini
│   │   └── database.py
│   └── main.py
├── venv/
├── web/
│   ├── templates/
│   │   └── home.html
│   └── app.py
├── README.md
├── requirements.txt
└── setup.py
```
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
```
4. Run python program
```
python3 src/main.py --help
```
5. Database

>Find the proper installation process of POSTGRESQL database from offcial documentation and configure parameters into the  database.ini file
