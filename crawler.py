import requests
from bs4 import BeautifulSoup

# Hardcode URL for testing purposes, will integrate input later
url= "https://www.roboform.com/filling-test-all-fields"        

# field list containing names or ids of text fields only; final output of the program
field= []             
try:
    # downloading HTML page
    target= requests.get(url)

    # initializing bs4 object
    soup= BeautifulSoup(target.content, 'html.parser')
    status= target.status_code

    for form in soup.find_all('input', type='text'):
        field.append([{'id': form.get('id'), 'name': form.get('name')}])

except Exception as e:
    print("Invalid URL")
    print(e)