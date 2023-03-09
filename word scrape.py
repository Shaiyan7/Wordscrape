import requests
from bs4 import BeautifulSoup

# prompt user for input
word = input("Enter a word: ")

# send GET request to Merriam-Webster's website
url = "https://www.merriam-webster.com/dictionary/" + word
response = requests.get(url)

# parse HTML using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# find the definition of the word
definition = soup.find('span', class_='dtText').text

# display the meaning of the word
print("The meaning of", word, "is:", definition)