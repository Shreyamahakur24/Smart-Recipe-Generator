from flask import Flask, request, jsonify
from flask_cors import CORS 

app = Flask(__name__)
CORS(app) 

RECIPES = [
    {
        "name": "Simple Omelette",
        "ingredients": ["egg", "milk", "butter", "salt", "pepper"],
        "instructions": "Whisk eggs with milk, salt, and pepper. Melt butter in a pan. Pour in the egg mixture and cook until set.",
        "nutritional_info": "Calories: 200, Protein: 12g",
        "dietary": ["non-vegetarian"],
        "cooking_time": "10 min",
        "difficulty": "Easy"
    },
    {
        "name": "Pasta with Tomato Sauce (Basic)",
        "ingredients": ["pasta", "tomato", "garlic", "oil", "basil", "salt"],
        "instructions": "Boil pasta. Sauté garlic in oil. Add chopped tomatoes and simmer for 10 min. Mix with pasta and garnish with basil.",
        "nutritional_info": "Calories: 450, Protein: 15g",
        "dietary": ["vegetarian"],
        "cooking_time": "30 min",
        "difficulty": "Medium"
    },
    {
        "name": "Scrambled Eggs",
        "ingredients": ["egg", "milk", "salt", "pepper", "butter"],
        "instructions": "Whisk eggs with a splash of milk, salt, and pepper. Cook in a buttered pan, stirring until set.",
        "nutritional_info": "Calories: 180, Protein: 11g",
        "dietary": ["non-vegetarian"],
        "cooking_time": "5 min",
        "difficulty": "Easy"
    },
    {
        "name": "Garlic Bread",
        "ingredients": ["bread", "butter", "garlic", "parsley"],
        "instructions": "Mix softened butter with minced garlic and chopped parsley. Spread on bread and bake until golden.",
        "nutritional_info": "Calories: 250, Protein: 5g",
        "dietary": ["vegetarian"],
        "cooking_time": "15 min",
        "difficulty": "Easy"
    },
    {
        "name": "Tuna Sandwich",
        "ingredients": ["tuna", "mayonnaise", "bread", "celery", "onion"],
        "instructions": "Mix tuna with mayonnaise, chopped celery, and onion. Spread between two slices of bread.",
        "nutritional_info": "Calories: 350, Protein: 25g",
        "dietary": ["non-vegetarian"],
        "cooking_time": "10 min",
        "difficulty": "Easy"
    },
    {
        "name": "Rice Pilaf",
        "ingredients": ["rice", "broth", "onion", "butter", "salt"],
        "instructions": "Sauté chopped onion in butter. Add rice and stir until toasted. Add broth and simmer until liquid is absorbed.",
        "nutritional_info": "Calories: 300, Protein: 7g",
        "dietary": ["vegetarian"],
        "cooking_time": "40 min",
        "difficulty": "Medium"
    },
    {
        "name": "Fried Rice (Veggie)",
        "ingredients": ["rice", "egg", "carrot", "peas", "soy sauce", "oil"],
        "instructions": "Cook rice. Scramble egg. Sauté carrots and peas. Mix all ingredients with soy sauce in a hot pan.",
        "nutritional_info": "Calories: 400, Protein: 18g",
        "dietary": ["vegetarian"],
        "cooking_time": "25 min",
        "difficulty": "Medium"
    },
    {
        "name": "Lentil Soup",
        "ingredients": ["lentil", "carrot", "celery", "onion", "broth", "salt", "oil"],
        "instructions": "Sauté carrot, celery, and onion in oil. Add lentils, broth, and salt. Simmer until lentils are tender.",
        "nutritional_info": "Calories: 320, Protein: 16g",
        "dietary": ["vegetarian", "gluten-free"],
        "cooking_time": "50 min",
        "difficulty": "Hard"
    },
    {
        "name": "Potato Salad",
        "ingredients": ["potato", "mayonnaise", "mustard", "salt", "pepper", "celery"],
        "instructions": "Boil and chop potatoes. Mix with mayonnaise, mustard, salt, pepper, and chopped celery.",
        "nutritional_info": "Calories: 380, Protein: 5g",
        "dietary": ["vegetarian", "gluten-free"],
        "cooking_time": "35 min",
        "difficulty": "Easy"
    },
    {
        "name": "Simple Grilled Cheese",
        "ingredients": ["bread", "cheese", "butter"],
        "instructions": "Butter the outsides of two slices of bread. Place cheese in the middle and grill until cheese is melted.",
        "nutritional_info": "Calories: 340, Protein: 14g",
        "dietary": ["vegetarian"],
        "cooking_time": "10 min",
        "difficulty": "Easy"
    },
    {
        "name": "Quesadilla (Cheese)",
        "ingredients": ["tortilla", "cheese", "butter"],
        "instructions": "Sprinkle cheese on half of a tortilla. Fold it over. Cook in a buttered pan until cheese melts.",
        "nutritional_info": "Calories: 360, Protein: 16g",
        "dietary": ["vegetarian"],
        "cooking_time": "10 min",
        "difficulty": "Easy"
    },
    {
        "name": "Black Bean Salsa",
        "ingredients": ["black bean", "tomato", "onion", "lime", "cilantro"],
        "instructions": "Mix drained black beans, diced tomato, onion, and cilantro. Dress with lime juice and salt.",
        "nutritional_info": "Calories: 150, Protein: 8g",
        "dietary": ["vegetarian", "gluten-free"],
        "cooking_time": "15 min",
        "difficulty": "Easy"
    },
    {
        "name": "Cucumber Salad",
        "ingredients": ["cucumber", "yogurt", "garlic", "dill", "salt"],
        "instructions": "Slice cucumber thinly. Mix yogurt with minced garlic, dill, and salt. Combine with cucumber.",
        "nutritional_info": "Calories: 120, Protein: 6g",
        "dietary": ["vegetarian", "gluten-free"],
        "cooking_time": "15 min",
        "difficulty": "Easy"
    },
    {
        "name": "Chickpea Curry (Simple)",
        "ingredients": ["chickpea", "onion", "garlic", "ginger", "tomato", "curry powder", "oil"],
        "instructions": "Sauté onion, garlic, and ginger. Add curry powder and chopped tomato. Stir in chickpeas and simmer.",
        "nutritional_info": "Calories: 420, Protein: 18g",
        "dietary": ["vegetarian", "gluten-free"],
        "cooking_time": "45 min",
        "difficulty": "Medium"
    },
    {
        "name": "Oatmeal",
        "ingredients": ["oat", "milk", "sugar", "salt"],
        "instructions": "Combine oats, milk, and salt in a pot. Cook until creamy. Stir in sugar.",
        "nutritional_info": "Calories: 250, Protein: 8g",
        "dietary": ["vegetarian"],
        "cooking_time": "10 min",
        "difficulty": "Easy"
    },
    {
        "name": "Boiled Rice",
        "ingredients": ["rice", "water", "salt"],
        "instructions": "Bring water to a boil. Add rice and salt. Cover and simmer until water is absorbed.",
        "nutritional_info": "Calories: 200, Protein: 4g",
        "dietary": ["vegetarian", "gluten-free"],
        "cooking_time": "20 min",
        "difficulty": "Easy"
    },
    {
        "name": "Simple Fruit Smoothie",
        "ingredients": ["banana", "milk", "yogurt", "honey"],
        "instructions": "Combine all ingredients in a blender and blend until smooth.",
        "nutritional_info": "Calories: 280, Protein: 10g",
        "dietary": ["vegetarian", "gluten-free"],
        "cooking_time": "5 min",
        "difficulty": "Easy"
    },
    {
        "name": "Mashed Potatoes",
        "ingredients": ["potato", "milk", "butter", "salt", "pepper"],
        "instructions": "Boil and mash potatoes. Stir in milk, butter, salt, and pepper until smooth.",
        "nutritional_info": "Calories: 300, Protein: 6g",
        "dietary": ["vegetarian", "gluten-free"],
        "cooking_time": "30 min",
        "difficulty": "Medium"
    },
    {
        "name": "Black Bean Burger Patty",
        "ingredients": ["black bean", "bread crumb", "onion", "garlic", "egg", "chili powder"],
        "instructions": "Mash black beans. Mix with bread crumbs, diced onion, minced garlic, egg, and chili powder. Form into patties and cook.",
        "nutritional_info": "Calories: 350, Protein: 18g",
        "dietary": ["vegetarian"],
        "cooking_time": "35 min",
        "difficulty": "Medium"
    },
    {
        "name": "Quick Salsa",
        "ingredients": ["tomato", "onion", "jalapeno", "lime", "salt", "cilantro"],
        "instructions": "Dice tomato, onion, and jalapeno. Mix with lime juice, salt, and chopped cilantro.",
        "nutritional_info": "Calories: 80, Protein: 3g",
        "dietary": ["vegetarian", "gluten-free"],
        "cooking_time": "10 min",
        "difficulty": "Easy"
    },
    {
        "name": "Paneer Scramble",
        "ingredients": ["paneer", "onion", "turmeric", "oil", "salt", "pepper"],
        "instructions": "Crumble paneer. Sauté onion in oil. Add crumbled paneer, turmeric, salt, and pepper. Cook until heated through.",
        "nutritional_info": "Calories: 220, Protein: 15g",
        "dietary": ["vegetarian", "gluten-free"],
        "cooking_time": "15 min",
        "difficulty": "Easy"
    }
]


def find_recipes(available_ingredients):
    """
    Finds recipes based on partial ingredient match and calculates a match score.
    Returns: List of recipes with added 'match_score' and 'missing_ingredients'.
    """
    ranked_matches = []
    
   
    available_set = set(item.strip().lower() for item in available_ingredients)
    
    
    MIN_MATCH_COUNT = 1 
    
    for recipe in RECIPES:
        required_set = set(recipe["ingredients"])
        
        
        matched_ingredients = required_set.intersection(available_set)
        match_count = len(matched_ingredients)
        
        
        missing_ingredients = list(required_set.difference(available_set))
        
       
        total_required = len(required_set)
        match_percentage = (match_count / total_required) * 100 if total_required > 0 else 0
        
        if match_count >= MIN_MATCH_COUNT:
       
            matched_recipe = recipe.copy()
            matched_recipe["match_score"] = match_count
            matched_recipe["match_percentage"] = round(match_percentage)
            matched_recipe["missing_ingredients"] = missing_ingredients
            
            ranked_matches.append(matched_recipe)
            
    
    ranked_matches.sort(key=lambda x: x["match_score"], reverse=True)
            
    return ranked_matches

@app.route('/generate-recipe', methods=['POST'])
def generate_recipe():
    data = request.json
    
    if not data or 'ingredients' not in data:
        
        return jsonify({"error": "Missing ingredients list"}), 400 

    available_ingredients = data['ingredients']
    dietary_preference = data.get('dietary_preference', 'none') 
    
    
    all_matching_recipes = find_recipes(available_ingredients)
    
    
    if dietary_preference != 'none' and dietary_preference:
        preference_lower = dietary_preference.lower()
        
        filtered_recipes = [
            recipe for recipe in all_matching_recipes 
            if preference_lower in [d.lower() for d in recipe.get('dietary', [])]
        ]
    else:
        filtered_recipes = all_matching_recipes

    if filtered_recipes:
        
        return jsonify({"recipes": filtered_recipes})
    else:
        
        return jsonify({"message": "No recipes found. Try entering common ingredients like 'egg' or 'rice'."})

if __name__ == '__main__':
    app.run(debug=True, port=5000)