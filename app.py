from app import app

if __name__ == '__main__':
    app.secret_key = "123456789" 
    app.run(debug=True)