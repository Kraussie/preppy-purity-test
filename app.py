import dataset
from flask import Flask, render_template, request, url_for, request
from utils import *
from flask.logging import default_handler

app = Flask(__name__)
app.logger.info('Flask Initialized')

#database initialization
db = dataset.connect('sqlite:///index.db')
table = db['resp_table']
app.logger.info('Database Initialized')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    #pull school arguments from URL
    school = request.args['sch']

    if school == 'crh':
        bknd = '#163052'
        hlight = '#aec9eb'
        headIMG = "/static/imgs/crh_test.jpg"
        schNM = 'Choate Rosemary Hall | Purity Test'
    elif school == 'da':
        bknd = '#1b5e20'
        hlight = '#00e676'
        headIMG = '/static/imgs/da.jpg'
        schNM = 'Deerfield Academy | Purity Test'
    elif school == 'hkiss':
        bknd = '#163052'
        hlight = '#7DA7D9'
        headIMG = '/static/imgs/hkiss.jpg'
        schNM = 'Hotchkiss School | Purity Test'
    elif school == 'lville':
        bknd = '#000'
        hlight = '#D50000'
        headIMG = '/static/imgs/lville.jpg'
        schNM = 'Lawrenceville School | Purity Test'
    elif school == 'and':
        bknd = '#163052'
        hlight = '#7DA7D9'
        headIMG = '/static/imgs/and.jpg'
        schNM = 'Phillips Academy Andover | Purity Test'
    elif school == 'ext':
        bknd = '#000'
        hlight = '#D50000'
        headIMG = '/static/imgs/ext_test.jpg'
        schNM = 'Phillips Academy Exeter | Purity Test'
    elif school == 'sa':
        bknd = '#000'
        hlight = '#F55F20'
        headIMG = '/static/imgs/sa_test.jpg'
        schNM = 'Suffield Academy | Purity Test'
    elif school == 'mdsx':
        bknd = '#000'
        hlight = '#D50000'
        headIMG = '/static/imgs/mdsx.png'
        schNM = 'Middlesex Academy | Purity Test'
    elif school == 'ewlk':
        bknd = '#481d6c'
        hlight = '#fff'
        headIMG = '/static/imgs/ewlk.png'
        schNM = 'Ethel Walker School | Purity Test'
    elif school == 'brkshr':
        bknd = '#1b5e20'
        hlight = '#00e676'
        headIMG = '/static/imgs/brkshr.jpg'
        schNM = 'Berkshire School | Purity Test'
    elif school == 'wstmn':
        bknd = '#000'
        hlight = '#ccc'
        headIMG = '/static/imgs/wstmn.jpg'
        schNM = 'Westminster School | Purity Test'
    elif school == 'ko':
        bknd = '#000'
        hlight = '#D50000'
        headIMG = '/static/imgs/ko.jpg'
        schNM = 'Kingswood Oxford School | Purity Test'
    elif school == 'avon':
        bknd = '#000'
        hlight = '#D50000'
        headIMG = '/static/imgs/avon.jpg'
        schNM = 'Avon Old Farms School | Purity Test'
    elif school == 'spal':
        bknd = '#000'
        hlight = '#D50000'
        headIMG = '/static/imgs/spal.jpg'
        schNM = 'St. Paul\'s School | Purity Test'
    elif school == 'mltn':
        bknd = '#163052'
        hlight = '#7DA7D9'
        headIMG = '/static/imgs/mltn.jpg'
        schNM = 'Milton Academy | Purity Test'
    elif school == 'wlstn':
        bknd = '#163052'
        hlight = '#7DA7D9'
        headIMG = '/static/imgs/wlstn.jpg'
        schNM = 'Williston Academy | Purity Test'
    elif school == 'grtn':
        bknd = '#000'
        hlight = '#D50000'
        headIMG = '/static/imgs/grtn.jpg'
        schNM = 'Groton School | Purity Test'
    elif school == 'knt':
        bknd = '#163052'
        hlight = '#fff'
        headIMG = '/static/imgs/knt.jpg'
        schNM = 'Kent School | Purity Test'
    elif school == 'gen':
        bknd = '#163052'
        hlight = '#fff'
        headIMG = '/static/imgs/gen.jpg'
        schNM = 'Preppy Purity Test'
    
    return render_template('test.html', school=school, bknd=bknd, hlight=hlight, headIMG=headIMG, schNM=schNM)

@app.route('/stats')
def stats():
    return render_template('stats.html')

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        dbTrans = {}
        
        #add user data to list
        dbTrans.update({
            'date' : request.form.get('date'),
            'time' : request.form.get('time'),
            'ipAdd' : request.form.get('ipAdd'),
            'school' : request.form.get('school'),
            'totalScore' : request.form.get('totalScore')
        })

        #add individual data to list
        for i in range(1,101):
            indScore = request.form.get('Q'+ str(i))
            dbTrans.update({'Q' + str(i) : indScore})
        
        #add user data to list
        dbTrans.update({
            'country' : request.form.get('country'),
            'region' : request.form.get('region'),
            'city' : request.form.get('city'),
            'zipcode' : request.form.get('zipcode'),
            'lat' : request.form.get('lat'),
            'lon' : request.form.get('lon'),
        })
        
        #save data to database
        table.insert(dbTrans)

        #log confirmation
        app.logger.info(color.BLUE + '[' + request.form.get('ipAdd') + ' >> ' + request.form.get('page') + ']' + color.END + ' Data Received ' + color.YELLOW + '(' + request.form.get('city') + ', ' + request.form.get('region') + ', ' + request.form.get('country') + ')' + color.END)
        
        return 'yes'
    elif request.method == 'GET':
        return 'not working yet'

@app.route('/load', methods=['POST'])
def load():
    #log post about page load
    app.logger.info(color.BLUE + '[' + request.form.get('page') + ' >> ' + request.form.get('ipAdd') + ']' + color.END + ' Rendered ' + color.YELLOW + '(' + request.form.get('city') + ', ' + request.form.get('region') + ', ' + request.form.get('country') + ')' + color.END)
    return 'yes'