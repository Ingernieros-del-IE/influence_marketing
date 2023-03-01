# INFLUENCE MARKETING RECOMMENDER 
=========================================

We have created a recommender that recommends influencers for marketing campaigns to companies based on the following variables; Account', 'Link', 'Followers', 'Audience Country','Authentic engagement', 'Category1', 'Hashtags', 'Cost Story', 'Cost Post', 'Name_co', 'Category_co' 'Hashtags_co', 'Country_co','Followers_co', 'Puntos'. 

We are using a dataset with 100000 rows. We have not tested the compatibility with smaller datasets. 

We are giving a punctuation to the cohesion between the company marketing campaing and the influencer personality, ubication and content. e.g. We belive that the ubication of the influencer could be less relevant that the affinity between the product and the type of content, however this could be a factor that could help a company reach more realistic customers.

LightFM is a Python implementation of a hybrid recommendation algorithms for both implicit and explicit feedbacks.

It is a hybrid content-collaborative model which represents users and items as linear combinations of their content features’ latent factors. The model learns embeddings or latent representations of the users and items in such a way that it encodes user preferences over items. These representations produce scores for every item for a given user; items scored highly are more likely to be interesting to the user.
