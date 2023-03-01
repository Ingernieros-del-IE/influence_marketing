import pandas as pd 

df = pd.read_csv('/Users/beltran/Desktop/recoData')

def engagementRateSumTest(self): # Here we will test that the engagement rate operation works as it should. 
    assert(df['Authentic Engagement']/df['Followers'])

def followersLimitTest(self): # Here we are testing that no item(influencer) is smaller than 100000 followers. 
    assert len(df['Followers']) > 10000

def test_dataset(): # We also test for the length of the data.
    assert len(df) == 100000