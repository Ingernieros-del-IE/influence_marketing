from flask import Flask, jsonify
import psycopg2
import csv

app = Flask(__name__)

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="Influence_data",
    user="postgres",
    password="2552"
)

# Load data from CSV file into database table
with open('df_api.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    cur = conn.cursor()
    for row in reader:
        cur.execute("INSERT INTO Influence_data (itemID, user_name, user_followers, user_likes_mean, user_links, user_eng_rate, user_hashtags_en, user_category, user_country, brand_name, brand_likes_mean, brand_category, brand_hashtags_en, brand_followers, brand_country, userID, rating) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", row)
    conn.commit()

# Define a route to retrieve all data from the database
@app.route('/data')
def get_data():
    cur = conn.cursor()
    cur.execute("SELECT * FROM Influence_data")
    rows = cur.fetchall()
    data = [{'itemID': row[0], 'user_name': row[1], 'user_followers': row[2], 'user_likes_mean': row[3], 'user_links': row[4], 'user_eng_rate': row[5], 'user_hashtags_en': row[6], 'user_category': row[7], 'user_country': row[8], 'brand_name': row[9], 'brand_likes_mean': row[10], 'brand_category': row[11], 'brand_hashtags_en': row[12], 'brand_followers': row[13], 'brand_country': row[14], 'userID': row[15], 'rating': row[16]} for row in rows]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)