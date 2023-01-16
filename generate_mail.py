import pandas as pd
from IPython.display import HTML, display
from datetime import datetime, timedelta
#--------
from functions import saveFile
#--------

def genarateMailText(mode = 'normal'):

    #change of prices
    dfChange = pd.read_csv('price_drop.csv')

    todayPriceChange = dfChange.loc[dfChange['date'] == datetime.today().strftime('%Y-%m-%d')]
    todayPriceChange.reset_index(drop=True, inplace=True)
    todayPriceChange.drop('date', axis=1, inplace=True)

    if len(todayPriceChange['link'] != 0):
        number = len(todayPriceChange['link'])
        priceChangeMail = f'<center><h2>Price changes: </h2></center><br> ' + todayPriceChange.to_html(index = False) + '<br>'
    else:
        priceChangeMail = '<center><h2>No price changes</h2></center><br> '

    #new ads
    dfNew = pd.read_csv('new_ads.csv')
    todayNew = dfNew.loc[dfNew['date'] == datetime.today().strftime('%Y-%m-%d')]
    todayNew.reset_index(drop=True, inplace=True)
    todayNew.drop('date', axis=1, inplace=True)

    if (len(todayNew['link']) != 0):
        number = len(todayNew['link'])
        newMail = f'<center><h2>New ads: </h2></center><br> ' + todayNew.to_html(index = False) + '<br>'
    else:
        newMail = '<center><h2>No new ads</h2></center><br>'

    #reactivated ads
    dfReactivated = pd.read_csv('reactivated_ads.csv')
    todayReactivated = dfReactivated.loc[dfReactivated['date'] == datetime.today().strftime('%Y-%m-%d')]
    todayReactivated.reset_index(drop=True, inplace=True)
    todayReactivated.drop('date', axis=1, inplace=True)

    if (len(todayReactivated['link']) != 0):
        number = len(todayReactivated['link'])
        reactivatedMail = f'<center><h2>Reactivated ads: </h2></center><br> ' + todayReactivated.to_html(index = False) + '<br>'
    else:
        reactivatedMail = '<center><h2>No reactivated ads</h2></center><br>'
    
    #deleted ads
    dfDeleted = pd.read_csv('deleted_ads.csv')
    todayDeleted = dfDeleted.loc[dfDeleted['date'] == datetime.today().strftime('%Y-%m-%d')]
    todayDeleted.reset_index(drop=True, inplace=True)
    todayDeleted.drop('date', axis=1, inplace=True)

    if (len(todayDeleted['link']) != 0):
        number = len(todayDeleted['link'])
        deletedMail = f'<center><h2>Deleted ads: </h2></center><br> ' + todayDeleted.to_html(index = False) + '<br>'
    else:
        deletedMail = '<center><h2>No deleted ads</h2></center><br>'

    data = datetime.today().strftime('%Y-%m-%d')
    #concating result of each block to email text
    textMail = f'''<center><h1>Otodom - {data}</h1></center>
    <hr width="90%" color="grey" size="1px" <br>
    {priceChangeMail}
    <hr width="90%" color="grey" size="1px" <br>
    {newMail}
    <hr width="90%" color="grey" size="1px" <br>
    {reactivatedMail}
    <hr width="90%" color="grey" size="1px" <br>
    {deletedMail}
    '''
    mailDf = pd.DataFrame([[textMail, datetime.today().strftime('%Y-%m-%d')]], columns = ['text', 'date'])

    if mode == 'test':
        return mailDf
    else:
        saveFile(mailDf, 'mail_content.csv')
