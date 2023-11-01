import streamlit as st

# Placeholder for your Amazon referral link
AMAZON_REFERRAL_TAG = "gfm0dd-20"

def create_amazon_search_link(ingredient):
    # URL encode the ingredient name for the Amazon URL
    return f"https://www.amazon.com/s?k={ingredient.replace(' ', '+')}&tag={AMAZON_REFERRAL_TAG}"

def generate_weekly_meals():
    # This function would ideally generate a dynamic meal plan or retrieve it from a database
    weekly_meals = {
        'Monday': {
            'Breakfast': {
                'Name': 'Scrambled Eggs with Toast',
                'Preparation': 'Scramble eggs and serve with a side of toasted bread.',
                'Ingredients': ['Eggs', 'Bread', 'Butter', 'Salt', 'Pepper']
            },
            'Dinner': {
                'Name': 'Baked Salmon with Vegetables',
                'Preparation': 'Bake salmon and steam vegetables.',
                'Ingredients': ['Salmon fillets', 'Broccoli', 'Carrots', 'Olive oil', 'Lemon']
            }
        },
        # ... Add entries for other days of the week
    }
    return weekly_meals

def display_meals(weekly_meals):
    for day, meals in weekly_meals.items():
        st.header(day)
        for meal_time, meal_info in meals.items():
            st.subheader(meal_info['Name'] + f" ({meal_time})")
            st.write("Preparation:", meal_info['Preparation'])
            st.write("Ingredients:")
            for ingredient in meal_info['Ingredients']:
                link = create_amazon_search_link(ingredient)
                st.markdown(f"- {ingredient} ([Buy on Amazon]({link}))")

def app():
    st.title("Child Weekly Meal Calendar")
    
    if st.button('Generate Meal Calendar'):
        weekly_meals = generate_weekly_meals()
        display_meals(weekly_meals)

if __name__ == "__main__":
    app()
