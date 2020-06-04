import requests
from bs4 import BeautifulSoup
import smtplib

def check_price():
	DESIRED_PRICE = 1500
	
	URL = "https://www.amazon.ca/Sony-XBR65X900F-LCD-Television-65/dp/B078GZYDFK/ref=sr_1_19?keywords=4k+tv+65%22&qid=1582430012&sr=8-19"

	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"}

	page = requests.get(URL, headers=headers) # Grab all the info from the page. Think of it as if you're making a request to that page and you're returning the information

	soup = BeautifulSoup(page.content, 'html.parser')
	# print(soup.prettify()) # Print to show the info you get from soup

	title = soup.find(id="productTitle").get_text().strip()
	# print(title.strip())

	html_price = soup.find(id="priceblock_ourprice").get_text()
	# print(price)

	# Convert price
	slice_price = ''.join([i for i in html_price[5:10] if i.isdigit()])

	convert_price = float(slice_price)
	# print(convert_price)

	if(convert_price > DESIRED_PRICE): 
		send_email(URL, title)
	else:
		print('Price did not decrease')

# Send updated price
def send_email(URL, title):
	SEND_EMAIL = 'saititsd2020@gmail.com'
	SEND_PASS = 'daxbraybalookilaaries123'
	MY_EMAIL = 'lei.matt7@gmail.com'
	
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login(SEND_EMAIL, SEND_PASS) #email, password
	
	subject = title + ' Price Decreased!'
	body = 'Price decreased for' + title + '\n\nCheck the following link: ' + URL
	msg = f"Subject: {subject}\n\n{body}"

	# send email
	server.sendmail(SEND_EMAIL, MY_EMAIL, msg)

	print('email sent')
	server.quit()

def main():
	check_price()

if __name__ == "__main__":
	main()