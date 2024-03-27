from flask import Flask, render_template, request , jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 100
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'saalary': 200
}, {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 300
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': 400
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS , company_name = 'Piku')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
