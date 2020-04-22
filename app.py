import dataset, logging
from flask import Flask, render_template, request, url_for

#create log file
LOG_FILENAME = '/var/log/app.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
#create console handler and set level to debug
ch = logging.StremHandler()
ch.setLevel(logging.DEBUG)
#create formatter + add to ch
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
#create modules loggers
indexLog = logging.getLogger('index.html')
testLog = logging.getLogger('test.html')
indexLog.addHandler(ch)
testLog.addHandler(ch)

#database initialization
db = dataset.connect('sqlite:///index.db')
table = db['resp_table']

app = Flask(__name__)

@app.route('/')
def index():
    indexLog.info('RENDERED')
    return render_template('index.html')

@app.route('/test')
def test():
    testLog.info('RENDERED')
    school = request.args['sch']
    if school == 'gen':
        bknd = '#163052'
        hlight = '#f9a825'
        headIMG = 'https://www.gradshop.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/h/s/hs-mt-044_0_4_3.jpg'
    elif school == 'crh':
        bknd = '#163052'
        hlight = '#7DA7D9'
        headIMG = 'https://www-tc.pbs.org/wgbh/americanexperience/media/filer_public_thumbnails/filer_public/d1/46/d1464710-a056-41ba-a15b-0f2fc5bfa34a/jfk_harvard_800.jpg__800x529_q85_crop_subsampling-2_upscale.jpg'
    elif school == 'da':
        bknd = '#1b5e20'
        hlight = '#00e676'
        headIMG = 'https://d13b2ieg84qqce.cloudfront.net/705b9a8896af4dad10ba668e7b9f8a9363189480.jpg'
    elif school == 'hkiss':
        bknd = '#0D47A1'
        hlight = '#eee'
        headIMG = 'https://www.hotchkiss.org/uploaded/images/Alumni/Alumni_Accomplishments/Banner_Janney77.jpg'
    elif school == 'lville':
        bknd = '#000'
        hlight = '#D50000'
        headIMG = 'https://prabook.com/web/show-photo-icon.jpg?id=13355&width=220&cache=false'
    elif school == 'and':
        bknd = '#0D4741'
        hlight = '#eee'
        headIMG = 'https://i.ytimg.com/vi/OJTq4j2kDdw/maxresdefault.jpg'
    elif school == 'ext':
        bknd = '#000'
        hlight = '#D50000'
        headIMG = 'https://media.nbcbayarea.com/2019/09/Yang_Thumb.jpg?resize=850%2C478'
    return render_template('test.html', school=school, bknd=bknd, hlight=hlight, headIMG=headIMG)

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
        'school' : request.form.get('school'),
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
