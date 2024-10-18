import csv
import requests
import json
from xml.dom.minidom import parseString



chargeitemid = 0
description = ""
Testbase_url = ""
#Prodbase_url = ""
action_url = ""

with open(SpringRentPenalty2.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
       
        print(row['EntryID'])
        # url = "" 
        URL = Testbase_url +action_url +row['EntryID'] + "?"  
       # print(URL)
        
       
        if row['SpringRentPenaltyAssessed'] == 'FALSE':
            if row['End Booking Reason ID'] == '9':
                    #print('--------')
                    chargeitemid = 0
                    description = ''
                    #Look for Buildind to assign chargeitemid and description values
                    if row['RoomLocationID'] == '1':
                        print('Acadian Hall')
                        chargeitemid = 5707
                        description = "Rent Penalty SPRING-ACD"
                    elif row['RoomLocationID'] == '3':
                        print('Blake Hall')
                        chargeitemid = 5709
                        description = "Rent Penalty SPRING-BLA"
                    elif row['RoomLocationID'] == '4':
                        print('Broussard')
                        chargeitemid = 5710
                        description = "Rent Penalty SPRING-BRO"
                    elif row['RoomLocationID'] == '5':
                        print("East Campus Apartment")
                        chargeitemid = 5729
                        description = "Rent Penalty SPRING-ECA"
                    elif row['RoomLocationID'] == '6':
                        print('West Campus Apartments')
                        chargeitemid = 5730
                        description = "Rent Penalty SPRING-WCA"
                    elif row['RoomLocationID'] == '9':
                        print("Herget")
                        chargeitemid = 5715
                        description = "Rent Penalty SPRING-HGT"
                    elif row['RoomLocationID'] == '10':
                        print('Annie Boyd')
                        chargeitemid = 0
                        description = ""
                    elif row['RoomLocationID'] == '12':
                        print('Louise Garig')
                        chargeitemid = 5718
                        description = "Rent Penalty SPRING-LGH"
                    elif row['RoomLocationID'] == '14':
                        print('East Laville')
                        chargeitemid = 5711
                        description = "Rent Penalty SPRING-ELV"
                    elif row['RoomLocationID'] == '15':
                        print('West Laville')
                        chargeitemid = 5725
                        description = "Rent Penalty SPRING-WLV"
                    elif row['RoomLocationID'] == '16':
                        print('mcVoy')
                        chargeitemid = 5719
                        description = "Rent Penalty SPRING-MCV"
                    elif row['RoomLocationID'] == '17':
                        print('Miller')
                        chargeitemid = 5720
                        description = "Rent Penalty SPRING-MLR"
                    elif row['RoomLocationID'] == '20':
                        print('North/ RC3')
                        chargeitemid = 5723
                        description = "Rent Penalty SPRING-RC3"
                    elif row['RoomLocationID'] == '21':
                        print('Beauregard')
                        chargeitemid = 5708
                        description = "Rent Penalty SPRING-BEA"
                    elif row['RoomLocationID'] == '22':
                        print('Jackson')
                        chargeitemid = 5716
                        description = "Rent Penalty SPRING-JAC"
                    elif row['RoomLocationID'] == '23':
                        print('Lejeune')
                        chargeitemid = 5717
                        description = "Rent Penalty SPRING-LEJ"
                    elif row['RoomLocationID'] == '24':
                        print('Taylor')
                        chargeitemid = 5724
                        description = "Rent Penalty SPRING-TAY"
                    elif row['RoomLocationID'] == '25':
                        print('SouthHall/ RC1')
                        chargeitemid = 5721
                        description = "Rent Penalty SPRING-RC1"
                    elif row['RoomLocationID'] == '26':
                        print('West Hall/ RC2')
                        chargeitemid = 5722
                        description = "Rent Penalty SPRING-RC2"
                    elif row['RoomLocationID'] == '29':
                        print('Cypress')
                        chargeitemid = 6669
                        description = "Rent Penalty SPRING-CYP"
                    elif row['RoomLocationID'] == '35':
                        print('Spruce')
                        chargeitemid = 6994
                        description = "Rent Penalty SPRING-SPR"
                    elif row['RoomLocationID'] == '42':
                        print("NGW")
                        chargeitemid = 6995
                        description = "Rent Penalty SPRING-NGW"
                    elif row['RoomLocationID'] == '43':
                        print("NGW")
                        chargeitemid = 6995
                        description = "Rent Penalty SPRING-NGW"
                    elif row['RoomLocationID'] == '44':
                        print("NGW")
                        chargeitemid = 6995
                        description = "Rent Penalty SPRING-NGW"
                    elif row['RoomLocationID'] == '45':
                        print("NGW")
                        chargeitemid = 6995
                        description = "Rent Penalty SPRING-NGW"
                    elif row['RoomLocationID'] == '46':
                        print("NGW")
                        chargeitemid = 6995
                        description = "Rent Penalty SPRING-NGW"
                    elif row['RoomLocationID'] == '47':
                        print("NGW")
                        chargeitemid = 6995
                        description = "Rent Penalty SPRING-NGW"
                    elif row['RoomLocationID'] == '50':
                        print("NGW")
                        chargeitemid = 6995
                        description = "Rent Penalty SPRING-NGW"
                    elif row['RoomLocationID'] == '51':
                        print("Evangeline")
                        chargeitemid = 5713
                        description = "Rent Penalty SPRING-EVG"
                    elif row['RoomLocationID'] == '52':
                        print('Cedar')
                        chargeitemid = 7500
                        description = "Rent Penalty SPRING-CDR"
                    elif row['RoomLocationID'] == '53':
                        print("Highland")
                        chargeitemid = 5714
                        description = "Rent Penalty SPRING-HGH"
                    elif row['RoomLocationID'] == '56':
                        print("Azalea")
                        chargeitemid = 7712
                        description = "Rent Penalty SPRING-AZL"
                    elif row['RoomLocationID'] == '57':
                        print("Camellia")
                        chargeitemid = 7720
                        description = "Rent Penalty SPRING-CAM"
                    else:
                        print('Nothing')
                    querystring ={
                                'TransactionTypeEnum':'Charge',
                                'ChargeItemId':chargeitemid,    
                                'Description':description,
                                "Amount":row['Amount'],
                                "TermSessionID":row['TermSessionID']        
                            }
                    headers = {
                                'Authorization': 'Basic '
                         }
                    response = requests.request("GET",URL,headers=headers,params=querystring)
                    #print(response.text)
                    data = response.text
                    print(data)
                    #print(querystring)
                    #print(URL)
                    print(response.status_code)
                    print('------------------')
                    document = parseString(data)
                    print(document.getElementsByTagName("TransactionID")[0].firstChild.nodeValue)
                    print(document.getElementsByTagName("EntryID")[0].firstChild.nodeValue)
                    print(document.getElementsByTagName("TransactionDate")[0].firstChild.nodeValue)
                    print(document.getElementsByTagName("Amount")[0].firstChild.nodeValue)
                    print(document.getElementsByTagName("Description")[0].firstChild.nodeValue)
                    print('--------------------------')


                    if (response.status_code == 200):
                        updateURL = Testbase_url + "update/Booking/" + row['BookingID'] + "?CustomBit2=TRUE"

                        querystring ={
                          }
                        headers = {
                                      'Authorization': 'Basic '
                                        
                          }

                        response2 = requests.request("GET",updateURL,headers=headers,params=querystring)
                        print(response2.text)
                        data2 = response2.text
                        print('----------')
            elif row['End Booking Reason ID'] == '0':
                print("No Spring Penalty")
        elif  row['SpringRentPenaltyAssessed'] == 'TRUE':
            print("Spring Rent Penalty Flag set to True")
      
       