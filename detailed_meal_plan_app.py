import streamlit as st
import random
import requests

def get_amazon_link(ingredient, referral_code="gfm0dd-20"):
    return f"https://www.amazon.com/s?k={ingredient}&tag={referral_code}"

def get_unsplash_image(query, api_key):
    url = f"https://api.unsplash.com/search/photos?page=1&query={query}&client_id={api_key}"
    response = requests.get(url)
    data = response.json()
    if data["results"]:
        return data["results"][0]["urls"]["small"]
    return "https://via.placeholder.com/150"  # default placeholder if no image found

API_KEY = "y7sY9svzrBEGTMLfN4mFwjjoP_aP11y7lZcLqH7Ml-Q"  # Replace with your Unsplash API key

# Database of child-friendly meals
MEALS = {
    "Pasta Salad": {
        "ingredients": ["pasta", "cherry tomatoes", "cucumber", "feta cheese", "olive oil", "oregano"],
        "instructions": ["Boil pasta until al dente. Drain.", "Mix pasta with cut tomatoes, sliced cucumber, and feta cheese.", "Drizzle with olive oil and sprinkle oregano before serving."]
    },

    "Spaghetti Bolognese": {
        "ingredients": ["spaghetti", "ground beef", "tomato sauce", "onion", "garlic", "olive oil"],
        "instructions": ["Boil spaghetti until al dente.", "In a pan, sauté onions and garlic in olive oil.", "Add ground beef and cook until brown.", "Pour in tomato sauce and simmer for 20 minutes."],
    },
    "Chicken Nuggets": {
        "ingredients": ["chicken breasts", "breadcrumbs", "egg", "salt", "pepper", "oil"],
        "instructions": ["Cut chicken into small pieces.", "Dip each piece in egg, then coat with breadcrumbs.", "Heat oil in a pan and fry chicken pieces until golden brown."],
    },
    "Veggie Stir Fry": {
        "ingredients": ["bell peppers", "carrots", "broccoli", "soy sauce", "garlic", "olive oil"],
        "instructions": ["Chop veggies into bite-sized pieces.", "In a pan, sauté garlic in olive oil.", "Add veggies and stir fry for 5-7 minutes.", "Add soy sauce and cook for another 2 minutes."],
    },
    "Cheese Quesadilla": {
        "ingredients": ["tortilla", "cheddar cheese", "butter"],
        "instructions": ["Place cheese between two tortillas.", "Melt butter in a pan.", "Cook tortilla on both sides until golden brown and cheese is melted."],
    },
    "Peanut Butter & Jelly Sandwich": {
        "ingredients": ["bread", "peanut butter", "jelly"],
        "instructions": ["Spread peanut butter on one slice of bread.", "Spread jelly on another slice.", "Press the two slices together."],
    },
    "Mini Pizzas": {
        "ingredients": ["mini pizza bases", "tomato sauce", "mozzarella cheese", "pepperoni"],
        "instructions": ["Spread tomato sauce on pizza base.", "Sprinkle mozzarella cheese.", "Add pepperoni slices.", "Bake in oven until cheese is melted and base is crispy."],
    },
    "Fruit Salad": {
        "ingredients": ["strawberries", "blueberries", "kiwi", "orange", "honey"],
        "instructions": ["Chop all fruits into bite-sized pieces.", "Mix in a bowl.", "Drizzle with a little honey for sweetness."],
    },
    "Mac and Cheese": {
        "ingredients": ["macaroni", "cheddar cheese", "milk", "butter", "flour"],
        "instructions": ["Cook macaroni according to package instructions.", "In another pot, melt butter, add flour and stir.", "Gradually add milk and cheese. Stir until smooth sauce forms.", "Mix sauce with macaroni."],
    },
    "Fish Sticks": {
        "ingredients": ["fish fillets", "breadcrumbs", "egg", "lemon", "salt", "pepper"],
        "instructions": ["Cut fish into sticks.", "Dip in beaten egg, then coat with breadcrumbs.", "Fry until golden brown. Serve with lemon wedges."],
    },
    "Veggie Wraps": {
        "ingredients": ["tortilla wraps", "lettuce", "tomato", "cucumber", "carrot", "ranch dressing"],
        "instructions": ["Lay tortilla flat. Spread a little ranch dressing.", "Add lettuce, sliced tomatoes, cucumbers, and grated carrot.", "Roll up the tortilla."],
    },
    "Egg Salad Sandwich": {
        "ingredients": ["bread", "eggs", "mayonnaise", "salt", "pepper", "lettuce"],
        "instructions": ["Boil eggs, then chop them.", "Mix with mayonnaise, salt, and pepper.", "Spread on bread, add lettuce, and make a sandwich."],
    }, 
    "Grilled Cheese Sandwich": {
        "ingredients": ["bread", "butter", "cheddar cheese"],
        "instructions": ["Butter one side of each bread slice.", "Place cheese between slices, buttered side out.", "Grill on a skillet until golden brown on each side and cheese is melted."],
    },
    "Chicken Alfredo Pasta": {
        "ingredients": ["pasta", "chicken breasts", "alfredo sauce", "parmesan cheese", "olive oil"],
        "instructions": ["Cook pasta according to package instructions.", "In a pan, cook chicken in olive oil until done.", "Add alfredo sauce and cooked pasta, mixing well. Serve with parmesan cheese."],
    },
    "Beef Tacos": {
        "ingredients": ["ground beef", "taco seasoning", "taco shells", "lettuce", "tomato", "cheese", "sour cream"],
        "instructions": ["Cook beef in a skillet and add taco seasoning.", "Fill taco shells with beef, lettuce, diced tomato, cheese, and top with sour cream."],
    },
    "Veggie Omelette": {
        "ingredients": ["eggs", "bell peppers", "onions", "tomatoes", "cheese", "salt", "pepper"],
        "instructions": ["Beat eggs and season with salt and pepper.", "Sauté veggies in a pan.", "Add beaten eggs and cheese. Cook until set."],
    },
    "Chicken Soup": {
        "ingredients": ["chicken", "carrots", "onions", "celery", "noodles", "chicken broth"],
        "instructions": ["Cook chicken in broth until done. Remove and shred.", "Add diced veggies to the broth. Once tender, add noodles.", "Once noodles are cooked, add shredded chicken back to the pot."],
    },
    "Pancakes": {
        "ingredients": ["pancake mix", "water", "syrup", "butter"],
        "instructions": ["Mix pancake mix with water.", "Pour batter onto hot griddle. Flip when bubbles form.", "Serve with butter and syrup."],
    },
    "Bean Burritos": {
        "ingredients": ["tortilla", "refried beans", "cheese", "salsa"],
        "instructions": ["Spread beans on tortilla.", "Add cheese and salsa.", "Roll up and microwave until cheese is melted."],
    },
    "French Toast": {
        "ingredients": ["bread", "eggs", "milk", "cinnamon", "syrup"],
        "instructions": ["Beat eggs with milk and cinnamon.", "Dip bread in egg mixture.", "Cook on a hot skillet until golden brown. Serve with syrup."],
    },
    "Baked Ziti": {
        "ingredients": ["ziti pasta", "marinara sauce", "ricotta cheese", "mozzarella cheese", "parmesan cheese"],
        "instructions": ["Cook pasta. In a baking dish, layer pasta, ricotta, marinara sauce, and cheeses.", "Repeat layers and bake until bubbly."],
    },
    "Chicken Caesar Wrap": {
        "ingredients": ["tortilla", "grilled chicken", "lettuce", "parmesan cheese", "caesar dressing"],
        "instructions": ["Place chicken, lettuce, cheese, and dressing on tortilla.", "Roll up tightly."],
    },
    "Mashed Potatoes": {
        "ingredients": ["potatoes", "butter", "milk", "salt", "pepper"],
        "instructions": ["Boil potatoes until tender. Mash with butter and milk.", "Season with salt and pepper."],
    },
    "Chicken and Rice": {
        "ingredients": ["chicken", "rice", "chicken broth", "carrots", "peas"],
        "instructions": ["Cook chicken in a pan. Remove and set aside.", "In the same pan, add rice and broth. Once rice is almost done, add veggies.", "Add chicken back to the pan until fully cooked."],
    },
    "Peanut Butter and Banana Sandwich": {
        "ingredients": ["bread", "peanut butter", "banana"],
        "instructions": ["Spread peanut butter on bread.", "Add banana slices.", "Close sandwich and enjoy."],
    },
    "Tomato Soup and Grilled Cheese": {
        "ingredients": ["canned tomato soup", "bread", "butter", "cheese"],
        "instructions": ["Heat soup in a pot.", "Make grilled cheese sandwich by buttering bread, adding cheese, and grilling until golden brown."],
    },
    "Ham and Cheese Rollups": {
        "ingredients": ["sliced ham", "cheese sticks"],
        "instructions": ["Place a cheese stick at the edge of a ham slice.", "Roll up tightly."],
    },
    "Creamed Spinach": {
        "ingredients": ["spinach", "butter", "milk", "flour", "salt", "pepper", "nutmeg"],
        "instructions": ["Melt butter, add flour. Slowly add milk to make a sauce.", "Add spinach and cook until wilted. Season with salt, pepper, and a pinch of nutmeg."],
    },
    "Potato Wedges": {
        "ingredients": ["potatoes", "olive oil", "salt", "pepper", "paprika"],
        "instructions": ["Cut potatoes into wedges. Toss with olive oil and seasonings.", "Bake until golden brown and crispy."],
    },
    "Spaghetti Carbonara": {
        "ingredients": ["spaghetti", "eggs", "parmesan cheese", "bacon", "garlic", "salt", "pepper"],
        "instructions": ["Cook spaghetti. In a bowl, mix eggs, cheese, salt, and pepper.", "Cook bacon until crispy. Add garlic.", "Add pasta to bacon, remove from heat. Quickly stir in egg mixture."],
    },
    "Chicken Nuggets": {
        "ingredients": ["chicken breasts", "bread crumbs", "eggs", "flour", "salt", "pepper"],
        "instructions": ["Cut chicken into nugget sizes. Dip in flour, then beaten eggs, then bread crumbs.", "Fry until golden brown."],
    },
    "Mac and Cheese": {
        "ingredients": ["macaroni", "butter", "flour", "milk", "cheddar cheese", "salt", "pepper"],
        "instructions": ["Cook macaroni. Melt butter, add flour. Slowly add milk to make a sauce.", "Add cheese and stir until melted. Mix in macaroni."],
    },
    "Peanut Butter and Jelly Sandwich": {
        "ingredients": ["bread", "peanut butter", "jelly"],
        "instructions": ["Spread peanut butter on one slice of bread and jelly on the other.", "Press slices together."],
    },
    "BBQ Chicken Pizza": {
        "ingredients": ["pizza dough", "BBQ sauce", "cooked chicken", "red onion", "mozzarella cheese", "cilantro"],
        "instructions": ["Spread BBQ sauce on dough. Top with chicken, onion, and cheese.", "Bake until crust is golden. Top with cilantro before serving."],
    },
    "Fish Sticks": {
        "ingredients": ["fish fillets", "bread crumbs", "eggs", "flour", "salt", "pepper"],
        "instructions": ["Cut fish into stick sizes. Dip in flour, then beaten eggs, then bread crumbs.", "Fry until golden brown."],
    },
    "Meatball Sub": {
        "ingredients": ["sub roll", "meatballs", "marinara sauce", "mozzarella cheese"],
        "instructions": ["Place meatballs and sauce on sub roll.", "Top with cheese. Bake until cheese is melted."],
    },
    "Quesadillas": {
        "ingredients": ["tortilla", "cheese", "chicken", "bell peppers", "onions"],
        "instructions": ["Place cheese, chicken, peppers, and onions on half of tortilla.", "Fold over and grill until golden brown."],
    },


allergic_ingredients = st.text_input("Enter allergic ingredients (comma separated)").split(',')
filtered_meals = {meal_name: details for meal_name, details in meals.items() if not any(allergen in details['ingredients'] for allergen in allergic_ingredients)}

if st.button('Generate Meal Plan'):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    for day in days:
        st.subheader(day)
        selected_meals = random.sample(list(filtered_meals.keys()), 2)  # Selects two meals for the day
        
        for meal in selected_meals:
            st.write(f"**{meal}**")
            ingredients = filtered_meals[meal]['ingredients']
            for ingredient in ingredients:
                st.markdown(f"[{ingredient}]({get_amazon_link(ingredient)})")
            st.write("Instructions: ")
            for index, step in enumerate(filtered_meals[meal]['instructions'], 1):
                st.write(f"{index}. {step}")
            st.image(get_unsplash_image(meal, API_KEY))
        st.write("----")