import requests

#  -- AHMIA SCRAPER --

def Scraper():
    import requests
    import random
    
    yourquery = input("Enter Query : ")
  

    if " " in yourquery:
        yourquery = yourquery.replace(" ","+")

    url = "https://ahmia.fi/search/?q={}".format(yourquery)
    #print(url)

    #lets set up some fake user agents
    ua_list = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19577"
    ,"Mozilla/5.0 (X11) AppleWebKit/62.41 (KHTML, like Gecko) Edge/17.10859 Safari/452.6", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2656.18 Safari/537.36"
    ,"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36", "Mozilla/5.0 (Linux; U; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13","Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27"
    ,"Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; zh-cn) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27"]
    ua = random.choice(ua_list)
    headers = {'User-Agent': ua}
    #this should work



    request = requests.get(url, headers=headers) #, verify=False)
    content = request.text


    def findlinks(content, path="sites"):
        import re
        import csv
        import random
        import os
        # Takes in content (webpage in string format) and searches it with regex
        regexquery = "\w+\.onion"
        
        # Regex query for finding onion links
        mineddata = re.findall(regexquery, content)
        
        # Remove duplicates while maintaining order
        mineddata = list(dict.fromkeys(mineddata))

        filename = f"{yourquery}.csv"
        
        # Construct the full path based on the specified directory
        full_path = os.path.join(path, filename)
        directory = os.path.dirname(full_path)

    # Check if the directory exists, and create it if not
        if not os.path.exists(directory):
            os.makedirs(directory)
        print("Saving to ...", full_path)

        # Check if the file already exists
        file_exists = os.path.exists(full_path)

        # Open the CSV file in append mode if it exists, otherwise in write mode
        with open(full_path, "a" if file_exists else "w", newline="", encoding="utf-8") as csvfile:
            # Create a CSV writer object
            csvwriter = csv.writer(csvfile)

            # Write the mined data to the CSV file
            for link in mineddata:
                csvwriter.writerow([f"http://{link}"])

        print("All the data written to a CSV file:", full_path)

# Example usage:
# content_example = "<html>... (webpage content)"
# Specify the desired path (replace "." with the desired directory)
# findlinks(content_example, path="/path/to/save/csv")




    if request.status_code == 200:
        print("Request went through. \n")
        #print(content)
        findlinks(content)

Scraper()
