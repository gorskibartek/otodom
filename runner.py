import pandas as pd
#-----
from scrap_data import pageResponse, fetchData
from generate_alerts import priceChange, newAds, reactivatedAds, deletedAds
from generate_mail import genarateMailText
from send_mail import sendMail


def main():

    pageCode = pageResponse()
    fetchResult = fetchData(pageCode[1])

    #protection to fetch proper number of ads. 
    #If fetchResult[0] (len(resultDf['adId']) is not equal to fetchResult[1] (max(adIdCounter)) we need to fetch data untill these numbers will 
    #be equal - all ads will be fetched
    while fetchResult[0] != fetchResult[1]:
        fetchResult = fetchData(pageCode[1])

    #alerts part
    data = pd.read_csv('otodom.csv')
    priceChange(data)
    newAds(data)
    reactivatedAds(data)
    deletedAds(data)

    #prepare and send email
    genarateMailText()
    sendMail()
    


if __name__ == '__main__':
    main()