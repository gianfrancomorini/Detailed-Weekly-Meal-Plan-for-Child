import streamlit as st
import random

# Define a dictionary of meals with their explanations and ingredients
meals = {
    "Pasta with Tomato Sauce": {
        "explanation": "Boil pasta until al dente, drain, and mix with warmed tomato sauce. Serve with grated Parmesan cheese on top.",
        "ingredients": ["Pasta", "Tomato sauce", "Parmesan cheese"]
    },
    "Grilled Cheese Sandwich": {
        "explanation": "Butter the outside of two slices of bread, place a slice of cheese between them, and grill on a skillet until each side is golden brown.",
        "ingredients": ["Bread", "Cheddar cheese", "Butter"]
    },
    "Chicken Nuggets with Veggies": {
        "explanation": "Bake chicken nuggets according to package instructions and serve with steamed carrots and broccoli.",
        "ingredients": ["Chicken nuggets", "Carrots", "Broccoli"]
    },
    "Tuna Salad": {
        "explanation": "Mix canned tuna with mayonnaise, chopped celery, and a squeeze of lemon. Serve on a bed of lettuce or as a sandwich filling.",
        "ingredients": ["Canned tuna", "Mayonnaise", "Celery", "Lemon", "Lettuce"]
    },
    "Peanut Butter and Jelly Sandwich": {
        "explanation": "Spread peanut butter on one slice of bread and jelly on the other. Press together and cut into halves or quarters.",
        "ingredients": ["Bread", "Peanut butter", "Jelly"]
    },
    "Macaroni and Cheese": {
        "explanation": "Prepare macaroni pasta, mix with cheese sauce until creamy and well combined. Optionally, bake for a crispy top layer.",
        "ingredients": ["Macaroni pasta", "Cheese", "Milk", "Butter"]
    },
    "Scrambled Eggs and Toast": {
        "explanation": "Whisk eggs with salt and pepper, scramble on a skillet until cooked. Serve with buttered toast.",
        "ingredients": ["Eggs", "Salt", "Pepper", "Bread", "Butter"]
    },
    "Ham and Cheese Quesadilla": {
        "explanation": "Place slices of ham and cheese between two tortillas, cook on a skillet until the tortillas are crispy and the cheese is melted.",
        "ingredients": ["Tortillas", "Ham", "Cheddar cheese"]
    },
    "Vegetable Stir Fry": {
        "explanation": "Stir-fry a mix of vegetables such as bell peppers, broccoli, and carrots in a wok with soy sauce and serve over rice.",
        "ingredients": ["Bell peppers", "Broccoli", "Carrots", "Soy sauce", "Rice"]
    },
    "French Toast": {
        "explanation": "Dip slices of bread into a mixture of beaten eggs, milk, and a pinch of cinnamon, then fry until golden brown. Serve with maple syrup.",
        "ingredients": ["Bread", "Eggs", "Milk", "Cinnamon", "Maple syrup"]
    },
    "Fruit Salad": {
        "explanation": "Chop a variety of fruits such as apples, bananas, and grapes and mix them together for a fresh fruit salad.",
        "ingredients": ["Apples", "Bananas", "Grapes"]
    },
    "Beef Tacos": {
        "explanation": "Brown ground beef with taco seasoning, serve in taco shells with shredded lettuce, cheese, and salsa.",
        "ingredients": ["Ground beef", "Taco seasoning", "Taco shells", "Lettuce", "Cheddar cheese", "Salsa"]
    },
    "Baked Fish Sticks": {
        "explanation": "Bake fish sticks according to the package instructions and serve with a side of green beans and tartar sauce.",
        "ingredients": ["Fish sticks", "Green beans", "Tartar sauce"]
    },
    "Homemade Pizza": {
        "explanation": "Top a pizza base with tomato sauce, shredded cheese, and your choice of toppings. Bake until the crust is crispy and the cheese is bubbly.",
        "ingredients": ["Pizza base", "Tomato sauce", "Mozzarella cheese", "Pepperoni"]
    }
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
    weekly_meal_plan = random.sample(list(meals.items()), 14)  # Ensure there are at least 14 meals defined
    schedule = {
        "Monday": weekly_meal_plan[0:2],
        "Tuesday": weekly_meal_plan[2:4],
        "Wednesday": weekly_meal_plan[4:6],
        "Thursday": weekly_meal_plan[6:8],
        "Friday": weekly_meal_plan[8:10],
        "Saturday": weekly_meal_plan[10:12],
        "Sunday": weekly_meal_plan[12:14]
    }
    return schedule

# Streamlit app layout
st.title('Child Weekly Meal Calendar')

if st.button('Generate Meal Plan'):
    meal_schedule = generate_meal_plan(meals)
    for day, meals in meal_schedule.items():
        st.header(day)
        for meal_name, meal_info in meals:
            st.subheader(meal_name)
            st.write(meal_info['explanation'])
            for ingredient in meal_info['ingredients']:
                amazon_link = create_amazon_link(ingredient)
                st.markdown(f"- [{ingredient}]({amazon_link})")

# Run this with `streamlit run your_script.py` in your command line
