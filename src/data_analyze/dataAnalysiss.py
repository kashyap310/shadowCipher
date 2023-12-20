import pandas as pd
import tldextract
import hashlib
from bs4 import BeautifulSoup
import os

# Create a folder to store the result CSV files
result_folder = 'Analysis_Results'
os.makedirs(result_folder, exist_ok=True)

# Define the result CSV file path
result_csv_path = os.path.join(result_folder, 'analysis_results.csv')

def analyze_website(url, html_content):
    results = []

    # Check for known phishing keywords
    phishing_keywords = ['login', 'password', 'credit card', 'social security']
    for keyword in phishing_keywords:
        if keyword.lower() in html_content.lower():
            results.append(f"Warning: Possible phishing keyword '{keyword}' found.")

    # Extract and analyze the domain
    domain_info = tldextract.extract(url)
    results.append(f"Domain: {domain_info.domain}, Subdomain: {domain_info.subdomain}, Suffix: {domain_info.suffix}")

    # Check for SSL/TLS encryption
    results.append("The site uses SSL/TLS encryption." if url.startswith('https://') else "Warning: The site does not use SSL/TLS encryption.")

    # Extract and print links in the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True)]
    title_tags = soup.find_all('title')

    # Print the content of each title tag
    for title_tag in title_tags:
        results.append(f"Title: {title_tag.text.strip()}")

    if links:
        results.append("Links found in the HTML content:")
        for link in links:
            results.append(link)

    paragraphs = soup.find_all('p')

    # Check each paragraph for the presence of "http" in the text
    for paragraph in paragraphs:
        paragraph_text = paragraph.text
        if "http" in paragraph_text:
            results.append(f"Link found in paragraph: {paragraph_text}")

    # Calculate a hash of the HTML content for later comparison
    html_hash = hashlib.sha256(html_content.encode('utf-8')).hexdigest()
    results.append(f"HTML Content Hash: {html_hash}")

    return results


# Function to process CSV file and call analyze_website for each row
def process_csv(csv_file):
    df = pd.read_csv(csv_file, names=['url', 'html_content'])

    result_data = []

    for index, row in df.iterrows():
        result = analyze_website(row['url'], row['html_content'])
        result_data.extend(result)
        print("------------------------------")

    # Convert the result data to a DataFrame
    result_df = pd.DataFrame(result_data, columns=['Analysis Results'])

    # Create or append to the result CSV file
    result_df.to_csv(result_csv_path, mode='a', header=not os.path.exists(result_csv_path), index=False)

# Replace 'your_csv_file.csv' with the path to your CSV file
process_csv('Crawled_data/html.csv')
