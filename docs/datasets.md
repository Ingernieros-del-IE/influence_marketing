# Datasets for the influence marketing recommender

For this project, we have used data from [Instagram](https://www.instagram.com/). Data has been gathered with our own data scrapper from random profiles. However, due to Instagram's policies, we have had to automate the creation of new accounts, encountering numerous problems that have lead us to obtaining less data than expected. The objective of the datasets is to increase when new clients create an account.

There are 2 datasets:

**1. Posts**: Contains 38209 rows (one for each post) with the variables user_id, user_name, followers, user_description, post_id, post_url, likes, post_description and post_location.

**2. Brands**: Contains social media data about 38202 companies or brands. It also contains the variables user_id, user_name, followers, user_description, post_id, post_url, likes, post_description and post_location.


Both datasets will be reduced to get a row per profile (influencer or brand), by calculating Engagement Rate and obtaining categories. Then, both datasets will be combined to get a matrix between both influencers and brands, and calculating the points of that relationship.

To increase the dataset, when a new company starts a campaign, it is asked to select an "ideal" influencer for that campaign. This relation brand-influencer is then added to the dataset after calculating the points of the relationship.