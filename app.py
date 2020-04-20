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
    school = request.args['sch']
    if school == 'gen':
        txtColor = '#ccc'
        bknd = '#fff'
        hlight = '#f9a825'
        headIMG = 'https://static.wixstatic.com/media/54af3f_ef2e9753337741b7ba8f5f8507255acc~mv2.png/v1/fill/w_320,h_254,al_c,q_85,usm_0.66_1.00_0.01/54af3f_ef2e9753337741b7ba8f5f8507255acc~mv2.webp'
    elif school == 'crh':
        txtColor = '#fff'
        bknd = '#163052'
        hlight = '#7DA7D9'
        headIMG = 'https://www-tc.pbs.org/wgbh/americanexperience/media/filer_public_thumbnails/filer_public/d1/46/d1464710-a056-41ba-a15b-0f2fc5bfa34a/jfk_harvard_800.jpg__800x529_q85_crop_subsampling-2_upscale.jpg'
    elif school == 'da':
        txtColor = '#fff'
        bknd = '#1b5e20'
        hlight = '#00e676'
        headIMG = 'https://d13b2ieg84qqce.cloudfront.net/705b9a8896af4dad10ba668e7b9f8a9363189480.jpg'
    elif school == 'hkiss':
        txtColor = '#fff'
        bknd = '#0D47A1'
        hlight = '#eee'
        headIMG = 'https://www.hotchkiss.org/uploaded/images/Alumni/Alumni_Accomplishments/Banner_Janney77.jpg'
    elif school == 'lville':
        txtColor = '#fff'
        bknd = '#000'
        hlight = '#D50000'
        headIMG = 'https://prabook.com/web/show-photo-icon.jpg?id=13355&width=220&cache=false'
    elif school == 'and':
        txtColor = '#fff'
        bknd = '#0D4741'
        hlight = '#eee'
        headIMG = 'https://i.ytimg.com/vi/OJTq4j2kDdw/maxresdefault.jpg'
    elif school == 'ext':
        txtColor = '#fff'
        bknd = '#000'
        hlight = '#D50000'
        headIMG = 'https://media.nbcbayarea.com/2019/09/Yang_Thumb.jpg?resize=850%2C478'
    return render_template('test.html', txtColor=txtColor, school=school, bknd=bknd, hlight=hlight, headIMG=headIMG)

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
