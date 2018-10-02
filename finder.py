from smtplib import SMTP as SMTP
import schedule, requests, time, sys

p90_urls = ("https://www.wholesalehunter.com/Product/Details/71136",
"https://www.wholesalehunter.com/Product/Details/93893",
"https://www.wholesalehunter.com/Product/Details/1003008",
"https://www.wholesalehunter.com/Product/Details/71136","https://vizardsgunsandammo.com/fn-3848950460-ps90-semi-auto-5-7x28mm-16-30-1-black-alloy/","https://vizardsgunsandammo.com/fn-3848950460-ps90-standard-semi-automatic-5-7mmx28mm-16-30-1-synthetic-black-stock-black/",
"https://www.ableammo.com/catalog/herstal-ps90-rifle-3848950060-57mmx28mm-1604-synthetic-stock-black-finish-p-137454.html",
"https://www.ableammo.com/catalog/herstal-ps90-semi-auto-rifle-3848950460-57mmx28mm-1604-synthetic-stock-black-finish-p-119529.html",
"https://www.ableammo.com/catalog/herstal-ps90-standard-rifle-3848950465-57mmx28mm-black-synthetic-stock-black-finish-rds-p-152598.html",
"https://www.ableammo.com/catalog/herstal-ps90-semi-auto-rifle-wred-dot-3848950462-57mmx28mm-synthetic-stock-black-finish-p-135724.html",
"https://palmettostatearmory.com/fnh-ps90.html")

sneaker_urls = ("https://www.neimanmarcus.com/p/off-white-mens-suede-leather-high-top-sneakers-white-black-prod200450489",
"https://www.off---white.com/en/US/men/products/omia102f18b040160130",
"https://www.farfetch.com/shopping/men/off-white-white-industrial-hi-top-leather-trainers-item-13164358.aspx",
"https://www.endclothing.com/us/off-white-high-top-sneaker-omia077s187840010101.html",
"https://www.matchesfashion.com/us/products/1227732?qxjkl=tsid:38929|cgn:tZkYzve9Cvk&c3ch=LinkShare&c3nid=tZkYzve9Cvk&utm_source=linkshare&utm_medium=affiliation&utm_campaign=us&utm_content=tZkYzve9Cvk&rffrid=aff.linkshare.3341494.37420",
"https://www.ssense.com/en-us/men/product/off-white/white-and-blue-industrial-high-top-sneakers/3051298?utm_source=stylight_us&utm_medium=cpc&utm_term=XXXXXX",
"https://www.vrients.com/usa/off-white-virgil-abloh-high-top-sneakers-white.html",
"https://www.mrporter.com/en-us/mens/off_white/industrial-leather--suede-and-ripstop-high-top-sneakers/1066117?ppv=2",
)

matches = ["backorder", "out of stock", "item not available", "sold out"]


def get_report(urls):
    report = ""
    for url in urls:
        res = requests.get(url)
        if any(match in res.text.lower for match in matches):
            report = report + url + " is not in stock\n"
        elif "add to cart" or "total qty available" or "checkoutButton" in res.text.lower:
            report = report + url + " has it! BUY IT! BUY IT!\n"
        else:
            report = report + url + " could not be parsed.\n"
    return report

def get_creds():
    with open('config.ini','r') as config:
        creds = config.readlines()
        email = creds[0].rstrip()
        pwd = creds[1].rstrip()
        rec = creds[2].rstrip()
        return {"email": email, "pwd": pwd, "rec": rec}

def send_email(message):
    creds = get_creds()
    conn = SMTP(host="smtp.gmail.com", port=587)
    conn.ehlo()
    conn.starttls()
    conn.ehlo()
    conn.login(creds['email'],creds['pwd'])
    conn.sendmail(creds['email'], creds['rec'], message)
    print("Email sent!")
    conn.close()

def look_for_guns():
    report = get_report(p90_urls)
    if "BUY IT!" in report:
        send_email(report)
    print(report)

def look_for_sneaks():
    report = get_report(sneaker_urls)
    if "BUY IT!" in report:
        send_email(report)
    print(report)

if sys.argv[1] is "sneakers":
    schedule.every().day.at("07:00").do(look_for_sneaks)
elif sys.argv[1] is "guns":
    schedule.every().day.at("07:00").do(look_for_guns)


while True:
    schedule.run_pending()
    time.sleep(1)
