from app import Flask, render_template, redirect, url_for, request, session


app = Flask(__name__)
app.secret_key = 'secretkey'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST": #role from submission
        role = request.POST.get('role')
        session['role'] = role #store selected role
        return redirect(url_for('home')) #redirect to homepage
    return render_template("index.html")

@app.route('/home')
def home():
    role = session.get('role', 'guest') #default role guest
    if role == 'customer_service':
        return render_template('home_customer_service.html')
    elif role == 'financial_manager':
        return render_template('home_financial_manager.html')
    elif role == 'production_manager':
        return render_template('home_production_manager.html')
    else:
        return render_template('home_default.html') #default view
    
if __name__ == "__main__":
    app.run(debug=True)
