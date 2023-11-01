import streamlit as st
import random

# Expanded list of meals and ingredients (example data, expand to 50 meals as needed)
meals = {
    # [First few meals for example, continue this pattern to reach 50 meals]
    'Mac & Cheese': ['macaroni', 'cheese', 'milk', 'butter'],
    'Chicken Nuggets': ['chicken', 'breadcrumbs', 'eggs'],
    'Spaghetti Bolognese': ['spaghetti', 'ground beef', 'tomato sauce', 'onion', 'garlic'],
    'Grilled Cheese Sandwich': ['bread', 'cheese', 'butter'],
    'Veggie Pizza': ['pizza dough', 'tomato sauce', 'cheese', 'bell peppers', 'mushrooms'],
    # ... add more meals here up to the 50th meal
}

# Allergens to be excluded
allergens = {
    'Dairy': ['cheese', 'milk', 'butter', 'yogurt', 'cream'],
    'Gluten': ['macaroni', 'breadcrumbs', 'spaghetti', 'bread', 'pizza dough', 'flour', 'cereal'],
    'Eggs': ['eggs', 'mayonnaise', 'some pastas'],
    'Nuts': ['peanuts', 'almonds', 'cashews', 'nut butters'],
    'Soy': ['soy sauce', 'tofu', 'soy milk', 'edamame'],
    'Seafood': ['fish', 'shrimp', 'lobster', 'crab'],
    # ... add more allergenic ingredients here if needed
}

# Function to filter meals based on allergens
def filter_meals(allergens_to_exclude):
    filtered_meals = {}
    for meal, ingredients in meals.items():
        if not any(allergen in ingredients for allergen in allergens_to_exclude):
            filtered_meals[meal] = ingredients
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
            st.markdown(f"**{day}:** {meal}")

        # Display Amazon links for ingredients
        st.subheader("Buy Ingredients:")
        all_ingredients = set(sum([available_meals[meal] for meal in weekly_meal_plan], []))
        amazon_links = create_amazon_links(all_ingredients, 'gfm0dd-20')
        for ingredient in all_ingredients:
            st.markdown(f"[{ingredient}]({amazon_links[ingredient]})")

# The rest of the app remains unchanged

# Save this script as `meal_planner_app.py` and run it with Streamlit using the following command:
# streamlit run meal_planner_app.py
