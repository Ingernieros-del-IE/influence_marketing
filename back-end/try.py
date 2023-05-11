import pandas as pd 

df = pd.read_csv('influencer_brand_df.csv')

print(df.columns)

for col in df.columns:
    df[col] = df[col].astype(str)

# save the modified DataFrame to a new CSV file
df.to_csv('modified_data.csv', index=False)