import dataset
from flask import Flask, render_template, request, url_for

db = dataset.connect('sqlite:///index.db')
table = db['resp_table']

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/stats')
def stats():
    return render_template('stats.html')

@app.route('/data', methods=['POST'])
def update():
    dbTrans = {}
    
    dbTrans.update({
        'date' : request.form.get('date'),
        'time' : request.form.get('time'),
        'ipAdd' : request.form.get('ipAdd'),
        'school' : request.form.get('test'),
        'totalScore' : request.form.get('totalScore')
    })

    for i in range(1,101):
        indScore = request.form.get('Q'+ str(i))
        dbTrans.update({'Q' + str(i) : indScore})
    
    dbTrans.update({
        'country' : request.form.get('country'),
        'region' : request.form.get('region'),
        'city' : request.form.get('city'),
        'zipcode' : request.form.get('zipcode'),
        'lat' : request.form.get('lat'),
        'lon' : request.form.get('lon'),
        'isp' : request.form.get('isp'),
        'org' : request.form.get('org'),
        'as' : request.form.get('as')
    })
    
    table.insert(dbTrans)

    return 'yes'

if __name__ == "__main__":
    app.run(debug=True)
