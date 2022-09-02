import urllib.request
import json
from datetime import date

def getData(url):
    r  = urllib.request.urlopen(url)
    html = r.read()
    html = html.decode()
    data = json.loads(html)
    return data

today = date.today()
month = today.month
day = today.day

Numbers = []
for i in range(1,81):
    Numbers.append([i,0])

winningtemp = 0
for day in range(1,day+1):
    month = str(month).zfill(2)
    day =  str(day).zfill(2)
    date = str(today.year)+'-'+month+'-'+day

    url = 'https://api.opap.gr/draws/v3.0/1100/draw-date/{}/{}/draw-id'.format(date,date)
    data = getData(url)
    myDraw = data[0]
    winningtemp += 20
    url = 'https://api.opap.gr/draws/v3.0/1100/{}'.format(myDraw)
    data = getData(url)

    winningNumbers = data['winningNumbers']['list']
    print('**********Για την:',date,'οι πρώτες κληρώσεις έχουν ως εξής:**********\n')
    for k in winningNumbers:
        Numbers[k-1][1] += 1
    for i in range(1,81):
        print('*Ο αριθμός', i, 'έχει ποσοστό εμφάνισης:', Numbers[i-1][1]/winningtemp*100, '% έως τώρα.\n')
