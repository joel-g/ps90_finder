from smtplib import SMTP as SMTP
import schedule, requests, time

p90_urls = ("https://www.wholesalehunter.com/Product/Details/71136",
"https://www.wholesalehunter.com/Product/Details/93893",
"https://www.wholesalehunter.com/Product/Details/1003008",
"https://www.wholesalehunter.com/Product/Details/71136","https://vizardsgunsandammo.com/fn-3848950460-ps90-semi-auto-5-7x28mm-16-30-1-black-alloy/","https://vizardsgunsandammo.com/fn-3848950460-ps90-standard-semi-automatic-5-7mmx28mm-16-30-1-synthetic-black-stock-black/",
"https://www.ableammo.com/catalog/herstal-ps90-rifle-3848950060-57mmx28mm-1604-synthetic-stock-black-finish-p-137454.html",
"https://www.ableammo.com/catalog/herstal-ps90-semi-auto-rifle-3848950460-57mmx28mm-1604-synthetic-stock-black-finish-p-119529.html",
"https://www.ableammo.com/catalog/herstal-ps90-standard-rifle-3848950465-57mmx28mm-black-synthetic-stock-black-finish-rds-p-152598.html",
"https://www.ableammo.com/catalog/herstal-ps90-semi-auto-rifle-wred-dot-3848950462-57mmx28mm-synthetic-stock-black-finish-p-135724.html")


def look_for_guns(urls):
    report = ""
    for url in urls:
        res = requests.get(url)
        if "BACKORDER" or "OUT OF STOCK" in res.text:
            report = report + url + " is not in stock\n"
        elif "ADD TO CART" or "Total qty available" or "checkoutButton" in res.text:
            report = report + url + " has it! BUY IT! BUY IT!\n"
        else:
            report = report + url + " could not be parsed.\n"
    return report

def get_creds():
    with open('config.ini','r') as config:
        creds = config.readlines()
        email = creds[0].rstrip()
        pwd = creds[1].rstrip()
        return {"email": email, "pwd": pwd}

def send_email(message):
    user = "<YOUR_EMAIL>"
    pswrd = "<YOUR_PASSWORD>"
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

# schedule.every().day.at("07:00").do(look_for_guns(p90_urls))

# while True:

    # schedule.run_pending()
    # time.sleep(1)
# getGuns()

print(get_creds()['pwd'])