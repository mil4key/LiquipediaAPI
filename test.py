import requests
import pandas
import re

headers = {'User-Agent': 'PredictorBot/0.1 (mil4konstant@gmail.com)', 'Accept-Encoding': 'gzip'}
response = requests.get('https://liquipedia.net/dota2/api.php?' + 'action=parse&format=json&page=' + 'Players_(all)',
headers=headers)

if __name__ == '__main__':
    pn = r'<tr>(?!<th.*?>)(.+?)(?!</th>)</tr>'
    out = re.findall(pn, response.json()['parse']['text']['*'])
    with open('C:/Users/mil4k/Projects/LiquipediaAPI/test.txt', 'w', encoding='utf-8') as outfile:
        outfile.write(response.json()['parse']['text']['*'])
    
    print(out)
