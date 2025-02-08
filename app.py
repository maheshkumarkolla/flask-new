
from flask import Flask, render_template ,jsonify
app = Flask(__name__ )
JOBS=[

    {
    'id':1,
    'title':"Data analyst",
    'location':"Bengaluru, India",
    'salary':"10,00,000"

    },

    {
    'id':2,
    'title':'Data scientist',
    'location':'Delhi, India',
    'salary':'15,00,000'
    },

    {
    'id':3,
    'title':"Frontend engineer",
    'location':"San Francisco, USA",
    

    },
]
@app.route("/")
def hello_world ():
    return render_template("hello.html",jobs=JOBS,company_name="Projects")
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)
if __name__ == "__main__":
 app.run(host='0.0.0.0', debug=True)