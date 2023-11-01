import streamlit as st
import random

# Expanded list of meals and ingredients with cooking instructions
meals = {
    # Example meals with cooking instructions
    'Mac & Cheese': {
        'ingredients': ['macaroni', 'cheese', 'milk', 'butter'],
        'instructions': 'Cook macaroni, mix with cheese, milk, and butter, then bake until golden.'
    },
    'Chicken Nuggets': {
        'ingredients': ['chicken', 'breadcrumbs', 'eggs'],
        'instructions': 'Coat chicken in egg, then breadcrumbs, and bake.'
    },
    # ... other meals listed similarly
}

# Function to filter meals based on allergens
def filter_meals(allergens_to_exclude):
    filtered_meals = {}
    for meal, details in meals.items():
        if not any(allergen in details['ingredients'] for allergen in allergens_to_exclude):
            filtered_meals[meal] = details
    return filtered_meals

# Function to create Amazon links with affiliate tag
def create_amazon_links(ingredients, affiliate_tag):
    amazon_base_url = "https://www.amazon.com/s?k={}&tag="
    return {ingredient: amazon_base_url.format(ingredient.replace(' ', '+')) + affiliate_tag for ingredient in ingredients}

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

    # Check if there are enough meals to generate a plan
    if len(available_meals) < 7:
        st.error("Not enough meals available to generate a full week plan based on selected allergens. Please select fewer restrictions.")
    else:
        # Randomly select a meal for each day of the week
        weekly_meal_plan = random.sample(list(available_meals.keys()), 7)

        # Display the meal plan
        st.subheader("Your Weekly Meal Plan:")
        for day, meal in zip(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], weekly_meal_plan):
            st.markdown(f"**{day}:** {meal} - {available_meals[meal]['instructions']}")

        # Display Amazon links for ingredients
        st.subheader("Buy Ingredients:")
        all_ingredients = set(sum([available_meals[meal]['ingredients'] for meal in weekly_meal_plan], []))
        amazon_links = create_amazon_links(all_ingredients, 'your-affiliate-tag-here')
        for ingredient in all_ingredients:
            st.markdown(f"[{ingredient}]({amazon_links[ingredient]})")
