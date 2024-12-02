import requests , json 
from time import time
from rich import print
open('data.json' , 'w')
baseurl = 'https://api.currencyfreaks.com/v2.0/rates/latest?apikey=f068cbe60b1a4837b2f63ba329b9ee8b'
# print(('https://sdk.invoicing.eta.gov.eg/codes/currencies/#list'))
response = requests.get(baseurl)
data = response.json()
with open('data.json' , 'w') as f:
    json.dump(data , f)

def mainMenu():
    while True:
        print('[green]#[/green]'*18)
        print('[green]Currency Converter[/green]')
        print('[green]#[/green]'*18)

        currencyFrom = input('write the currency code you want to convert from : ').upper()
        while currencyFrom not in data['rates']:
            print('invalid currency code')
            print('If you don\'t know the currency code,\nplease visit ==> (https://sdk.invoicing.eta.gov.eg/codes/currencies/#list)')
            currencyFrom = input('write the currency code you want to convert from : ').upper()
        currencyTo = input('write the currency code you want to convert to : ').upper()
        while currencyTo not in data['rates']:
            print('invalid currency code')
            print('If you don\'t know the currency code,\nplease visit ==> (https://sdk.invoicing.eta.gov.eg/codes/currencies/#list)')
            currencyTo = input('write the currency code you want to convert to : ').upper()
        amount = input('write the amount you want to convert : ')
        while True:
            try:
                amount = float(amount)
                if amount < 0:
                    print('amount must be positive')
                    amount = input('write the amount you want to convert : ')
                else:
                    break
            except:
                print('amount should be a number')
                amount = input('write the amount you want to convert : ')
        result = round((float(data["rates"][currencyTo])/float(data["rates"][currencyFrom]))*float(amount),3)
        print(f'[bold cyan]{amount} {currencyFrom} = {result} {currencyTo}[/bold cyan]')
        print( '#'*18)
        print( '#'*18)
        print('1 - convert another currency \n2 - exit')
        choice = input('Enter your choice : ')
        while True:
            try:
                choice = int(choice)
                if choice == 1:
                    break
                elif choice == 2:
                    return
                else:
                    print('invalid choice')
                    choice = input('Enter your choice : ')
            except:
                print('choice should be a number')
                choice = input('Enter your choice : ')
mainMenu()





# egpCurrfromUSD = data['rates']['EGP']
# AUDCurrfromUSD = data['rates']['AED']
# print(float(AUDCurrfromUSD)/float(egpCurrfromUSD))
