# INFLUENCE MARKETING RECOMMENDER 
=========================================

![alt text](influence_marketing_lib\utils\logo.png)

We have created a recommender to connect brands with influencers for marketing campaigns. The variables that we are using are 'user_Name, 'followers', 'user_Description', 'likes', 'post_Description', 'location', 'hashtags', 'post_Url',	'engagement_rate', 'hashtags_translated', 'all_descriptions', 'translated'and 'max_category'. 

We are using two dataset obtained by data scrapping, one for brands and one for influencers. After combining and obtaining the relationships between the two datasets, we obtain a dataset with more than 200 000 rows.

We are starting off with a trained data relating all items and all users gathered with data scrapping, we need a big dataset so that predictions can be made from the start. If the company is already in the dataset an influencer will be directly recommended, in the case the company is not in the database a new row with the company a randomly chosen influencer, to grow the dataset. With each interaction the company (the user) does in the framework (click, add to campaign, collaboration), new rows will be added.

We are giving a punctuation to the cohesion between the company marketing campaing and the influencer user, ubication and content. In this case we are giving 5 per ubication, 10 per category and 1 per each coinciding hashtag. At the end we sum the engagement rate to this punctuation to retrieve the rating.

Furthermore, a new system were points will be calculated through the interaction of users with the app. These include colaborations, clicks, check info, campaigns...

We are using two algorithms:
- LightFM is a Python implementation of a hybrid recommendation algorithms for both implicit and explicit feedbacks. It is a hybrid content-collaborative model which represents users and items as linear combinations of their content features’ latent factors. The model learns embeddings or latent representations of the users and items in such a way that it encodes user preferences over items. These representations produce scores for every item for a given user; items scored highly are more likely to be interesting to the user.

- LightGBM is a gradient boosting framework that uses tree based learning algorithms. It has the following characteristics: Faster training speed and higher efficiency, Lower memory usage, Better accuracy, Support of parallel, distributed, and GPU learning, and Capable of handling large-scale data.
