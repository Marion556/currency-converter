from flask import Flask, request, render_template, redirect, flash
from forex_python.converter import CurrencyRates, CurrencyCodes

app = Flask(__name__)
app.config["SECRET_KEY"] = "Bathtub"

currency_rates = CurrencyRates()
currency_codes = CurrencyCodes()
supported_currency = ['EUR', 'IDR', 'BGN', 'ILS', 'GBP', 'DKK',
               'CAD', 'JPY', 'HUF', 'RON', 
               'MYR', 'SEK', 'SGD', 'HKD', 'AUD',
               'CHF', 'KRW', 'CNY', 'TRY', 'HRK', 'NZD', 
               'THB', 'USD', 'NOK', 'RUB', 'INR', 'MXN', 
               'CZK', 'BRL', 'PLN', 'PHP', 'ZAR']


@app.route("/")
def homepage():
    return render_template("index.html")
       
@app.route("/result", methods=('GET', 'POST'))
def submit_page():
    from_curr = request.form['fromCurr'].upper()  
    to_curr = request.form['toCurr'].upper()  
    amount = int(request.form['amount'])  
    symbol = currency_codes.get_symbol(to_curr)

    if from_curr not in supported_currency:
        flash('Not a valid Code!', 'alert alert-danger')
        return redirect('/')
    elif to_curr not in supported_currency:
        flash('Not a valid Code!', 'alert alert-danger')
        return redirect('/')
    else:
        result = currency_rates.convert(from_curr, to_curr, amount)
        symbol = currency_codes.get_symbol(to_curr)
        flash('Success!', 'alert alert-success')
        return render_template('result.html', from_curr=from_curr, to_curr=to_curr, amount=amount, result=result, symbol=symbol)

    
   


