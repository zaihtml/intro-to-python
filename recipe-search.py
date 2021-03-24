import requests


def recipe_search(ingredient, dietary_require, dietary_requirement_num,
                  meal_type, meal_type_num, calories):
    # Register to get an APP ID and key https://developer.edamam.com/
    app_id = 'ac163df5'
    app_key = 'a304cf9b2a79c2dbf8ccfb1ec3aef68e'

    # If we use the alternative way of formatting at the start I think we can add things a lot easier in for loops:
    url = f"https://api.edamam.com/search?q={ingredient}&app_id={app_id}&app_key={app_key}"

    # This should mean multiple health things can be added in one search
    for num in dietary_requirement_num:
        if num in ['1', '2', '3', '4', '5']:
            url = url + f"&health={dietary_require[int(num) - 1]}"

    # This should mean what kind of meal type can be added in one search
    for num in meal_type_num:
        if num in ['1', '2', '3']:
            url = url + f"&mealtype={meal_type[int(num) - 1]}"

    # This should mean the calorie content of each meal to be added in one search
    if str.isdigit(calories):  # checks if calories variable exists and if it can be converted to a number
        lower_bound = 500
        upper_bound = 1000
        calories_output = min(max(int(calories), lower_bound), upper_bound)
        url = url + f"&calories{calories_output}"

    result = requests.get(url)
    data = result.json()

    return data['hits']


def run():
    # Enter your ingredients
    ingredient = input('Enter ingredient(s) separated by commas: ')

    # Enter dietary requirements
    dietary_require = [
        'vegan', 'vegetarian', 'dairy-free', 'gluten-free', 'peanut-free'
    ]
    # Numbering starts at 1 for ease of use: then -1 when using number to reference list
    dietary_requirement_num = input(
        'Do you have any of these dietary requirements? If multiple then separate by commas. Vegan = 1, vegetarian = 2, lactose = 3, gluten = 4, peanut allergy = 5 '
    )

    # Enter which meal type you're looking for
    meal_type = ["breakfast", "lunch", "dinner"]
    meal_type_num = input(
        'Would you like recipes for breakfast, lunch or dinner?" Breakfast = 1, lunch = 2, dinner = 3 '
    )

    # Enter desired calorie intake
    calories = input(
        'What is your desired estimated calorie intake per meal? Can leave blank')

    results = recipe_search(ingredient, dietary_require,
                            dietary_requirement_num, meal_type, meal_type_num,
                            calories)

    label_unique = []

    for result in results:
        recipe = result['recipe']
        if recipe['label'] not in label_unique:
            print(recipe['label'])
            print(recipe['url'])
            print(recipe['image'])
            print()
        label_unique += [recipe['label']]
        # This adds each recipe name to a list, then you can use if recipe label not in this list, then print the info. This only prints unique recipes (no duplicates)


run()
