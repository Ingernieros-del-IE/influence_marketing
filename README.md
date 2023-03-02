# INFLUENCE MARKETING RECOMMENDER 
=========================================

We have created a recommender that recommends influencers for marketing campaigns to companies based on the following variables; Account', 'Link', 'Followers', 'Audience Country','Authentic engagement', 'Category1', 'Hashtags', 'Cost Story', 'Cost Post', 'Name_co', 'Category_co' 'Hashtags_co', 'Country_co','Followers_co', 'Puntos'. 

We are using a dataset with 100000 rows. We have not tested the compatibility with smaller datasets. 

We are starting off with some data relating all items and all users, we need a big dataset so that predictions can be made from the start. If the company is already in the dataset an influencer will be recommended, in the case the company is not in the database we will include a new row with the company and an influencer that we choose randomly.

 At the moment we are giving a punctuation to the cohesion between the company marketing campaing and the influencer personality, ubication and content. In this case we are giving 5 per ubication, 10 per category and 1 per each coinciding hashtag. At the end we sum the engagement rate to this punctuation to retrieve the rating.

We are thinking to introduce a new system were points will be calculated through the interaction of users with the app. These include colaborations, clicks, check info, campaigns...

LightFM is a Python implementation of a hybrid recommendation algorithms for both implicit and explicit feedbacks.

It is a hybrid content-collaborative model which represents users and items as linear combinations of their content features’ latent factors. The model learns embeddings or latent representations of the users and items in such a way that it encodes user preferences over items. These representations produce scores for every item for a given user; items scored highly are more likely to be interesting to the user.
