import streamlit as st
import random

# Define a dictionary of meals with their explanations and ingredients
meals = {
    "Pasta with Tomato Sauce": {
        "explanation": "Boil pasta and top with homemade tomato sauce.",
        "ingredients": ["Pasta", "Tomato sauce", "Parmesan cheese"]
    },
    "Grilled Cheese Sandwich": {
        "explanation": "Grill bread with cheese until golden brown.",
        "ingredients": ["Bread", "Cheese", "Butter"]
    },
    # ... Add more meals as needed
}

# Function to create an Amazon link with a referral tag
def create_amazon_link(ingredient):
    # This is a placeholder for where you'd construct the URL to search for the ingredient on Amazon
    # with your referral tag. Since we can't make web requests, this will be a static example.
    base_url = "https://www.amazon.com/s?k="
    referral_tag = "gfm0dd-20"
    return f"{base_url}{ingredient.replace(' ', '+')}&tag={referral_tag}"

# Function to generate the weekly meal plan
def generate_meal_plan(meals):
    weekly_meal_plan = random.sample(list(meals.items()), 14)
    return weekly_meal_plan

# Streamlit app layout
st.title('Child Weekly Meal Calendar')

if st.button('Generate Meal Plan'):
    meal_plan = generate_meal_plan(meals)
    for day, (meal_name, meal_info) in enumerate(meal_plan, start=1):
        st.subheader(f'Day {day}: {meal_name}')
        st.write(meal_info['explanation'])
        for ingredient in meal_info['ingredients']:
            amazon_link = create_amazon_link(ingredient)
            st.markdown(f"- [{ingredient}]({amazon_link})")

# Run this with `streamlit run your_script.py` in your command line
