import streamlit as st

# This would be your Amazon referral link
AMAZON_REFERRAL = "gfm0dd-20"

# Sample meal data structure
meals = {
    'Mac & Cheese': {
        'ingredients': ['macaroni', 'cheese', 'milk', 'butter'],
        'instructions': 'Cook macaroni as per package instructions; drain. Melt butter in a pot, add milk and cheese, stir until smooth. Mix in macaroni until coated; serve warm.'
    },
    'Chicken Nuggets': {
        'ingredients': ['chicken', 'breadcrumbs', 'eggs'],
        'instructions': 'Cut chicken into bite-size pieces. Dip in beaten eggs, then coat with breadcrumbs. Bake or fry until golden brown; ensure it’s cooked through.'
    },
    'Spaghetti Bolognese': {
        'ingredients': ['spaghetti', 'ground beef', 'tomato sauce', 'onion', 'garlic'],
        'instructions': 'Cook spaghetti as instructed. Brown beef with onion and garlic; drain fat. Add tomato sauce, simmer; serve over spaghetti.'
    },
    'Cheese Quesadilla': {
        'ingredients': ['tortilla', 'cheese', 'salsa'],
        'instructions': 'Sprinkle cheese on half a tortilla, fold over. Cook on a skillet until cheese melts and tortilla is golden brown. Serve with salsa.'
    },
       'Grilled Cheese Sandwich': {
        'ingredients': ['bread', 'cheese', 'butter'],
        'instructions': 'Butter one side of each bread slice. Place bread butter-side-down on skillet, top with cheese, and cover with another slice of bread, butter-side-up. Cook on medium heat until bread is toasted and cheese is melted.'
    },
    'Veggie Pizza': {
        'ingredients': ['pizza dough', 'tomato sauce', 'cheese', 'bell peppers', 'mushrooms'],
        'instructions': 'Preheat oven as per pizza dough package instructions. Spread sauce on dough, sprinkle cheese, add bell peppers and mushrooms. Bake until crust is golden and cheese is bubbly.'
    },
    'Turkey and Cheese Roll-Up': {
        'ingredients': ['turkey', 'cheese', 'tortilla'],
        'instructions': 'Lay tortilla flat, place turkey and cheese on top, roll up tightly, slice into rounds and serve.'
    },
    'Peanut Butter & Jelly Sandwich': {
        'ingredients': ['peanut butter', 'jelly', 'bread'],
        'instructions': 'Spread peanut butter on one slice of bread and jelly on the other. Press slices together and serve.'
    },
    'Meatball Sub': {
        'ingredients': ['ground beef', 'breadcrumbs', 'tomato sauce', 'sub roll', 'parmesan cheese'],
        'instructions': 'Mix ground beef with breadcrumbs, form into balls, and cook. Simmer meatballs in sauce, then put in sub roll, top with parmesan, and serve.'
    },
    'Chicken Alfredo Pasta': {
        'ingredients': ['fettuccine', 'chicken', 'alfredo sauce', 'parmesan'],
        'instructions': 'Cook fettuccine as instructed; drain. Sauté chicken until cooked. Combine pasta, chicken, and alfredo sauce. Garnish with parmesan cheese.'
    },
       'Stir Fry Veggies with Rice': {
        'ingredients': ['rice', 'mixed vegetables', 'soy sauce'],
        'instructions': 'Cook rice as per package instructions. Stir fry mixed vegetables in a pan, add cooked rice and soy sauce, and stir until well mixed and heated through.'
    },
    'Baked Ziti': {
        'ingredients': ['ziti pasta', 'ricotta cheese', 'tomato sauce', 'mozzarella cheese'],
        'instructions': 'Cook ziti according to package instructions; drain. Mix with ricotta and tomato sauce, place in a baking dish, top with mozzarella, and bake until bubbly.'
    },
    'Tuna Salad': {
        'ingredients': ['tuna', 'mayonnaise', 'celery', 'lettuce'],
        'instructions': 'Mix tuna with mayonnaise and chopped celery. Serve on a bed of lettuce leaves.'
    },
    'Chicken Caesar Wrap': {
        'ingredients': ['chicken', 'romaine lettuce', 'caesar dressing', 'tortilla', 'parmesan cheese'],
        'instructions': 'Grill chicken and slice. Toss chicken with lettuce and caesar dressing. Lay on tortilla, sprinkle with parmesan, roll up, and serve.'
    },
    'BBQ Chicken Pizza': {
        'ingredients': ['pizza dough', 'chicken', 'bbq sauce', 'red onions', 'mozzarella cheese'],
        'instructions': 'Preheat oven. Spread bbq sauce on rolled out pizza dough, top with cooked chicken, red onions, and mozzarella. Bake as per dough instructions.'
    },
    'Hamburger': {
        'ingredients': ['ground beef', 'burger bun', 'lettuce', 'tomato', 'cheese'],
        'instructions': 'Form ground beef into patties and grill to desired doneness. Place on buns and top with lettuce, tomato, and cheese.'
    },
    'Hot Dog': {
        'ingredients': ['hot dog', 'bun', 'ketchup', 'mustard'],
        'instructions': 'Cook hot dog, place in bun, and top with ketchup and mustard.'
    },
    'Tomato Soup & Grilled Cheese': {
        'ingredients': ['tomato soup', 'bread', 'cheese', 'butter'],
        'instructions': 'Heat tomato soup as per instructions. Butter bread slices, place cheese between unbuttered sides, grill until golden brown. Serve together.'
    },
    'Rice & Beans': {
        'ingredients': ['rice', 'black beans', 'cheese', 'salsa'],
        'instructions': 'Cook rice as per instructions. Warm black beans, mix with cooked rice, top with cheese and salsa.'
    },
    'Chicken Tenders': {
        'ingredients': ['chicken', 'flour', 'eggs', 'breadcrumbs'],
        'instructions': 'Dredge chicken in flour, dip in beaten eggs, coat with breadcrumbs, and fry until golden and cooked through.'
    },
   'Pasta Primavera': {
        'ingredients': ['pasta', 'mixed vegetables', 'parmesan cheese', 'olive oil'],
        'instructions': 'Cook pasta as per package directions. Sauté mixed vegetables in olive oil, toss with cooked pasta, and garnish with parmesan cheese.'
    },
    'Meatloaf': {
        'ingredients': ['ground beef', 'breadcrumbs', 'ketchup', 'egg', 'onion'],
        'instructions': 'Combine all ingredients, shape into a loaf, and bake in preheated oven until cooked through. Top with additional ketchup if desired.'
    },
    'Chicken Soup': {
        'ingredients': ['chicken', 'chicken broth', 'noodles', 'carrots', 'celery'],
        'instructions': 'In a pot, combine chicken, broth, and vegetables; bring to a boil. Add noodles and simmer until noodles are tender.'
    },
    'Ham & Cheese Sandwich': {
        'ingredients': ['ham', 'cheese', 'bread', 'mustard'],
        'instructions': 'Assemble the sandwich with ham, cheese, and mustard between slices of bread. Serve cold or grilled.'
    },
    'Potato Wedges': {
        'ingredients': ['potatoes', 'olive oil', 'paprika'],
        'instructions': 'Cut potatoes into wedges, toss with olive oil and paprika, and bake until golden and crisp.'
    },
    'Chicken Quesadilla': {
        'ingredients': ['chicken', 'tortilla', 'cheese', 'salsa'],
        'instructions': 'Place cheese and cooked chicken on half of a tortilla, fold over, cook on a skillet until cheese melts. Serve with salsa.'
    },
    'Fish Sticks': {
        'ingredients': ['fish fillets', 'breadcrumbs', 'eggs'],
        'instructions': 'Cut fish into sticks, dip in beaten eggs, coat with breadcrumbs, and bake or fry until golden brown.'
    },
    'Scrambled Eggs & Toast': {
        'ingredients': ['eggs', 'bread', 'butter'],
        'instructions': 'Scramble eggs in a pan with butter. Toast bread and serve together.'
    },
    'Peanut Butter and Banana Sandwich': {
        'ingredients': ['peanut butter', 'banana', 'bread'],
        'instructions': 'Spread peanut butter on bread, add sliced banana, and close sandwich. Serve as is or grilled.'
    },
    'Mini Pizzas': {
        'ingredients': ['english muffins', 'tomato sauce', 'mozzarella cheese', 'pepperoni'],
        'instructions': 'Split english muffins, top with tomato sauce, cheese, and pepperoni, bake until cheese is melted.'
    },
    'Turkey Burger': {
        'ingredients': ['ground turkey', 'burger bun', 'lettuce', 'tomato'],
        'instructions': 'Form ground turkey into patties and grill. Serve on buns with lettuce and tomato.'
    },
    'Chicken and Rice Casserole': {
        'ingredients': ['chicken', 'rice', 'cream of mushroom soup', 'cheddar cheese'],
        'instructions': 'Layer cooked chicken and rice in a casserole dish, pour cream of mushroom soup over, top with cheese, and bake until bubbly.'
    },
    'Shepherds Pie': {
        'ingredients': ['ground beef', 'mashed potatoes', 'mixed vegetables'],
        'instructions': 'Layer cooked ground beef mixed with vegetables in a dish, top with mashed potatoes, and bake until the top is golden brown.'
    },
    'Sloppy Joes': {
        'ingredients': ['ground beef', 'tomato sauce', 'bell pepper', 'onion', 'burger bun'],
        'instructions': 'Cook beef with pepper and onion, stir in tomato sauce, simmer, and serve on buns.'
    },
    'Oatmeal with Fruit': {
        'ingredients': ['oatmeal', 'milk', 'banana', 'strawberries'],
        'instructions': 'Prepare oatmeal with milk as directed, top with sliced banana and strawberries.'
    },
    'Bean and Cheese Burrito': {
        'ingredients': ['tortilla', 'refried beans', 'cheese'],
        'instructions': 'Warm tortilla, spread refried beans in the center, sprinkle cheese, roll up, and optionally grill for a crisp exterior.'
    },
    'Chicken Pot Pie': {
        'ingredients': ['chicken', 'pie crust', 'frozen vegetables', 'chicken broth'],
        'instructions': 'Mix cooked chicken with vegetables and broth, place in pie crust, top with another crust, and bake until crust is golden.'
    },
    'French Toast': {
        'ingredients': ['bread', 'eggs', 'milk', 'cinnamon'],
        'instructions': 'Dip bread in a mixture of beaten eggs, milk, and cinnamon, then fry until golden brown on both sides.'
    },
    'Pancakes': {
        'ingredients': ['pancake mix', 'milk', 'eggs'],
        'instructions': 'Prepare pancake batter with mix, milk, and eggs; cook on a griddle until bubbles form and edges are dry.'
    },
    'Lasagna': {
        'ingredients': ['lasagna noodles', 'ricotta cheese', 'ground beef', 'tomato sauce', 'mozzarella cheese'],
        'instructions': 'Layer cooked noodles with cheese, cooked beef, and sauce. Repeat layers, top with cheese, and bake until bubbly and golden.'
    },
    'Chicken Curry with Rice': {
        'ingredients': ['chicken', 'curry sauce', 'rice'],
        'instructions': 'Cook chicken with curry sauce until done. Serve over cooked rice.'
    },
    'BLT Sandwich': {
        'ingredients': ['bacon', 'lettuce', 'tomato', 'bread', 'mayonnaise'],
        'instructions': 'Layer cooked bacon, lettuce, and tomato with mayonnaise on bread. Serve sandwich immediately.'
    },
    'Chicken Parmesan': {
        'ingredients': ['chicken', 'breadcrumbs', 'tomato sauce', 'mozzarella cheese', 'pasta'],
        'instructions': 'Bread chicken with breadcrumbs, fry until golden, top with sauce and cheese, bake until cheese melts. Serve over pasta.'
    },
    'Stuffed Peppers': {
        'ingredients': ['bell peppers', 'ground beef', 'rice', 'tomato sauce'],
        'instructions': 'Mix cooked beef and rice with tomato sauce, stuff into hollowed peppers, and bake until peppers are tender.'
    },
    'Yogurt Parfait': {
        'ingredients': ['yogurt', 'granola', 'honey', 'berries'],
        'instructions': 'Layer yogurt, granola, and berries in a glass. Drizzle with honey before serving.'
    },
    'Baked Potato': {
        'ingredients': ['potato', 'cheddar cheese', 'sour cream', 'chives'],
        'instructions': 'Bake potato until tender, split open, and top with cheese, sour cream, and chives.'
    },
    'Chili': {
        'ingredients': ['ground beef', 'tomato sauce', 'kidney beans', 'onion', 'cheddar cheese'],
        'instructions': 'Cook beef and onion, add tomato sauce and beans, simmer. Serve topped with cheddar cheese.'
    },
    'Salmon & Vegetables': {
        'ingredients': ['salmon', 'mixed vegetables', 'lemon', 'olive oil'],
        'instructions': 'Season salmon and vegetables with lemon and olive oil, and bake until salmon is flaky.'
    },
    'Chicken Gyro': {
        'ingredients': ['chicken', 'pita bread', 'tzatziki sauce', 'lettuce', 'tomato', 'onion'],
        'instructions': 'Wrap cooked chicken with vegetables in pita bread and top with tzatziki sauce.'
    },
    'Egg Salad Sandwich': {
        'ingredients': ['eggs', 'mayonnaise', 'mustard', 'bread', 'lettuce'],
        'instructions': 'Combine chopped eggs with mayonnaise and mustard. Spread on bread and add lettuce to assemble the sandwich.'
    },
    'Sausage & Peppers': {
        'ingredients': ['sausage', 'bell peppers', 'onion', 'tomato sauce', 'hoagie roll'],
        'instructions': 'Cook sausage with peppers and onion, simmer in tomato sauce, and serve on hoagie rolls.'
    }

    },
    # Repeat for each day of the week
    # ...
}

def generate_meal_plan():
    # You can add functionality here to generate a meal plan dynamically
    return meals

def create_amazon_link(ingredient):
    return f"https://www.amazon.com/s?k={ingredient.replace(' ', '+')}&tag={AMAZON_REFERRAL}"

def display_meal(day, meal_type, meal):
    st.header(f"{day} {meal_type}")
    st.subheader(meal["Name"])
    st.write(meal["Preparation"])
    st.subheader("Ingredients")
    for ingredient in meal["Ingredients"]:
        st.write(f"- {ingredient} ([Buy on Amazon]({create_amazon_link(ingredient)}))")

def app():
    st.title("Child Weekly Meal Calendar")

    weekly_meal_plan = generate_meal_plan()

    for day, meals in weekly_meal_plan.items():
        for meal_type, meal in meals.items():
            display_meal(day, meal_type, meal)

if __name__ == "__main__":
    app()
