import pandas as pd
from datetime import datetime, timedelta

#save file with delete of data from current date
def saveFile(data, file):
    oldResult = pd.read_csv(file)
    oldResult = oldResult.loc[oldResult['date'] != datetime.today().strftime('%Y-%m-%d')]
    resultAll = pd.concat([oldResult, data])
    resultAll.to_csv(file, index = False)
