import requests
import pandas
import re

headers = {'User-Agent': 'PredictorBot/0.1 (mil4konstant@gmail.com)', 'Accept-Encoding': 'gzip'}
response = requests.get('https://liquipedia.net/dota2/api.php?' + 'action=parse&format=json&page=' + 'Players_(all)',
headers=headers)

if __name__ == '__main__':
    regular = r'<tr>(?!<th.*?>)(.+?)(?!</th>)</tr>'
    players = re.findall(regular, response.json()['parse']['text']['*'])
    positions = []
    for player in players:
        regular = r'<td.*?>(.+?)</td>'
        info = re.findall(regular, player)
        regular = r'(?<=href="/dota2/Category:)\w+'
        country = re.findall(regular, info[0])
        id = info[1]
        regular = r'<span class="team-template-text"><a.*?>(.+?)</a></span>'
        team = re.findall(regular, info[2])
        position = 'q'
        if len(team) != 0:
            team = team[0]
            regular = r'</span> \((.*?)\)'
            position = re.findall(regular, info[2])[0]
        else:
            team = 'Without team'
            position = info[2]
        
        conds = {"(": "", " ": "", ")": ""}
        conds = dict((re.escape(k), v) for k, v in conds.items())
        pn = re.compile("|".join(conds.keys()))
        position = pn.sub(lambda m: conds[re.escape(m.group(0))], position)
        if position not in positions:
            positions.append(position)
            
        regular = r'(?<=href=")\w+'
        links = re.findall(regular, info[3])
    print(positions)
    with open('C:/Users/mil4k/Projects/LiquipediaAPI/test.txt', 'w', encoding='utf-8') as outfile:
        outfile.write(response.json()['parse']['text']['*'])
    
    # print(players)
