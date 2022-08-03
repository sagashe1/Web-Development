from flask import Flask  # library for creating web page
app = Flask(__name__)  # Created Flask app
print(__name__) # when we run code on python, the __name__ is given __main__
@app.route('/') # we can give the link of the URL 
def hello_world():
  return "Hello World!!"
if __name__ == "__main__":
  print("Inside if")
