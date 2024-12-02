import requests , json # requests library for api and json library for json file
from time import time # time library for time
from rich import print # rich library for coloring outputs
open('data.json' , 'w')
baseurl = 'https://api.currencyfreaks.com/v2.0/rates/latest?apikey=f068cbe60b1a4837b2f63ba329b9ee8b'
response = requests.get(baseurl)
data = response.json()
with open('data.json' , 'w') as f:
    json.dump(data , f)

#main menu
def mainMenu():
    while True:
        print('[green]#[/green]'*18)
        print('[green]Currency Converter[/green]')
        print('[green]#[/green]'*18)

        # convert from currency code input 
        currencyFrom = input('write the currency code you want to convert from : ').upper()
        # convert from currency code validating input 
        while currencyFrom not in data['rates']:
            print('invalid currency code')
            print('If you don\'t know the currency code,\nplease visit ==> (https://sdk.invoicing.eta.gov.eg/codes/currencies/#list)')
            currencyFrom = input('write the currency code you want to convert from : ').upper()
        # convert to currency code input 
        currencyTo = input('write the currency code you want to convert to : ').upper()
        # convert to currency code validating input 
        while currencyTo not in data['rates']:
            print('invalid currency code')
            print('If you don\'t know the currency code,\nplease visit ==> (https://sdk.invoicing.eta.gov.eg/codes/currencies/#list)')
            currencyTo = input('write the currency code you want to convert to : ').upper()
        # amount of currency input
        amount = input('write the amount you want to convert : ')
        # amount of currency validating input
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
        # the result of 
        result = round((float(data["rates"][currencyTo])/float(data["rates"][currencyFrom]))*float(amount),3)
        # resuming or exiting menu
        print(f'[bold cyan]{amount} {currencyFrom} = {result} {currencyTo}[/bold cyan]')
        print( '#'*18)
        print( '#'*18)
        print('1 - convert another currency \n2 - exit')
        #choice input 
        choice = input('Enter your choice : ')
        #choice validating input 
        while True:
            try:
                choice = int(choice)
                if choice == 1:
                    break
                elif choice == 2:
                    print('[green]Thank You for using my application[/green]')
                    return
                else:
                    print('invalid choice')
                    choice = input('Enter your choice : ')
            except:
                print('choice should be a number')
                choice = input('Enter your choice : ')


#calling the main menu function
mainMenu()

