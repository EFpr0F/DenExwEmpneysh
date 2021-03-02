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

numberList = []
for i in range(1,81):
    numberList.append([i,0])

totalWinningNumbers = 0
for day in range(1,day+1):
    month = '0'*(2-len(str(month)))+str(month)
    day = '0'*(2-len(str(day)))+str(day)
    date = str(today.year)+'-'+month+'-'+day
    print ('\n', date, '\n')
    url = 'https://api.opap.gr/draws/v3.0/1100/draw-date/{}/{}/draw-id'.format(date,date)
    data = getData(url)
    firstDraw = data[0]
    totalWinningNumbers += 20
    url = 'https://api.opap.gr/draws/v3.0/1100/{}'.format(firstDraw)
    data = getData(url)
    winningNumbers = data['winningNumbers']['list']
    for number in winningNumbers:
        numberList[number-1][1] += 1
    for i in range(1,81):
        print('Ο αριθμός', i, 'έχει', numberList[i-1][1], 'εμφανίσεις δηλαδή ποσοστό εμφάνισης:', numberList[i-1][1]/totalWinningNumbers*100, '% μέχρι στιγμής.')
