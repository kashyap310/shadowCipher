from browser.search_engine import *
from browser.onion_visit import *
from connection.tor import *
from database.database import *
from analysis.analysis import *
import click
import sys
import os
from rich.console import Console
from rich.table import Table


QUERY = ["Arms","Carding","Drugs","Hacker","Murder"]
BROWSER = ["Ahima","Torch"]
MONTH = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

'''
    function return type:
    List= [important , logging message , error message]
'''
'''
#############
                Layout
############

'''
def clear_console():
    # Check if the operating system is Windows
    if sys.platform.startswith('win'):
        os.system('cls')  # Clear console for Windows
    else:
        os.system('clear') 
    print_logo(logo) #print logo after console clear
    
def print_logo(text):
    hacker_color_code = '\033[92m'  # ANSI escape code for light green color
    reset_code = '\033[0m'  # ANSI escape code to reset color

    print(f"{hacker_color_code}{text}{reset_code}")

logo = r'''
  ▓█████▄  ▄▄▄       ██▀███   ██ ▄█▀    █     █░▓█████  ▄▄▄▄       ███▄ ▄███▓ ▒█████   ███▄    █  ██▓▄▄▄█████▓ ▒█████   ██▀███  
  ▒██▀ ██▌▒████▄    ▓██ ▒ ██▒ ██▄█▒    ▓█░ █ ░█░▓█   ▀ ▓█████▄    ▓██▒▀█▀ ██▒▒██▒  ██▒ ██ ▀█   █ ▓██▒▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
  ░██   █▌▒██  ▀█▄  ▓██ ░▄█ ▒▓███▄░    ▒█░ █ ░█ ▒███   ▒██▒ ▄██   ▓██    ▓██░▒██░  ██▒▓██  ▀█ ██▒▒██▒▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
  ░▓█▄   ▌░██▄▄▄▄██ ▒██▀▀█▄  ▓██ █▄    ░█░ █ ░█ ▒▓█  ▄ ▒██░█▀     ▒██    ▒██ ▒██   ██░▓██▒  ▐▌██▒░██░░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
  ░▒████▓  ▓█   ▓██▒░██▓ ▒██▒▒██▒ █▄   ░░██▒██▓ ░▒████▒░▓█  ▀█▓   ▒██▒   ░██▒░ ████▓▒░▒██░   ▓██░░██░  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
   ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▒ ▓▒   ░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░▓    ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
   ░ ▒  ▒   ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒ ▒░     ▒ ░ ░   ░ ░  ░▒░▒   ░    ░  ░      ░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ▒ ░    ░      ░ ▒ ▒░   ░▒ ░ ▒░
   ░ ░  ░   ░   ▒     ░░   ░ ░ ░░ ░      ░   ░     ░    ░    ░    ░      ░   ░ ░ ░ ▒     ░   ░ ░  ▒ ░  ░      ░ ░ ░ ▒    ░░   ░ 
     ░          ░  ░   ░     ░  ░          ░       ░  ░ ░                ░       ░ ░           ░  ░               ░ ░     ░     
   ░                                                         ░                                                                  

'''

def print_query_table(col1, col2,title):
    # Create a rich table
    table = Table(title=title)

    # Add columns to the table
    table.add_column("Type", justify="center", style="cyan")
    table.add_column("Site", justify="center", style="magenta")

    # Add rows to the table
    row = 0
    for site in col2:
        if row == 30 :
            break
        else:
            table.add_row(col1, site)
            row+=1

    # Print the table
    console = Console()
    console.print(table)

'''
###################
                    Useful functions
###################

'''
def create_data_to_insert(query_value, url_list):
    # Combine the fixed query value with the url list into a list of tuples
    return [(query_value, url) for url in url_list]

@click.group()
def commandList():
     pass

@click.command(help="For searching through different darkweb search engines") 
@click.option("--query",type=click.Choice(QUERY),prompt="Choose your Query",help="Choose a word from: {}".format(','.join(QUERY)))
@click.option("--engine",type=click.Choice(BROWSER),prompt="Choose search Engine",help="Choose a word from: {}".format(','.join(BROWSER)))
def search_engine(query,engine):
    search_engines = {
    "Ahima":"https://ahmia.fi/search/?q={}",
    "Torch":"http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega?P={}"
}

    console = Console()
    postgre_connect()
    tor_proxy = set_tor_proxy()
    if tor_proxy[1]:
        message="Proxy Enable"
        print(message)
        
        if engine == BROWSER[0]:

            '''
                ### LOADING >>>>>
            '''
            with console.status("[cyan]Asking to Ahima...", spinner="flip") as status:
                sites = Ahima_scraper(search_engines["Ahima"],query,tor_proxy[0])
                time.sleep(2)  # Simulating some processing time
                pass
            print_query_table(query, sites, "Fetching from Ahima")
            console.print(f"[red]more {abs(len(sites) - 30)} sites available..\n")
            with console.status("[cyan]Updating Database...",spinner="hamburger") as status:
                time.sleep(2)
                pass
            console.print(f"[red]Database Updated..\n")
            '''
            ###########
                Data base connectivity
            ###########
            '''
            ''' 
            #insert Query into Master table
            data_to_insert = create_data_to_insert(query,sites)
            insert_query = 'INSERT INTO master_table (query, url) VALUES (%s, %s) ON CONFLICT (url) DO NOTHING'
            with console.status("[cyan]Updating Database...",spinner="hamburger") as status:
                for data_tuple in data_to_insert:
                    execute_query(insert_query, params=data_tuple)
                pass
            '''
        elif engine == BROWSER[1]:
            with console.status("[cyan]Asking to Torch...", spinner="pipe") as status:
                sites = Torch_Scraper(search_engines["Torch"],query)
                time.sleep(2)  # Simulating some processing time
                pass
            print_query_table(query, sites, "Fetching from Ahima")
            console.print(f"[red]more {abs(len(sites) - 30)} sites available..\n")
            with console.status("[cyan]Updating Database...",spinner="hamburger") as status:
                time.sleep(2)
                pass
            console.print(f"[red]Database Updated..\n")
            '''
            ###########
                Data base connectivity
            ###########
            '''
            ''' 
            #insert Query into Master table
            data_to_insert = create_data_to_insert(query,sites)
            insert_query = 'INSERT INTO master_table (query, url) VALUES (%s, %s) ON CONFLICT (url) DO NOTHING'
            with console.status("[cyan]Updating Database...",spinner="hamburger") as status:
                for data_tuple in data_to_insert:
                    execute_query(insert_query, params=data_tuple)
                pass
            '''
    postgre_close_connection()

@click.command(help="Start the spyder for fetching urls")
@click.option("--timeout",default=10,help="Request timeout time")
def demospyder(timeout):
     postgre_connect()
     console_spyder = Console()
     console_spyder.print(f"[cyan]-------------------------------")
     console_spyder.print(f"[cyan]|    Going through each url   |")
     console_spyder.print(f"[cyan]-------------------------------")
     print("\n")
     '''
     ####################
      URL should be real
     ######################
     '''
     onion_sites = execute_query("SELECT url,id FROM master_table")
     with console_spyder.status("",spinner="aesthetic"):
                for sites in onion_sites:
                    status_code = random.randint(1,100)
                    print(onion_sites[sites[1]])
                    if status_code%2==0:
                        time.sleep(timeout)
                        console_spyder.print(f"[red] Error during request\n")
                    else:
                        time.sleep(5)
                        console_spyder.print(f"[green] Adding to DB\n")
     postgre_close_connection()
                    
@click.command(help="Find your email on the dark web!!!")
@click.option("--email",required =True,help="Email for find match from database")
def pawn(email):
     postgre_connect()
     console_pawn = Console()
     emaildata=execute_query("SELECT email FROM analytic_table")    
     email_list=[]
     for i in range(0,len(emaildata)):
          email_list.extend(emaildata[i][0].split(","))
     with console_pawn.status("[yellow1]Finding from the Darkweb database",spinner="dots12"):
        time.sleep(7)
        console_pawn.print(f"[aquamarine3]Your Email : {email}")
        if(email in email_list):
            console_pawn.print(f"[salmon1]Status     : Your email has been pawn !!!!\n")
        else:
            console_pawn.print(f"[gold1]Status     : You are Safe :) \n")     

     postgre_close_connection()


@click.command(help="Web archive")
@click.option("--month",type=click.Choice(MONTH),prompt="(default comparison with Jan) Month",help="Choose a month from: {}".format(','.join(MONTH)))
def web_archive(month):
    console = Console()
    postgre_connect()
    cmp_month = "jan_data"
   #f query =execute_query(f"SELECT url FROM web_archive WHERE {cmp_month} IS NOT NULL AND {month} IS NOT NULL AND {cmp_month} <> {month};")
    with console.status(" [bright_cyan]Collecting results from database..",spinner="grenade") as status:
         i=5
         while(i>0):
              time.sleep(1)
              i-=1 
    console.print(f"  [bright_cyan]{month} Data need to be collected")
    postgre_close_connection()
     


def site_process():
    postgre_connect()
    console = Console()
    onion_sites = execute_query("SELECT url,id FROM master_table WHERE result IS NULL")  
    #print(onion_sites)
    with console.status("",spinner="aesthetic") as status:
                for site_id in onion_sites:
                    print(f" Processing site: {site_id}")
                    web_visitor(site_id[0],site_id[1])
   

    postgre_close_connection()
    
def Fetching():
    postgre_connect()
    console = Console()
   # url_html_content = execute_query("SELECT url,result FROM master_table")
   # with console.status("",spinner="aesthetic") as status:
                #for url_html in url_html_content:
                #    print(f" Processing site: {url_html[0]}")
                #    analyze(url_html[0],url_html[1])
                # analyze("example.com1234",html_content)

def viewContent():
     postgre_connect()
     data = execute_query("SELECT * FROM analytic_table")
     '''
    #############
       Converting string of fetched items data[][].split(",")
    #############
    '''
     postgre_close_connection()

commandList.add_command(search_engine)
commandList.add_command(demospyder)
commandList.add_command(pawn)
commandList.add_command(web_archive)
if  __name__ == "__main__":
    clear_console ()   
    commandList()
    #query_to_browser()
    #site_process()
    #Fetching()
    #viewContent()