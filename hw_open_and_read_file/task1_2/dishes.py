from pprint import pprint


def create_cook_book(recipes):
    cook_book = {}
    with open(recipes, encoding = 'utf-8') as file_obj:
        
        for line in file_obj:
            current_dish = line.strip('\n')
            cook_book.setdefault(current_dish, [])
            quantity = int(file_obj.readline())
            recipe = []
            for item in range(quantity):
                data = file_obj.readline().strip().split(' | ')
                ingredient = {'ingredient_name': data[0], 'quantity': data[1], 'measure': data[2]}
                recipe.append(ingredient)
            cook_book[current_dish] = recipe
            file_obj.readline()

        return cook_book


def get_shop_list_by_dishes(book, dishes, person_count):
    ingr_for_shop = {}
    for dish in dishes:
        for ingredient in book[dish]:
            ingredient_temp = {ingredient['ingredient_name']: {'measure': ingredient['measure'],\
            'quantity': int(ingredient['quantity']) * person_count}}
            if ingredient['ingredient_name'] not in ingr_for_shop.keys():
                ingr_for_shop.update(ingredient_temp)
            else:
                ingr_for_shop[ingredient['ingredient_name']]['quantity'] += \
                ingredient_temp[ingredient['ingredient_name']]['quantity']
    return ingr_for_shop

pprint(create_cook_book('recipes.txt'))
pprint(get_shop_list_by_dishes(create_cook_book('recipes.txt'), ['Фахитос', 'Омлет'], 2))