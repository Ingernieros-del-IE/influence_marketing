import pytest
import pandas as pd

@pytest.fixture
def df():
    # Replace the link below with your own shareable link
    file_link = "https://drive.google.com/file/d/1Gb2B3QMujysVqQY1G1OjoS3BhFWCF5gu/view?usp=sharing"
    return pd.read_csv(file_link)

def test_engagementRateSum(df):
    # Here we will test that the engagement rate operation works as it should.
    assert df['user_likes_mean'] > 500

def test_followersLimit(df):
    # Here we are testing that no item (influencer) has less than 10000 followers.
    assert (df['user_followers'] >= 10000).all()
