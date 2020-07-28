import requests
from bs4 import BeautifulSoup

#Hardcode URL for testing purposes, will integrate input later
url= "https://www.roboform.com/filling-test-all-fields"     #needs to be verified as valid URL
target= requests.get(url)                                   #downloading HTML page
soup= BeautifulSoup(target.content, 'html.parser')          #initialising bs4 object
status= target.status_code

field= []                                                   #contains names or ids of text fields only; final output of the program

for form in soup.find_all('input'):
    '''
        Build input field list here
            Remember to only record text inputs
    '''
