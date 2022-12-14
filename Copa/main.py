# monitoring the cup matches and
# narrating

import requests
import time
import datetime
import pyttsx3

def getMatchData():
    return requests.get(
        url='https://temporeal.lance.com.br/storage/matches/copa-do-mundo-2022-09-12-2022-croaciaxbrasil.json'
    ).json()

lastUpdate = None

while True:
    matchData = getMatchData()

    narrations = matchData['match']['narrations']
    lastNarrations = matchData[len(narrations) - 1]
    lastNarrationsTime = datetime.strptime(lastNarrations['created_at'], '%Y-%m-%dT%H:%M:%S.000000Z')

    if(not lastUpdate) or (lastNarrationsTime > lastUpdate):
        lastUpdate = lastNarrationsTime
        lastNarrationMoment = narrations[len(narrations) - 1]['moment']
        lastNarrationText = narrations[len(narrations) - 1]['text']
        print(f'.\n.\n{lastNarrationMoment}" - {lastNarrationText}')

    engine = pyttsx3.init()
    # Texto que a engine irá narrar
    engine.say(lastNarrationText)
    # Executando
    engine.runAndWait()

    time.sleep(10)