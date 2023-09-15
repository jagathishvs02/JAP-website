from flask import Flask,render_template,jsonify

app=Flask(__name__)
JOBS =[
  {
    'id': 1,
    'title':'Software Developer',
    'location':'Chennai,India',
    'salary':'Rs.12,00,000'
  },
   {
    'id': 2,
    'title':'Frontend Developer',
    'location':'Bangalore,India',
    'salary':'Rs.10,00,000'
  },
   {
    'id': 3,
    'title':'Backend Developer',
    'location':'Chennai,India',
    'salary':'Rs.12,00,000'  
  },
  {
    'id': 4,
    'title':'Data Scientist',
    'location':'Chennai,India',
    'salary':'Rs.12,00,000'
  },
]
@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__=="__main__":
  app.run(host='0.0.0.0')

  

  
  
  