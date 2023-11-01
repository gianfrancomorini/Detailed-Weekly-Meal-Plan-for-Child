import streamlit as st

# This is a placeholder for your Amazon referral link
AMAZON_REFERRAL = "gfm0dd-20"

# Sample meal data
meals = {
    "Monday": {
        "Breakfast": {
            "Name": "Oatmeal with Fruits",
            "Preparation": "Cook the oatmeal and top it with your choice of fruits.",
            "Ingredients": ["Oatmeal", "Banana", "Strawberry", "Honey"]
        },
        "Dinner": {
            "Name": "Grilled Chicken Salad",
            "Preparation": "Grill the chicken and mix it with salad greens and dressing.",
            "Ingredients": ["Chicken breast", "Salad greens", "Caesar dressing"]
        }
    },
    # Add similar dictionaries for other days of the week
}

def generate_meal_plan():
    # This function would generate a meal plan, for simplicity we're using a static dict
    return meals

def create_amazon_link(ingredient):
    # This function creates a URL for an ingredient search on Amazon with the referral tag
    return f"https://www.amazon.com/s?k={ingredient.replace(' ', '+')}&tag={AMAZON_REFERRAL}"

def display_meal(day, meal_type, meal):
    st.header(f"{day} - {meal_type}")
    st.subheader(meal["Name"])
    st.write(meal["Preparation"])
    st.subheader("Ingredients")
    for ingredient in meal["Ingredients"]:
        link = create_amazon_link(ingredient)
        st.markdown(f"- {ingredient} ([Buy on Amazon]({link}))")

def app():
    st.title("Child Weekly Meal Calendar")

    # Generate or retrieve the meal plan
    weekly_meal_plan = generate_meal_plan()

    # Display the meal plan
    for day, day_meals in weekly_meal_plan.items():
        for meal_type, meal in day_meals.items():
            display_meal(day, meal_type, meal)

if __name__ == "__main__":
    app()
