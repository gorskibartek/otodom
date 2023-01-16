import pandas as pd
from datetime import datetime, timedelta


#new_ads - 0, reactivated_ads = 0, deleted_ads = 0, price_change = 0
def df_1():
    data = {
        'adId':
            [],
        'link':
            [],
        'price':
            [],
        'pricePerMeter':
            [],
        'area':
            [],
        'photo':
            [],
        'dateCreated':
            [],
        'pushedUpAt':
            [],
        'isPrivateOwner':
            [],
        'date':
            []
        
    }
    df = pd.DataFrame(data)
    return df

#new ad = 62902306 
#new ads - 1, reactivated_ads = 0, deleted_ads = 0, price_change = 0 
def df_2():

    data = {
        'adId':
            [62902306],
        'link':
            ['https://www.otodom.pl/pl/pod-77-nowoczesne-mieszkanie-nr-11-ID4fWLk'],

        'price':
            [604716],
        'pricePerMeter':
            [9105],
        'area':
            [66.41],
        'photo':
            ['https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6IjFlZDRjdDl3M3VuMTMtQVBMIiwidyI6W3siZm4iOiJlbnZmcXFlMWF5NGsxLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.pviMuE3c8Asf0eoebi3ne9U4mLBJVAQwl6V_YBB-OuA/image;s=1280x1024;q=80'],
        'dateCreated':
            ['2022-12-19 19:00:42'],
        'pushedUpAt':
            ['2022-12-19T19:00:42+01:00'],
        'isPrivateOwner':
            [False],
        'date':
            [datetime.today().strftime('%Y-%m-%d')]
        
    }
    df = pd.DataFrame(data)
    return df

#reactivated ad = 62902305, price_change = 62902305
#new_ads = 0, reactivated_ads = 1, deleted_ads = 0, price_change = 1
def df_3():
    data = {
        'adId':
            [62902305,
            62902305],
        'link':
            ['https://www.otodom.pl/pl/pod-77-nowoczesne-mieszkanie-nr-11-ID4fWLk',
            'https://www.otodom.pl/pl/pod-77-nowoczesne-mieszkanie-nr-11-ID4fWLk'],
        'price':
            [604716,
            590000],
        'pricePerMeter':
            [9105,
            8884],
        'area':
            [66.41,
            66.41],
        'photo':
            ['https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6IjFlZDRjdDl3M3VuMTMtQVBMIiwidyI6W3siZm4iOiJlbnZmcXFlMWF5NGsxLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.pviMuE3c8Asf0eoebi3ne9U4mLBJVAQwl6V_YBB-OuA/image;s=1280x1024;q=80',
            'https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6IjFlZDRjdDl3M3VuMTMtQVBMIiwidyI6W3siZm4iOiJlbnZmcXFlMWF5NGsxLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.pviMuE3c8Asf0eoebi3ne9U4mLBJVAQwl6V_YBB-OuA/image;s=1280x1024;q=80'],
        'dateCreated':
            ['2022-12-19 19:00:42',
            '2022-12-19 19:00:42'],
        'pushedUpAt':
            ['2022-12-19T19:00:42+01:00',
            '2022-12-19T19:00:42+01:00'],
        'isPrivateOwner':
            [False,
            False],
        'date':
            [(datetime.today() - timedelta(3)).strftime('%Y-%m-%d'),
            datetime.today().strftime('%Y-%m-%d')]
    }
    df = pd.DataFrame(data)
    return df




#63753626 - duplicated deleted ad, 62902305 - reactivated ad, 63788024 - new ad
#new_ads = 1, reactivated_ads = 1, deleted_ads = 1
def df_4():
    data = {
    'adId':
        [62902305,
        63753626,
        63753626,
        62902305,
        63788024],
    'link':
        ['https://www.otodom.pl/pl/pod-77-nowoczesne-mieszkanie-nr-11-ID4fWLk',
        'https://www.otodom.pl/pl/super-apartment-w-rewelacyjnej-cenie-pabianice-ID4jwei',
        'https://www.otodom.pl/pl/super-apartment-w-rewelacyjnej-cenie-pabianice-ID4jwei',
        'https://www.otodom.pl/pl/pod-77-nowoczesne-mieszkanie-nr-11-ID4fWLk',
        'https://www.otodom.pl/pl/atrakcyjna-cena-46m2-w-pabianicach-ID4jEb6'],
    'price':
        [604716,
        680000,
        680000,
        500000,
        250000],
    'pricePerMeter':
        [9105,
        7543,
        7543,
        7528,
        5217],
    'area':
        [66.41,
        90.15,
        90.15,
        66.41,
        46.0],
    'photo':
        ['https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6IjFlZDRjdDl3M3VuMTMtQVBMIiwidyI6W3siZm4iOiJlbnZmcXFlMWF5NGsxLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.pviMuE3c8Asf0eoebi3ne9U4mLBJVAQwl6V_YBB-OuA/image;s=1280x1024;q=80',
        'https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6Imtud3Fqbnk3ZmFpYTMtQVBMIiwidyI6W3siZm4iOiJlbnZmcXFlMWF5NGsxLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.C4YYcnoYUpTnokXSnbMgTmqD6sZdqkGbpxQuNkP77Sw/image;s=1280x1024;q=80',
        'https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6Imtud3Fqbnk3ZmFpYTMtQVBMIiwidyI6W3siZm4iOiJlbnZmcXFlMWF5NGsxLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.C4YYcnoYUpTnokXSnbMgTmqD6sZdqkGbpxQuNkP77Sw/image;s=1280x1024;q=80',
        'https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6IjFlZDRjdDl3M3VuMTMtQVBMIiwidyI6W3siZm4iOiJlbnZmcXFlMWF5NGsxLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.pviMuE3c8Asf0eoebi3ne9U4mLBJVAQwl6V_YBB-OuA/image;s=1280x1024;q=80',
        'https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6Ijg3bGlpdTVrY3J0aTItQVBMIiwidyI6W3siZm4iOiJlbnZmcXFlMWF5NGsxLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.6ywjcTAD7EzxvttOoxZweHoHpGwOJdnB2MzfR9w01Co/image;s=1280x1024;q=80'],
    'dateCreated':
        ['2022-12-19 19:00:42',
        '2022-12-19 13:53:09',
        '2022-12-19 13:53:09',
        '2022-12-19 19:00:42',
        '2022-12-19 19:16:51'],
    'pushedUpAt':
        ['2022-12-19T19:00:42+01:00',
        '2022-12-19T13:53:09+01:00',
        '2022-12-19T13:53:09+01:00',
        '2022-12-19T19:00:42+01:00',
        ''],
    'isPrivateOwner':
        [False,
        False,
        False,
        False,
        False],
    'date':
        [(datetime.today() - timedelta(3)).strftime('%Y-%m-%d'),
        (datetime.today() - timedelta(1)).strftime('%Y-%m-%d'),
        (datetime.today() - timedelta(1)).strftime('%Y-%m-%d'),
        datetime.today().strftime('%Y-%m-%d'),
        datetime.today().strftime('%Y-%m-%d')]
    }
    df = pd.DataFrame(data)
    return df


