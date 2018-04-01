import json
import requests
import os
import time
from win10toast import ToastNotifier


toaster = ToastNotifier()
temp = "tmpbuy"
icon_path = 'bitcoin.ico'


def write_data(data): #wriing data to file
    file = open (temp , "w+")
    file.write(str(data))
    file.close()

def read_data(): #reading data to file
    if not os.path.isfile(temp):
        write_data('0')
    file = open(temp)
    return file.read()

def send_message(msg):
    '''you can yous your message api here'''

def pricing(): # compare the pricing and output the result
    request = requests.get("https://www.zebapi.com/api/v1/market/ticker/btc/inr")
    data = json.loads(request.content.decode())
    old_price = float(read_data())
    new_price = float(data["buy"])
    current_price = str(new_price)
    
    if old_price > new_price :
        diff = old_price - new_price
        diff = str(diff)
        status = 'Getting down'
        msg = "price is getting down with rs: " + diff+ " present price is : " + current_price
        toaster.show_toast(status,msg,icon_path=icon_path)
        
        
    elif old_price < new_price :
        diff = new_price - old_price
        diff = str(diff)
        status = 'Getting up'
        msg = "price is getting up with rs: " + diff + " present price is : " + current_price
        toaster.show_toast(status,msg,icon_path=icon_path)
        
        
        
        
    else:
        status = 'No Diffrence'
        msg = "No Diffrence , present price is : " + current_price
        toaster.show_toast(status,msg,icon_path=icon_path)
    old_price = new_price
    write_data(new_price)

while True:
    pricing()
    time.sleep(60*60)
    


