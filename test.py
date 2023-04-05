from calendar import month
import requests
import datetime
import json

keep_going = True
today = datetime.date.today()
date = datetime.datetime(2023,3,1)

while keep_going:
    
    params = {
        "date": date.date(),
        "vendor_name": "SAZERAC COMPANY  INC",
        "category_name": "STRAIGHT BOURBON WHISKIES",
        "im_desc": "BLANTONS BUY THE BARREL",
        # "city": "ANKENY"
    }
    url = f"https://data.iowa.gov/resource/m3tr-qhgy.json"

    response = requests.get(url, params=params)
    if response.json():
        print(date.date())
        with open(f"sazerac_sales/{date.date()}.json", "w") as file:
            file.write(json.dumps(response.json()))
        # print(url)
        # print(response.json()[0])
        # print("more info")
    if date.date() == today:
        keep_going = False
    
    date += datetime.timedelta(days=1)
