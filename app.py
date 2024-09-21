from flask import Flask

app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    return "Hello, World! Welcome to GitHub Actions."

# Ensure the app runs when executed
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  
