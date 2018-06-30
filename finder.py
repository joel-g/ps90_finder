from selenium import webdriver
from bs4 import BeautifulSoup
from smtplib import SMTP as SMTP
import schedule
import time

def getSizes():
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://ammoseek.com/guns/9mm-luger/Glock?ikw=26")
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    for price in soup.find_all("td):
        if price.contents[0] == '$447.99':
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

schedule.every().day.at("07:00").do()

# while True:

    # schedule.run_pending()
    # time.sleep(1)
getGuns()