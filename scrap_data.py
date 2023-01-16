import pandas as pd 
from bs4 import BeautifulSoup
import requests
from requests import get
import json
from datetime import datetime, timedelta
import time
from IPython.display import HTML, display
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import schedule

from functions import saveFile


def pageResponse():
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Safari/605.1.15"}
    #check number of offer pages to check from webpage json
    url = ('https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/pabianice')
    response = requests.get(url, headers)
    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.find('script', id = '__NEXT_DATA__')
    resultJson = json.loads(result.string)
    return [response.status_code, resultJson]

def fetchData(data):
    #initializing lists to create result data frame
    adId = []
    link = []
    price  = []
    pricePerMeter = []
    area = []
    photo = []
    dateCreated = []
    pushedUpAt = []
    isPrivateOwner = []

    #to check if proper number of ads where fetched
    adIdCounter = []
    checkedAdsCounter = 0

    numberOfPages = data['props']['pageProps']['tracking']['listing']['page_count']

    #getting detalis of each ad
    for page in range(1, numberOfPages + 1):
        url = (f'https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/pabianice?page={page}')
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        res = soup.find('script', id = '__NEXT_DATA__')

        data = json.loads(res.string)
        adIdCounter.append(data['props']['pageProps']['tracking']['listing']['result_count'])

        adsToCheck = len(data['props']['pageProps']['data']['searchAds']['items'])
        for ad in range(0, adsToCheck):
            adId.append(data['props']['pageProps']['data']['searchAds']['items'][ad]['id'])
            link.append('https://www.otodom.pl/pl/oferta/'+ data['props']['pageProps']['data']['searchAds']['items'][ad]['slug'])
            price.append(data['props']['pageProps']['data']['searchAds']['items'][ad]['totalPrice']['value'])
            pricePerMeter.append(data['props']['pageProps']['data']['searchAds']['items'][ad]['pricePerSquareMeter']['value'])
            area.append(data['props']['pageProps']['data']['searchAds']['items'][ad]['areaInSquareMeters'])
            dateCreated.append(data['props']['pageProps']['data']['searchAds']['items'][ad]['dateCreated'])
            pushedUpAt.append(data['props']['pageProps']['data']['searchAds']['items'][ad]['pushedUpAt'])
            isPrivateOwner.append(data['props']['pageProps']['data']['searchAds']['items'][ad]['isPrivateOwner'])

            #ads sometimes don't have photo so we have to check it and fetch link to photo only when it is possible
            if len(data['props']['pageProps']['data']['searchAds']['items'][ad]['images']) == 0:
                photo.append('')
            else:
                photo.append(data['props']['pageProps']['data']['searchAds']['items'][ad]['images'][0]['large'])

        
        #2 seconds of pause between changing number of page
        time.sleep(2)
        #create DataFrame from retrived data
        resultDf = pd.DataFrame(list(zip(adId, link, price, pricePerMeter, area, photo, dateCreated, pushedUpAt, isPrivateOwner)),
                                columns = ['adId', 'link', 'price', 'pricePerMeter', 'area', 'photo', 'dateCreated', 'pushedUpAt', 'isPrivateOwner'])

    #add date of script execution
    resultDf['date'] = datetime.today().strftime('%Y-%m-%d')

    saveFile(resultDf, 'otodom.csv')

    #Sometimes adsToCheck is returning wrong number of ads (between 2 to 4 less ads). In order to get proper number of ads
    #we are collecting total number of ads for each ads page (list: adIdCounter). We are returning len of df with all fetched ads 
    #and max value from the list (adIdCounter) to check if these numbers are the same in runner.py 
    return [len(resultDf['adId']), max(adIdCounter)]


