
import time
import requests
import json
from tests.base_test import BaseTest
class CancelOrders():
  def cancel_new_orders(self):
    '''this function will fetch all created orders and extract id's for new order and finally cancel those orders'''

    url = "https://api-partner.uat.cheq.io/mercuri/api/suite-management/customer-orders?source=ACTIVE_ORDER"

    payload = {}
    headers = {
      'accept': 'application/json, text/plain, */*',
      'accept-language': 'en',
      'access-control-allow-origin': '*',
      'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTgyNTMzLCJjdXN0b21lcl90eXBlIjoiUkVHSVNURVJFRCIsInZlcmlmaWVkQ3VzdG9tZXJQYXJ0bmVySWQiOm51bGwsImlhdCI6MTc0MjAxNTE3NywiZXhwIjoxNzQ0NjA3MTc3fQ.v5qY26TPoVgaWjlQGNLQFijRQMRGrb7Ehu3iI3myxF8',
      'if-none-match': 'W/"42d64-L+PBuEaVw4Sc4J3maBJVPTToo7w"',
      'origin': 'https://suites.uat.cheqplease.com',
      'priority': 'u=1, i',
      'referer': 'https://suites.uat.cheqplease.com/',
      'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'cross-site',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response = response.text

    data = json.loads(response)

    # Extract the ID where orderStatus is "1"
    order_Ids = []

    for i in range(len(data['data']['rows'])) :
      if data['data']['rows'][i]['orderStatus'] == '1':
        order_Ids.append(data['data']['rows'][i]['id'])
        # print(data['data']['rows'][i]['id'])

    print('Total New Order: ',len(order_Ids))

    if len(order_Ids) > 0:

      # now cancel those order using cancel-order api
      url = "https://api-partner.uat.cheq.io/mercuri/api/suite-management/cancel-order"


      headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en',
        'access-control-allow-origin': '*',
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTgyNTMzLCJjdXN0b21lcl90eXBlIjoiUkVHSVNURVJFRCIsInZlcmlmaWVkQ3VzdG9tZXJQYXJ0bmVySWQiOm51bGwsImlhdCI6MTc0MjAxNTE3NywiZXhwIjoxNzQ0NjA3MTc3fQ.v5qY26TPoVgaWjlQGNLQFijRQMRGrb7Ehu3iI3myxF8',
        'content-type': 'application/json',
        'origin': 'https://suites.uat.cheqplease.com',
        'priority': 'u=1, i',
        'referer': 'https://suites.uat.cheqplease.com/',
        'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
      }
      time.sleep(3)
      for id in order_Ids:
        payload = json.dumps({
          "orderId": id
        })
        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
