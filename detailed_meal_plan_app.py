# Streamlit Weekly Meal Plan App with Dynamic Images
import streamlit as st
import random
import requests

# Your Amazon affiliate code
affiliate_code = "gfm0dd-20"  

# Using Unsplash API to fetch images
def get_image_url(query):
    endpoint = "https://api.unsplash.com/search/photos"
    headers = {
        "Authorization": "Client-ID y7sY9svzrBEGTMLfN4mFwjjoP_aP11y7lZcLqH7Ml-Q"
    }
    params = {
        "query": query,
        "per_page": 1
    }
    response = requests.get(endpoint, headers=headers, params=params)
    data = response.json()
    if data['results']:
        return data['results'][0]['urls']['small']

# Sample structure of meals
meals = {
    "Meal 1": {
        "instructions": ["Step 1", "Step 2"],
        "ingredients": ["ingredient 1", "ingredient 2"]
    },
    # ... (Repeat the structure for 1000 meals)
}

def generate_amazon_link(ingredient, affiliate_code):
    """Generate a direct Amazon link for a given ingredient with the affiliate code."""
    base_url = f"https://www.amazon.com/s?k={ingredient.replace(' ', '+')}&tag={affiliate_code}"
    return base_url

st.title('Detailed Weekly Meal Plan for Child')
st.write("Please specify any ingredients you'd like to avoid due to allergies:")

# User input for allergies
allergy_ingredients = st.text_input("Ingredients to avoid (comma separated)").split(',')

# Filter out meals that contain the allergenic ingredients
filtered_meals = {k: v for k, v in meals.items() if not any(ingredient in v["ingredients"] for ingredient in allergy_ingredients)}

if st.button('Generate Meal Plan'):
    all_ingredients = set()
    
    for i in range(7):  # For each day of the week
        st.write(f"### Day {i + 1}")
        
        selected_meals = random.sample(list(filtered_meals.keys()), 2)
        for meal in selected_meals:
            st.write(f"**Meal: {meal}**")
            
            # Fetch image from Unsplash
            image_url = get_image_url(meal)
            if image_url:
                st.image(image_url, caption=meal, use_column_width=True)
            
            for instruction in meals[meal]['instructions']:
                st.write(instruction)
            
            st.write("Ingredients:")
            for ingredient in meals[meal]['ingredients']:
                st.markdown(f"[{ingredient}]({generate_amazon_link(ingredient, affiliate_code)})")
            
            all_ingredients.update(meals[meal]['ingredients'])
            st.write("\n")
        
        # ... (Similar structure for snacks)
        
    st.write("### Amazon links to buy ingredients:")
    for ingredient in all_ingredients:
        st.write(f"{ingredient}: {generate_amazon_link(ingredient, affiliate_code)}")

st.write("Note: Please ensure the suitability of each ingredient for the child's dietary needs before purchasing.")
