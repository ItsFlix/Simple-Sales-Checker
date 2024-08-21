
import requests
import time
import json
import random

cookie = '_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_COOKIEHERE'

web = "WEBHOOK URL HERE"
data = {}

UserId = 'GROUPOWNERID OR GROUPADMINID HERE'
GroupId = 'GROUPID HERE'

OneRobux = 0.0035
DumbNumber = 0
TotalChecks = 0

#Perm Global Variables
TotalBalance = ''
Buyer = ''
AmountMade = ''
PendingTotal = ''
DailyTotal = ''
FinalString = ''


def Notify(name,desc,bigtext):
      data = {"username" : name}
      data["embeds"] = [{"color" : random.uniform(1000000,9999999), "description" :  desc, "title" : bigtext}]
      result = requests.post(web, json = data)


def PreSaleCheck(target,user):
    #global TotalBalance
    global DailyTotal
    global PendingTotal

    # GroupRobux = requests.get(f'https://economy.roblox.com/v1/groups/{target}/currency', cookies={".ROBLOSECURITY": cookie})
    # json66 = json.loads(GroupRobux.text)

    # MyRobux = requests.get(f'https://economy.roblox.com/v1/users/{user}/currency', cookies={".ROBLOSECURITY": cookie})
    # json69 = json.loads(MyRobux.text)

    GroupSalesInfo = requests.get(f'https://economy.roblox.com/v1/groups/{target}/revenue/summary/day', cookies={".ROBLOSECURITY": cookie})
    json44 = json.loads(GroupSalesInfo.text)
    DailyTotal = json44['itemSaleRobux']
    PendingTotal = json44['pendingRobux']

    print("PreChecked Today's Sales " + str(DailyTotal*OneRobux ) + ' USD')
    print('PreChecked Pending Robux ' + str(PendingTotal*OneRobux) + ' USD')
    Notify('Started Program',"PreChecked Today's Sales " + str(DailyTotal*OneRobux ) + ' USD','PreChecked Pending Robux ' + str(PendingTotal*OneRobux) + ' USD')



def SaleCheck(target,user):
     global TotalBalance
     global Buyer
     global AmountMade
     global PendingTotal
     global DailyTotal
     global FinalString
     global DumbNumber
     global TotalChecks

     #https://www.roblox.com/groups/configure?id=14780120#!/revenue   NOT NEEDED
    #  Page = requests.get(f'https://www.roblox.com/groups/configure?id={target}#!/revenue', cookies={".ROBLOSECURITY": cookie})
    #  Soup = BeautifulSoup(Page.content , "html.parser")
     #print(Soup)

     #https://groups.roblox.com/v1/groups/14780120  NOT NEEDED
    #  GroupInfo = requests.get(f'https://groups.roblox.com/v1/groups/{target}', cookies={".ROBLOSECURITY": cookie})
    #  json2 = json.loads(GroupInfo.text)
    #  print(str(json2['id']))

     #https://economy.roblox.com/v1/groups/14780120/revenue/summary/day
     GroupSalesInfo = requests.get(f'https://economy.roblox.com/v1/groups/{target}/revenue/summary/day', cookies={".ROBLOSECURITY": cookie})
     json4 = json.loads(GroupSalesInfo.text)
     #print(str(PendingTotal))


     #https://economy.roblox.com/v1/groups/14780120/currency
     GroupRobux = requests.get(f'https://economy.roblox.com/v1/groups/{target}/currency', cookies={".ROBLOSECURITY": cookie})
     json1 = json.loads(GroupRobux.text)
     #print(str(json1['robux']))

     #https://economy.roblox.com/v1/users/1984684915/currency
     MyRobux = requests.get(f'https://economy.roblox.com/v1/users/{user}/currency', cookies={".ROBLOSECURITY": cookie})
     json3 = json.loads(MyRobux.text)
     #print(str(json3['robux']))

     TotalBalance = json1['robux'] + json3['robux'] + json4['pendingRobux']

     DumbNumber = DumbNumber + 1
     TotalChecks = TotalChecks + 1
     if DumbNumber == 5:
        DumbNumber = 0
        print('Checked x' +str(TotalChecks))
        print('Balance: ' + str(TotalBalance*OneRobux) + ' USD')


     # RESULTS
     # 30 000 = 105.00 USD
     # 10 000 = 35
     # 1000 = 3.5
     # 100 = 0.35
     # 10 = 0.035
     # 1 = 0.0035

     
     if PendingTotal != json4['pendingRobux']:
        AmountMade = json4['pendingRobux'] - PendingTotal

        DailyTotal = json4['itemSaleRobux']
        PendingTotal = json4['pendingRobux']

        FinalString = 'Recieved '+str(AmountMade*OneRobux) + ' USD ' + ' Balance: ' + str(TotalBalance*OneRobux) + ' USD'
        Notify('Balance Changed','',FinalString)
        print(FinalString)

          



PreSaleCheck(GroupId,UserId)
time.sleep(1)
while True:
     SaleCheck(GroupId,UserId)
     time.sleep(5)
