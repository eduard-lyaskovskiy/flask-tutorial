exchange_rates = {
    'BUY' : {
        'USD':18.2600, 	
        'EUR':20.1200,
        'RON':3.9100,	
        'UAH':0.4700,	
        'GBP':23.8000,
        'CHF':19.4300,	
    },
    'SELL' : {
        'USD':18.4100, 	
        'EUR':20.2900,
        'RON':4.1100,	
        'UAH':0.5700,	
        'GBP':24.3000,
        'CHF':19.8300,
    }
}
def curs():
    print('Enter operation type "BUY" or "SELL"')
    operation_type = input()
    if operation_type in exchange_rates:
        print('Enter currency: USD, EUR, RON, UAH, GBP, CHF')
        currency_input = input()
        if currency_input in exchange_rates['BUY']:
            print(f'Enter {currency_input} sum')
            mdl = input()
            summ = exchange_rates[operation_type][currency_input] * int(mdl)
            print(f'You got mdl {summ} if you {operation_type} {currency_input}')
        else:
            print('Enter correct currency type')
            curs()
    else:
        print('Enter correct operation type')
        curs()

if __name__ == '__main__':
    curs()