import pandas as pd 

df = pd.read_csv('../input/beltrnvalle/influencer-data.csv')

print(df.columns)

def engagementRateSumTest(self): # Here we will test that the engagement rate operation works as it should. 
    assert(df['user_likes_mean']) > 500

def followersLimitTest(self): # Here we are testing that no item(influencer) is smaller than 100000 followers. 
    assert len(df['user_followers']) > 10000
