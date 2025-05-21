# Personalized Recipe Recommendation System for University Students

## Overview

This project is a web-based **recipe recommendation system** designed to help university students overcome information overload and make healthier, budget-friendly meal choices. The platform provides **personalized recipe suggestions** and detailed **nutritional information** based on user-specific data such as dietary restrictions, cuisine preferences, and nutritional goals. The system is built with a Python backend using Flask and leverages machine learning to generate tailored recipe recommendations.

---

## Features

- **Personalized Recommendations:** Suggests recipes based on user-inputted ingredients, preferred cuisine, dietary restrictions, and available cooking time.
- **Nutritional Insights:** Displays comprehensive nutritional information (calories, protein, fats, carbs, etc.) for each recipe.
- **User-Friendly Interface:** Responsive web app built with HTML, CSS (Tailwind), and JavaScript, ensuring accessibility across devices.
- **Data-Driven:** Utilizes a large, diverse recipe dataset, cleaned and processed for accuracy and consistency.
- **Machine Learning Algorithms:** Employs content-based filtering using TF-IDF and K-Nearest Neighbors (KNN) for relevant recipe recommendations.
- **Visualizations:** Includes interactive graphs for user ratings and nutritional breakdowns to aid decision-making.

---

## How It Works

1. **User Input:** Users enter available ingredients, select cuisine type, diet preference, and desired preparation time.
2. **Recommendation Engine:** The backend processes the input using TF-IDF and cosine similarity to find the best-matching recipes.
3. **Results Display:** The top 10 recommended recipes are shown, each with:
   - Recipe name
   - Ingredients (formatted, easy to read)
   - Step-by-step instructions
   - User ratings (visualized)
   - Nutritional information (bar chart and calorie count)
4. **User Experience:** The interface is intuitive and mobile-friendly, making meal planning quick and easy.

---

## Technologies Used

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS (Tailwind), JavaScript
- **Machine Learning:** TF-IDF, KNN, Cosine Similarity (scikit-learn)
- **Data Processing:** Pandas, OpenRefine, NLTK
- **Visualization:** Matplotlib/Plotly (for graphs)

---

## Data Processing and Modeling

- **Data Collection:** Recipes were scraped from diverse sources and merged from Kaggle datasets (originally from Food.com), ensuring a wide variety of cuisines and dietary options.
- **Cleaning:** Null values, duplicates, and inconsistencies were removed. Ingredient and step lists were standardized for clarity.
- **Feature Engineering:** Tags for cuisine, diet, and time were mapped and split into separate columns for easy filtering.
- **Modeling:** 
  - **TF-IDF** quantifies ingredient importance for each recipe.
  - **KNN** and **cosine similarity** identify recipes with similar ingredient profiles.
  - **Ranking:** Recommendations are ordered by historical ratings, recipe complexity, and calorie content.

---

## Visualizations

- **User Ratings Histogram:** Shows the distribution of recipe ratings for quick quality assessment.
- **Nutritional Bar Chart:** Displays percent daily value for key nutrients (carbs, fats, protein, sodium, sugar, total fat) and calorie count.

---

## Getting Started

1. **Clone the repository**
2. **Install dependencies**
