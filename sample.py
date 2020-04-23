import requests, random, progressbar

for i in progressbar.progressbar(range(350)):
    sendData = {
        'date': '4-22-2020',
        'time': '22:33:20',
        'school': 'gen',
        'page': 'index.db',
        'ipAdd': '38.126.101.128',
        'country': 'United States',
        'region': 'Connecticut',
        'city': 'New Haven',
        'zipcode': '06511',
        'lat': '41.3186',
        'lon': '-72.9302'
    }

    questionList = []
    count = 0
    for i in range(1,101):
        value = random.randint(0,1)
        sendData['Q' + str(i)] = str(value)
        if value == 1:
            count += 1
        sendData['totalScore'] = 100 - count

    requests.post('http://127.0.0.1:5000/data', data = sendData)