# NLP
=========================================

This directory contains the processes we used to extract several feature from the dataset using NLP. For the first approach we extracted locations from texts using NER(Named entity recognition). This was used to fill some of the nan values we had in the post_location column. For the second approach to extract categories we created a dictionary, where matches between the words in each category and both user and post description. The category with more matches will be chosen and added in a new column max_categories.