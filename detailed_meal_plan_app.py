import streamlit as st
import random

# Expanded list of meals and ingredients (example data, expand to 50 meals as needed)
meals = {
    'Mac & Cheese': ['macaroni', 'cheese', 'milk', 'butter'],
    'Chicken Nuggets': ['chicken', 'breadcrumbs', 'eggs'],
    'Spaghetti Bolognese': ['spaghetti', 'ground beef', 'tomato sauce', 'onion', 'garlic'],
    'Grilled Cheese Sandwich': ['bread', 'cheese', 'butter'],
    'Veggie Pizza': ['pizza dough', 'tomato sauce', 'cheese', 'bell peppers', 'mushrooms'],
    'Turkey and Cheese Roll-Up': ['turkey', 'cheese', 'tortilla'],
    'Peanut Butter & Jelly Sandwich': ['peanut butter', 'jelly', 'bread'],
    'Meatball Sub': ['ground beef', 'breadcrumbs', 'tomato sauce', 'sub roll', 'parmesan cheese'],
    'Cheese Quesadilla': ['tortilla', 'cheese', 'salsa'],
    'Beef Tacos': ['ground beef', 'taco shells', 'cheese', 'lettuce', 'tomato'],
    'Chicken Alfredo Pasta': ['fettuccine', 'chicken', 'alfredo sauce', 'parmesan'],
    'Stir Fry Veggies with Rice': ['rice', 'mixed vegetables', 'soy sauce'],
    'Baked Ziti': ['ziti pasta', 'ricotta cheese', 'tomato sauce', 'mozzarella cheese'],
    'Tuna Salad': ['tuna', 'mayonnaise', 'celery', 'lettuce'],
    'Chicken Caesar Wrap': ['chicken', 'romaine lettuce', 'caesar dressing', 'tortilla', 'parmesan cheese'],
    'BBQ Chicken Pizza': ['pizza dough', 'chicken', 'bbq sauce', 'red onions', 'mozzarella cheese'],
    'Hamburger': ['ground beef', 'burger bun', 'lettuce', 'tomato', 'cheese'],
    'Hot Dog': ['hot dog', 'bun', 'ketchup', 'mustard'],
    'Tomato Soup & Grilled Cheese': ['tomato soup', 'bread', 'cheese', 'butter'],
    'Rice & Beans': ['rice', 'black beans', 'cheese', 'salsa'],
    'Chicken Tenders': ['chicken', 'flour', 'eggs', 'breadcrumbs'],
    'Pasta Primavera': ['pasta', 'mixed vegetables', 'parmesan cheese', 'olive oil'],
    'Meatloaf': ['ground beef', 'breadcrumbs', 'ketchup', 'egg', 'onion'],
    'Chicken Soup': ['chicken', 'chicken broth', 'noodles', 'carrots', 'celery'],
    'Ham & Cheese Sandwich': ['ham', 'cheese', 'bread', 'mustard'],
    'Potato Wedges': ['potatoes', 'olive oil', 'paprika'],
    'Chicken Quesadilla': ['chicken', 'tortilla', 'cheese', 'salsa'],
    'Fish Sticks': ['fish fillets', 'breadcrumbs', 'eggs'],
    'Scrambled Eggs & Toast': ['eggs', 'bread', 'butter'],
    'Peanut Butter and Banana Sandwich': ['peanut butter', 'banana', 'bread'],
    'Mini Pizzas': ['english muffins', 'tomato sauce', 'mozzarella cheese', 'pepperoni'],
    'Turkey Burger': ['ground turkey', 'burger bun', 'lettuce', 'tomato'],
    'Chicken and Rice Casserole': ['chicken', 'rice', 'cream of mushroom soup', 'cheddar cheese'],
    'Shepherds Pie': ['ground beef', 'mashed potatoes', 'mixed vegetables'],
    'Sloppy Joes': ['ground beef', 'tomato sauce', 'bell pepper', 'onion', 'burger bun'],
    'Oatmeal with Fruit': ['oatmeal', 'milk', 'banana', 'strawberries'],
    'Bean and Cheese Burrito': ['tortilla', 'refried beans', 'cheese'],
    'Chicken Pot Pie': ['chicken', 'pie crust', 'frozen vegetables', 'chicken broth'],
    'French Toast': ['bread', 'eggs', 'milk', 'cinnamon'],
    'Pancakes': ['pancake mix', 'milk', 'eggs'],
    'Lasagna': ['lasagna noodles', 'ricotta cheese', 'ground beef', 'tomato sauce', 'mozzarella cheese'],
    'Chicken Curry with Rice': ['chicken', 'curry sauce', 'rice'],
    'BLT Sandwich': ['bacon', 'lettuce', 'tomato', 'bread', 'mayonnaise'],
    'Chicken Parmesan': ['chicken', 'breadcrumbs', 'tomato sauce', 'mozzarella cheese', 'pasta'],
    'Stuffed Peppers': ['bell peppers', 'ground beef', 'rice', 'tomato sauce'],
    'Yogurt Parfait': ['yogurt', 'granola', 'honey', 'berries'],
    'Baked Potato': ['potato', 'cheddar cheese', 'sour cream', 'chives'],
    'Chili': ['ground beef', 'tomato sauce', 'kidney beans', 'onion', 'cheddar cheese'],
    'Salmon & Vegetables': ['salmon', 'mixed vegetables', 'lemon', 'olive oil'],
    'Chicken Gyro': ['chicken', 'pita bread', 'tzatziki sauce', 'lettuce', 'tomato', 'onion'],
    'Egg Salad Sandwich': ['eggs', 'mayonnaise', 'mustard', 'bread', 'lettuce'],
    'Sausage & Peppers': ['sausage', 'bell peppers', 'onion', 'tomato sauce', 'hoagie roll']
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
