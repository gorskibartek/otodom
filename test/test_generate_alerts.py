import pandas as pd
from datetime import datetime, timedelta
import unittest
import sys
#----
from generate_df import df_1, df_2, df_3, df_4
#----
sys.path.append('//Users//bartoszgorski//Documents//DEV/otodom_with_test')
from generate_alerts import newAds, reactivatedAds, deletedAds, priceChange



class TestNewAds(unittest.TestCase):
    def test_new_ads1(self):
        res = newAds(df_1(), 'test')
        self.assertEqual(len(res['adId']), 0)
        
    def test_new_ads2(self):
        res = newAds(df_2(), 'test')
        self.assertEqual(len(res['adId']), 1)
        self.assertEqual(res['adId'][0], 62902306)

    def test_new_ads3(self):
        res = newAds(df_3(), 'test')
        self.assertEqual(len(res['adId']), 0)
    
    def test_new_ads4(self):
        res = newAds(df_4(), 'test')
        self.assertEqual(len(res['adId']), 1)
        self.assertEqual(res['adId'][0], 63788024)


class TestReactivatedAds(unittest.TestCase):
    def test_reactivated1(self):
        res = reactivatedAds(df_1(), 'test')
        self.assertEqual(len(res['adId']), 0)
    
    def test_reactivated2(self):
        res = reactivatedAds(df_2(), 'test')
        self.assertEqual(len(res['adId']), 0)

    def test_reactivated3(self):
        res = reactivatedAds(df_3(), 'test')
        self.assertEqual(len(res['adId']), 1)
        self.assertEqual(res['adId'][0], 62902305)

    def test_reactivated4(self):
        res = reactivatedAds(df_4(), 'test')
        self.assertEqual(len(res['adId']), 1)
        self.assertEqual(res['adId'][0], 62902305)

class TestDeletedAds(unittest.TestCase):
    def testDeleted1(self):
        res = deletedAds(df_1(), 'test')
        self.assertEqual(len(res['adId']), 0)
    
    def testDeleted2(self):
        res = deletedAds(df_2(), 'test')
        self.assertEqual(len(res['adId']), 0)

    def testDeleted3(self):
        res = deletedAds(df_3(), 'test')
        self.assertEqual(len(res['adId']), 0)

    def testDeleted4(self):
        res = deletedAds(df_4(), 'test')
        self.assertEqual(len(res['adId']), 1)
        self.assertEqual(res['adId'][0], 63753626)

class TestPriceChange(unittest.TestCase):
    def testPriceChange1(self):
        res = priceChange(df_1(), 'test')
        self.assertEqual(len(res['adId']), 0)
    
    def testPriceChange2(self):
        res = priceChange(df_2(), 'test')
        self.assertEqual(len(res['adId']), 0)

    def testPriceChange3(self):
        res = priceChange(df_3(), 'test')
        self.assertEqual(len(res['adId']), 1)
        self.assertEqual(res['adId'][0], 62902305)
        self.assertEqual(res['newPrice'][0], 590000)

    def testPriceChange4(self):
        res = priceChange(df_4(), 'test')
        self.assertEqual(len(res['adId']), 1)
        self.assertEqual(res['adId'][0], 62902305)
        self.assertEqual(res['newPrice'][0], 500000)

if __name__ == '__main__':
    unittest.main(verbosity=2)




