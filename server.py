from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    order_sum = 0
    for el, val in request.form.items():
        if el in ['apple', 'strawberry', 'raspberry', 'blackberry']:
            order_sum += int(val)
    print(f"Charging {request.form['first_name']} {request.form['last_name']} for {order_sum} fruits")
    return render_template("checkout.html", order_sum=order_sum)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    