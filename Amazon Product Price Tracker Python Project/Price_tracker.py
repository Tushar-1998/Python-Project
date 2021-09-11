# Problem statement: How to Track the product prices from Amazon/Flipkart.
import bs4
import urllib.request
import smtplib
import time

prices_list = []

def check_price():
    url = 'https://www.amazon.in/Infinity-Glide-500-Wireless-Headphones/dp/B07W5MYRF4/ref=sr_1_4?crid=2387SDRCXDODZ&dchild=1&keywords=jbl+bluetooth+headphones+%E0%A4%82+infinity&qid=1625542182&smid=A14CZOWI0VEHLG&sprefix=jbl+bluetooth+headphones+%E0%A4%82%2Caps%2C342&sr=8-4'

    sauce = urllib.request.urlopen(url).read()
    soup = bs4.BeautifulSoup(sauce, "html.parser")

    prices = soup.find(id="priceblock_dealprice").get_text()
    prices = float(prices.replace(",","").replace("₹", ""))
    #print(prices, type(prices))
    prices_list.append(prices)
    return prices

def send_email(message):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("tushargoel29jan@gmail.com", "Tushar@9958")
    s.sendmail("tushargoel29jan@gmail.com", "tushar29jan@gmail.com", message)
    s.quit()

send_email("Prices Of your Product JBL Infinity is 1000")

# Checking the prices decrease of product.
def price_decrease_check(prices_list):
    if prices_list[-1] < prices_list[-2]:
        return True
    else:
        return False

count = 1

while True:
    current_price = check_price()
    if count > 1:
        flag = price_decrease_check(prices_list)
        if  flag:
            decrease = prices_list[-1] - prices_list[-2]
            message = f"The price has been decreased please check the product. The price decreased by {decrease} rupees."
            send_email(message)
    time.sleep(43000)
    count += 1


