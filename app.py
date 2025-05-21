from flask import Flask, render_template, jsonify, request
import pandas as pd
import re
import ast
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tabulate import tabulate
import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__)

# Load the processed recipe dataset
df = pd.read_csv("final_dataset.csv")

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Preprocessing functions
def process_ingredients(ingredients_str):
    ingredients_str = ingredients_str.lower()
    l = ingredients_str.split()
    l = [lemmatizer.lemmatize(item) for item in l]
    l = [item for item in l if item not in stop_words]
    return ' '.join(l)

from sklearn.feature_extraction.text import TfidfVectorizer

# TF-IDF feature extractor
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(df['ingredients_combined'])

diet_type_dict = {
        'Gluten Free' : 'diet_type_gluten_free', 
        'Diary Free': 'diet_type_diary_free',
        'Special Nutrient Food' : 'diet_type_special_nutrient_focus', 
        'Low Carb' : 'diet_type_low_carb',
        'Low Protein' : 'diet_type_low_protein', 
        'Diabetic Friendly' : 'diet_type_diabetic_friendly',
        'Kosher' : 'diet_type_kosher', 
        'High Protein' : 'diet_type_high_protein', 
        'High Fiber' : 'diet_type_high_fiber',
        'Vegetarian' : 'diet_type_vegetarian', 
        'Healthy': 'diet_type_healthy', 
        'Low Calorie' : 'diet_type_low_calorie',
        'Low Fat' : 'diet_type_low_fat', 
        'Low Saturated Fat' : 'diet_type_low_saturated_fat',
        'Low Sodium' : 'diet_type_low_sodium', 
        'Low Cholesterol' : 'diet_type_low_cholesterol', 
        'Vegan' : 'diet_type_vegan',
        'High Calcium' : 'diet_type_high_calcium', 
        'Lactose Free' : 'diet_type_lactose_free',
        'Non Vegetarian' : 'diet_type_non_vegetarian' }

cuisine_dict = {
    'Australian':'cuisine_australian', 
    'Canadian':'cuisine_canadian',
    'European':'cuisine_european', 
    'Chinese' :'cuisine_chinese',
    'Middle Eastern' : 'cuisine_middle_eastern',
    'American':'cuisine_american', 
    'African':'cuisine_african', 
    'Indian':'cuisine_indian',
    'Russian' : 'cuisine_russian', 
    'Asian' : 'cuisine_asian', 
    'Oceanian' : 'cuisine_oceanian',
    'Caribbean/Latin American' : 'cuisine_caribbean_latin_american'
}

# 'No preference','Within 15 minutes','Within 30 minutes','Within 1 hour','Within 2 hours','Within 3 hours','More than 4 hours'

# Get recipes function
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

def get_recipes(input_str, time_to_make, diet_type, cuisine):
    
    if input_str != "":
        input_str = process_ingredients(input_str)
        input_tfidf = tfidf.transform([input_str])
        cosine_similarities = cosine_similarity(input_tfidf, tfidf_matrix)
        all_recipe_indices_sorted = cosine_similarities.argsort()[0][-30:][::-1]
        df_new = df.iloc[all_recipe_indices_sorted]  
        
    elif input_str == "":
        df_new = df.sort_values(by = ['num_rating','n_ingredients'], ascending = [False, True])
    
    ## filtering the results on time to make 
    if time_to_make != "No preference":
        df_new = df_new[df_new['time_to_make'] == time_to_make]
    
    ## filtering the results on diet type
    # if diet_type != "No preference":
    #     col_name1 = diet_type_dict[diet_type]
    #     df_new = df_new[df_new[col_name1] == 1]
    
    ## new 
    if diet_type != ["No preference"]:  # Changed to check against a list containing "No preference"
        for diet in diet_type:
            if diet in diet_type_dict:  # Check if the diet type is in our dictionary
                col_name = diet_type_dict[diet]
                df_new = df_new[df_new[col_name] == 1]
        
    
    ## filtering the results on cuisine
    if cuisine != "No preference":
        col_name2 = cuisine_dict[cuisine]
        df_new = df_new[df_new[col_name2] == 1]
        
    df_new = df_new[['name', 'recipe_id', 'minutes', 'n_steps', 'steps', 'ingredients',
        'n_ingredients', 'cuisine', 'time_to_make', 'minutes_category',
       'steps_category', 'calories', 'total_fat', 'sugar', 'sodium', 'protein',
       'saturated_fat', 'carbohydrates', 'ingredients_combined', 'rating_1',
       'rating_2', 'rating_3', 'rating_4', 'rating_5', 'num_rating']]
    
    top_recipes = df_new.sort_values(by = ['n_ingredients','num_rating','minutes'], ascending = [True, False, True])
    
    if top_recipes.empty:
        return "Sorry! No recipes found, try with only ingredients"
    
    return top_recipes.head(5).to_dict(orient='records')

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/recommendations', methods=['POST'])
def recommendations():
    data = request.json
    input_str = data.get('input_str', '')
    cuisine = data.get('cuisine', 'No preference')
    diet_type = data.get('diet_type', 'No preference')
    time_to_make = data.get('time_to_make', 'No preference')
    recommended_recipes = get_recipes(input_str, time_to_make, diet_type, cuisine)
    return jsonify(recommended_recipes)

if __name__ == '__main__':
    app.run(debug=True)
