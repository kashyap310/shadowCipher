from bs4 import BeautifulSoup
import re

from database.database import execute_query


def analyze(url, html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    emails = re.findall(email_pattern, html_content)
    emailstr = ",".join(emails)

    usernames = soup.find_all('span',class_='username')
    usernamestr=",".join(usernames)
    links = [a['href'] for a in soup.find_all('a', href=True)]
    linkstr = ",".join(links)
    
    data_content =(url,emailstr,usernamestr,linkstr)
    #print("Data content",data_content)
    insert_query = "INSERT INTO analytic_table (url, email, username, links) VALUES (%s, %s, %s, %s)"
    #execute_query(insert_query, (data['url'], data['emails'], data['usernames'], data['links']))
    execute_query(insert_query,data_content)
    print("Data Updated")
