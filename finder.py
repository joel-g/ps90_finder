from selenium import webdriver
from bs4 import BeautifulSoup
from smtplib import SMTP as SMTP
import schedule, requests
import time

p90_urls = ("https://www.wholesalehunter.com/Product/Details/71136",
"https://www.wholesalehunter.com/Product/Details/93893",
"https://www.wholesalehunter.com/Product/Details/1003008",
"https://www.wholesalehunter.com/Product/Details/71136","https://vizardsgunsandammo.com/fn-3848950460-ps90-semi-auto-5-7x28mm-16-30-1-black-alloy/","https://vizardsgunsandammo.com/fn-3848950460-ps90-standard-semi-automatic-5-7mmx28mm-16-30-1-synthetic-black-stock-black/",
"https://www.ableammo.com/catalog/herstal-ps90-rifle-3848950060-57mmx28mm-1604-synthetic-stock-black-finish-p-137454.html",
"https://www.ableammo.com/catalog/herstal-ps90-semi-auto-rifle-3848950460-57mmx28mm-1604-synthetic-stock-black-finish-p-119529.html",
"https://www.ableammo.com/catalog/herstal-ps90-standard-rifle-3848950465-57mmx28mm-black-synthetic-stock-black-finish-rds-p-152598.html",
"https://www.ableammo.com/catalog/herstal-ps90-semi-auto-rifle-wred-dot-3848950462-57mmx28mm-synthetic-stock-black-finish-p-135724.html")






g26 = "https://ammoseek.com/guns/9mm-luger/Glock?ikw=26"

def getGuns():
    driver = webdriver.Chrome('./chromedriver')
    driver.get(g26)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    for price in soup.find_all("td"):
        print(price.contents)
        if "447.99" in price.contents[0]:
            print("found one")
    driver.quit()



def sendEmail():
    user = "<YOUR_EMAIL>"
    pswrd = "<YOUR_PASSWORD>"
    message = "Found a Glock 26"
    conn = SMTP(host="smtp.gmail.com", port=587)
    conn.ehlo()
    conn.starttls()
    conn.ehlo()
    sender = user
    recipient = user
    conn.login(user,pswrd)
    conn.sendmail(sender,recipient,message)
    print("Email sent!")
    conn.close()

schedule.every().day.at("07:00").do(getGuns)

# while True:

    # schedule.run_pending()
    # time.sleep(1)
# getGuns()

for url in p90_urls:
    res = requests.get(url)
    if "BACKORDER" or "OUT OF STOCK" in res.text:
        print("not in stock")
    elif "ADD TO" in res.text:
        print("in stock")
    else:
        print("inconclusive")