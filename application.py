from flask import Flask, render_template, request, flash



app = Flask(__name__)
app.secret_key = 'YOURKEY!'
currentSessionData = []



@app.route('/')
def home():
    return render_template('calculator.html')


@app.route('/calculate', methods=['POST'])
def calculate():

    # GETTING USER DATA

    var1 = request.form.get("var1", type=int)
    var2 = request.form.get("var2", type=int)
    operation = request.form.get("operation")

    if var1 == ' ':
        flash('Must submit a variable 1', category='error')

    if var2 == ' ':
        flash('Must submit a variable 2', category='error')

    # CALCULATING

    if(operation == 'Addition'):
        sign = '+'
        result = var1 + var2
    elif(operation == 'Subtraction'):
        sign = '-'
        result = var1 - var2
    elif(operation == 'Multiplication'):
        sign = 'x'
        result = var1 * var2
    elif(operation == 'Division'):
        sign = '/'
        result = var1 / var2
    else:
        result = 'INVALID CHOICE'


    # STORING SESSION DATA

    wholeOperation = str(var1) + ' ' + str(sign) + ' ' + str(var2) + ' = ' + str(result)
    currentSessionData.append(wholeOperation)
    

    return render_template('calculate.html', result=result, sign=sign, operation=operation, var1=var1, var2=var2)


@app.route("/history")
def history():
    
    return render_template('history.html', currentSessionData=currentSessionData)









if __name__=="__main__":
    app.run()
