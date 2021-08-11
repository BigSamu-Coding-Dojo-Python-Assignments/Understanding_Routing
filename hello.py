from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')         
def hello_world():
    return "Hello World!"

@app.route('/say/<name>')         
def hello_person(name):
    return f"Hi {name}!"  

@app.route('/<name>')
def hello_repeat(name):
    print(80*"*")
    print("in the hello person function")
    print(name)
    return f"Hello {name}!"  

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.