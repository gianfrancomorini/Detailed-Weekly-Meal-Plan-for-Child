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
        "instructions": "Butter one side of each bread slice. Place cheese between bread slices, buttered side out. Grill on a pan until golden brown.",
        "ingredients": ["bread", "cheese", "butter"]
    },
    "Chicken Nuggets with Mashed Potatoes": {
        "instructions": "Bake chicken nuggets as per package instructions. Boil potatoes until soft, mash with butter and milk. Serve together.",
        "ingredients": ["chicken nuggets", "potatoes", "butter", "milk"]
    },
    "Mac and Cheese": {
        "instructions": "Boil macaroni until al dente. In a separate pan, melt butter, add milk and cheese. Mix sauce with macaroni.",
        "ingredients": ["macaroni", "cheddar cheese", "milk", "butter"]
    },
    "Vegetable Stir-fry": {
        "instructions": "Stir-fry broccoli and bell peppers in a pan. Add tofu and soy sauce. Cook until vegetables are tender.",
        "ingredients": ["broccoli", "bell peppers", "soy sauce", "tofu"]
    },
    "Cheese Pizza": {
        "instructions": "Spread tomato sauce on pizza dough. Top with mozzarella cheese. Bake until crust is golden brown.",
        "ingredients": ["pizza dough", "tomato sauce", "mozzarella cheese"]
    }
}

snacks = {
    "Fruit Salad": {
        "instructions": "Dice a variety of fruits and mix them together in a bowl.",
        "ingredients": ["apple", "banana", "orange"]
    },
    "Yogurt with Granola": {
        "instructions": "Pour yogurt into a bowl and top with granola.",
        "ingredients": ["yogurt", "granola"]
    },
    "Peanut Butter & Jelly Sandwich": {
        "instructions": "Spread peanut butter and jelly on bread slices and serve.",
        "ingredients": ["bread", "peanut butter", "jelly"]
    },
    "Cheese Sticks": {
        "instructions": "Take cheese sticks from packaging and serve.",
        "ingredients": ["cheese sticks"]
    }
}

def generate_amazon_link(ingredient, affiliate_code):
    """Generate a direct Amazon link for a given ingredient with the affiliate code."""
    base_url = f"https://www.amazon.com/s?k={ingredient.replace(' ', '+')}&tag={affiliate_code}"
    return base_url

affiliate_code = "gfm0dd-20"  # Your Amazon affiliate code

st.title('Detailed Weekly Meal Plan for Child')

if st.button('Generate Meal Plan'):
    all_ingredients = set()
    for i in range(7):  # For each day of the week
        st.write(f"### Day {i + 1}")
        
        selected_meals = random.sample(list(meals.keys()), 2)
        for meal in selected_meals:
            st.write(f"**Meal: {meal}**")
            st.write(meals[meal]['instructions'])
            all_ingredients.update(meals[meal]['ingredients'])
        
        selected_snacks = random.sample(list(snacks.keys()), 2)
        for snack in selected_snacks:
            st.write(f"**Snack: {snack}**")
            st.write(snacks[snack]['instructions'])
            all_ingredients.update(snacks[snack]['ingredients'])
        
        st.write("\n")

    st.write("### Amazon links to buy ingredients:")
    for ingredient in all_ingredients:
        st.write(f"{ingredient}: {generate_amazon_link(ingredient, affiliate_code)}")

st.write("Note: Please ensure the suitability of each ingredient for the child's dietary needs before purchasing.")
