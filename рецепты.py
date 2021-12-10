from pprint import pprint 

def cook_dict(file_name):   
    cook_book = {}
    with open(file_name) as file:
        for line in file:
            dish = line.strip()
            counter = int(file.readline())
            recipe_list = []
            for item in range(counter):
                ingredient_name, quantity, measure = file.readline().split(' | ')
                recipe_list.append(
                    {'имя_ингредиента' : ingredient_name, 'количество' : int(quantity), 'мера' : measure.rstrip()}
                )
            cook_book[dish] = recipe_list
            file.readline()
    return cook_book



def get_shop_list_by_dishes(dishes, person_count):
    cook_book = cook_dict('рецепты.txt')
    dict_book = {}
    for dish in dishes:
        for a in cook_book[dish]:
            ingredient = a['имя_ингредиента']
            units = a['мера']
            quant = (int(a['количество']))*person_count
            if ingredient not in dict_book:
                dict_book.update({ingredient:{'мера': units,'количество': quant}})
            elif ingredient in dict_book:
                dict_book[ingredient]['количество'] = (quant + int(dict_book[ingredient]['количество']))
    return dict_book

get_shop_list_by_dishes(['Кофе', 'Утка по-пекински'], 2)