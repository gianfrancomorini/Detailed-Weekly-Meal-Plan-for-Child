import streamlit as st
import random

# Predefined meals and ingredients (example data)
meals = {
    'Mac & Cheese': ['macaroni', 'cheese', 'milk', 'butter'],
    'Chicken Nuggets': ['chicken', 'breadcrumbs', 'eggs'],
    'Spaghetti Bolognese': ['spaghetti', 'ground beef', 'tomato sauce', 'onion', 'garlic'],
    'Grilled Cheese Sandwich': ['bread', 'cheese', 'butter'],
    'Veggie Pizza': ['pizza dough', 'tomato sauce', 'cheese', 'bell peppers', 'mushrooms'],
}

# Allergens to be excluded
allergens = {
    'Dairy': ['cheese', 'milk', 'butter'],
    'Gluten': ['macaroni', 'breadcrumbs', 'spaghetti', 'bread', 'pizza dough'],
    'Eggs': ['eggs'],
}

# Helper function to filter meals based on allergens
def filter_meals(allergens_to_exclude):
    filtered_meals = {}
    for meal, ingredients in meals.items():
        if not any(allergen in ingredients for allergen in allergens_to_exclude):
            filtered_meals[meal] = ingredients
    return filtered_meals

# Helper function to create Amazon links
def create_amazon_links(ingredients):
    amazon_base_url = "https://www.amazon.com/s?k={}&tag=YOUR_AFFILIATE_TAG"
    return {ingredient: amazon_base_url.format(ingredient.replace(' ', '+')) for ingredient in ingredients}

# Streamlit UI
st.title("Weekly Meal Planner for Kids")

# Select allergens to exclude
allergens_selected = st.multiselect("Select allergens to filter out:", list(allergens.keys()))

# Aggregating selected allergens
allergens_to_exclude = []
for allergen in allergens_selected:
    allergens_to_exclude.extend(allergens[allergen])

if st.button('Generate Meal Plan'):
    # Filter meals based on selected allergens
    available_meals = filter_meals(allergens_to_exclude)

    # Randomly select a meal for each day of the week
    weekly_meal_plan = random.sample(list(available_meals.keys()), 7)

    # Display the meal plan
    st.subheader("Your Weekly Meal Plan:")
    for day, meal in zip(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], weekly_meal_plan):
        st.markdown(f"**{day}:** {meal}")

    # Display Amazon links for ingredients
    st.subheader("Buy Ingredients:")
    all_ingredients = set(sum([available_meals[meal] for meal in weekly_meal_plan], []))
    amazon_links = create_amazon_links(all_ingredients)
    for ingredient in all_ingredients:
        st.markdown(f"[{ingredient}]({amazon_links[ingredient]})")

# Run the following command in your terminal to install streamlit if you haven't already:
# pip install streamlit

# To run the app, save this script as `meal_planner_app.py` and run the command:
# streamlit run meal_planner_app.py
