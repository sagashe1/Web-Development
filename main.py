from flask import Flask,render_template  # library for creating web page
app = Flask(__name__)  # Created Flask app
# print(__name__) # when we run code on python, the __name__ is given __main__
JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$150,000'
  }
]
@app.route('/') # we can give the link of the URL 
def hello_world():
  return render_template('home.html',
                         jobs=JOBS, 
                        company_name='Entice Careers')
if __name__ == "__main__":
  print("Inside if")
  app.run(host='0.0.0.0',debug = True)
