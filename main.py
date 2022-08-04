from flask import Flask,render_template  # library for creating web page
app = Flask(__name__)  # Created Flask app
print(__name__) # when we run code on python, the __name__ is given __main__
@app.route('/') # we can give the link of the URL 
def hello_world():
  return render_template('home.html')
if __name__ == "__main__":
  print("Inside if")
  app.run(host='0.0.0.0',debug = True)
