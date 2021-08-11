from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')         
def hello_world():
    return "Hello World!"

@app.route('/dojo')         
def dojo():
    return "Dojo"

@app.route('/say/<name>')         
def say_name(name):
    if type(name) == str:
        return f"Hi {name}!"  
    else:
        return "string only"

@app.route('/repeat/<number>/<word>')         
def repeat_words(number, word):
    if number.isdigit() and type(word) == str: 
        return f"{word} " * int(number)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def no_response(path):
    return 'Sorry! No response. Try again.'

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.