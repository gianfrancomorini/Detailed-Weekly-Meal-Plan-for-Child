# Streamlit Weekly Meal Plan App with Detailed Meals and Snacks
import streamlit as st
import random

# Sample meals, snacks, their preparation instructions, and ingredients
meals = {
    "Spaghetti with Marinara Sauce": {
        "instructions": "Boil spaghetti until al dente. Heat marinara sauce in a pan and mix with spaghetti. Serve with parmesan cheese on top.",
        "ingredients": ["spaghetti", "marinara sauce", "parmesan cheese"]
    },
    "Grilled Cheese Sandwich": {
        "instructions": "Butter one side of each bread slice. Place cheese between slices, buttered side out. Grill on a skillet until golden brown on each side and cheese is melted.",
        "ingredients": ["bread", "butter", "cheddar cheese"]
    },
    "Chicken Nuggets with Mashed Potatoes": {
        "instructions": "Bake chicken nuggets as per package instructions. Boil potatoes until soft, mash with butter and milk. Serve together.",
        "ingredients": ["chicken nuggets", "potatoes", "butter", "milk"]
    },
    # ... [Keep the other meals as they are, but ensure no duplicates]
    "Chicken Soup": {
        "ingredients": ["chicken", "carrots", "onions", "celery", "noodles", "chicken broth"],
        "instructions": ["Cook chicken in broth until done. Remove and shred.", "Add diced veggies to the broth. Once tender, add noodles.", "Once noodles are cooked, add shredded chicken back to the pot."],
    },
    "Pancakes": {
        "ingredients": ["pancake mix", "water", "syrup", "butter"],
        "instructions": ["Mix pancake mix with water.", "Pour batter onto a hot skillet and cook until bubbles form. Flip and cook the other side.", "Serve with syrup and butter."]
    }
    # Note: This is not the complete list, just a snippet for the sake of demonstration.
}

# Streamlit UI
st.title("Weekly Meal Plan")

if st.button("Generate Meal Plan"):
    sample_meals = random.sample(list(meals.keys()), 7)  # Select 7 random meals for a week
    for day, meal in enumerate(sample_meals, 1):
        st.subheader(f"Day {day}: {meal}")
        st.write("Ingredients:", ", ".join(meals[meal]['ingredients']))
        st.write("Instructions:", meals[meal]['instructions'])

st.write("Note: Click the button to generate a new meal plan for the week.")
