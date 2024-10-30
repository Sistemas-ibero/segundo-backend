from flask import Flask, render_template, request

app = Flask(__name__)

def login(email, password):
    if email == 'ejemplo@gmail.com' and password == '1234':
        return True
    else:
        print("Usuario o contraseña incorrectos, llegale")
        return False

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/success' , methods=['GET', 'POST'])
def success():
    email = request.form.get('email')
    password = request.form.get('password')
    print(email, password)

    resultado = login(email, password)
    if resultado == False:
        return render_template('index.html')
    else:
        return render_template('success.html')
        

if __name__ == '__main__':
    app.run(debug=True)