import pandas as pd
from datetime import datetime, timedelta
from functions import saveFile



def priceChange(data, mode = 'normal'):

    #initializing lists to create result data frame
    adId = []
    link = []
    area = []
    oldPrice = []
    newPrice = []

    #getting ads which are currently active to check drop changes
    todayAds = data.loc[data['date'] == datetime.today().strftime('%Y-%m-%d')]
    adIdToCheck = todayAds['adId'].unique()

    for i in range(0, len(adIdToCheck)):

        activeAdData = data.loc[data['adId'] == adIdToCheck[i]]
        activeAdData.reset_index(drop=True, inplace=True)

        #check if price changed
        if len(activeAdData['adId']) > 1:
            if activeAdData['price'][len(activeAdData) - 1] < activeAdData['price'][len(activeAdData) - 2]:
                adId.append(activeAdData['adId'][len(activeAdData) - 1])
                link.append(activeAdData['link'][len(activeAdData) - 1])
                area.append(activeAdData['area'][len(activeAdData) - 1])
                oldPrice.append(activeAdData['price'][len(activeAdData) - 2])
                newPrice.append(activeAdData['price'][len(activeAdData) - 1])

    #create DataFrame with ads which price changed        
    priceDropDf = pd.DataFrame(list(zip(adId, link, area, oldPrice, newPrice)),
                                        columns = ['adId','link', 'area', 'oldPrice', 'newPrice'])
    #adding date of price change
    priceDropDf['date'] = datetime.today().strftime('%Y-%m-%d')

    if mode == 'test':
        return priceDropDf
    else:
        saveFile(priceDropDf, 'price_drop.csv')


def newAds(data, mode = 'normal'):

    #initializing lists to create result data frame
    adId = []
    link = []
    area = []
    price = []
    pricePerMeter = []

   

    #getting ads which are currently active to check if it is new ad
    todayAds = data.loc[data['date'] == datetime.today().strftime('%Y-%m-%d')]
    adIdToCheck = todayAds['adId'].unique()

    

    #check all active ads
    for i in range(0, len(adIdToCheck)):
        activeAdData = data.loc[data['adId'] == adIdToCheck[i]]
        activeAdData.reset_index(drop=True, inplace=True)

        #if we have only one row for selected ad it means that it is new ad
        if (len(activeAdData) == 1):
            adId.append(activeAdData['adId'][len(activeAdData) - 1])
            link.append(activeAdData['link'][len(activeAdData) - 1])
            area.append(activeAdData['area'][len(activeAdData) - 1])
            price.append(activeAdData['price'][len(activeAdData) - 1])
            pricePerMeter.append(activeAdData['pricePerMeter'][len(activeAdData) - 1])
    
    #create DataFrame with new ads
    newAdsDf = pd.DataFrame(list(zip(adId, link, area, price, pricePerMeter)),
                                            columns = ['adId','link', 'area', 'price', 'pricePerMeter'])

    newAdsDf['date'] = datetime.today().strftime('%Y-%m-%d')

    if mode == 'test':
        return newAdsDf
    else:
        saveFile(newAdsDf, 'new_ads.csv')

def reactivatedAds(data, mode = 'normal'):
    #if data on input is empty change type of date column to object
    if len(data['adId']) == 0:
        data['date'] = data['date'].astype(str)

    #initializing lists to create result data frame
    adId = []
    link = []
    area = []
    price = []
    pricePerMeter = []
    oldPrice = []
    oldPricePerMeter = []


    #getting ads which were active yesterday to check if any ad was added today
    yesterdayAds = data.loc[data['date'] == (datetime.today() - timedelta(1)).strftime('%Y-%m-%d')]
    yesterdayAds_id = yesterdayAds['adId'].unique()

    #getting ads which are active today 
    todayAds = data.loc[data['date'] == datetime.today().strftime('%Y-%m-%d')]
    todayAds_id = todayAds['adId'].unique()

    #list of new ads
    newAdsIds = list(set(todayAds_id) - set(yesterdayAds_id))

    #list of uniqe ads which were active befeore yesterday
    beforeYesterdayAds = data.loc[data['date'] <= (datetime.today() - timedelta(2)).strftime('%Y-%m-%d')]
    beforeYesterdayAdsIds = beforeYesterdayAds['adId'].unique()

    #comparing each of new ads from today with ads which were active before yesterday
    reactivatedIds = list(set(newAdsIds).intersection(beforeYesterdayAdsIds))

    #getting data for new ads to check if they were active before -> they are reactivated
    for i in range(0, len(reactivatedIds)):
        #getting data from newly added ad
        reactivatedAdsData = todayAds.loc[todayAds['adId'] == reactivatedIds[i]]
        reactivatedAdsData.reset_index(drop=True, inplace=True)

        #getting price of ad at ad expiry date
        reactivatedAdsPreviousData = beforeYesterdayAds.loc[beforeYesterdayAds['adId'] == reactivatedIds[i]]
        reactivatedAdsPreviousData.reset_index(drop=True, inplace=True)
        
        adId.append(reactivatedAdsData['adId'][0])
        link.append(reactivatedAdsData['link'][0])
        area.append(reactivatedAdsData['area'][0])
        price.append(reactivatedAdsData['price'][0])
        pricePerMeter.append(reactivatedAdsData['pricePerMeter'][0])
        oldPrice.append(reactivatedAdsPreviousData['price'][len(reactivatedAdsPreviousData)-1])
        oldPricePerMeter.append(reactivatedAdsPreviousData['pricePerMeter'][len(reactivatedAdsPreviousData)-1])

    #create DataFrame with new ads
    reactivatedAdsDf = pd.DataFrame(list(zip(adId, link, area, price, pricePerMeter, oldPrice, oldPricePerMeter)),
                                            columns = ['adId','link', 'area', 'price', 'pricePerMeter', 'oldPrice', 'oldPricePerMeter'])

    reactivatedAdsDf['date'] = datetime.today().strftime('%Y-%m-%d')

    if mode == 'test':
        return reactivatedAdsDf
    else:
        saveFile(reactivatedAdsDf, 'reactivated_ads.csv')

def deletedAds(data, mode = 'normal'):

    #initializing lists to create result data frame
    adId = []
    link = []
    area = []
    price = []
    pricePerMeter = []


    #getting ads which were active yesterday to check if they were deleted
    yesterdayAds = data.loc[data['date'] == (datetime.today() - timedelta(1)).strftime('%Y-%m-%d')]
    yesterdayAds_id = yesterdayAds['adId'].unique()
    
    #getting ads which are active today to check if any ad was deleted
    todayAds = data.loc[data['date'] == datetime.today().strftime('%Y-%m-%d')]
    todayAds_id = todayAds['adId'].unique()

    #list of deleted ads ids
    deleted_id = list(set(yesterdayAds_id) - set(todayAds_id))

    #getting data for deleted ads based on data from yesterday
    for i in range(0, len(deleted_id)):
        deletedAdData = yesterdayAds.loc[yesterdayAds['adId'] == deleted_id[i]]
        deletedAdData.reset_index(drop=True, inplace=True)

        adId.append(deletedAdData['adId'][0])
        link.append(deletedAdData['link'][0])
        area.append(deletedAdData['area'][0])
        price.append(deletedAdData['price'][0])
        pricePerMeter.append(deletedAdData['pricePerMeter'][0])
    
    #create DataFrame with new ads
    deletedAdsDf = pd.DataFrame(list(zip(adId, link, area, price, pricePerMeter)),
                                            columns = ['adId', 'link', 'area', 'price', 'pricePerMeter'])

    deletedAdsDf['date'] = datetime.today().strftime('%Y-%m-%d')

    if mode == 'test':
        return deletedAdsDf
    else:
        saveFile(deletedAdsDf, 'deleted_ads.csv')
    


