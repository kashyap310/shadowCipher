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

### Upcoming features
1. Real time alerting
2. Wide range of Qurey types and customizable database
3. Web archive (Time based) with HTML and snapshot  (on going...)
4. Pawn tool : protect privacy and find data breaches (improving..)
