def ingredients_list(ingredient):
    ingredient_list = {}
    lst = ingredient.split('|')
    ingredient_list['ingredient_name'] = lst[0]
    ingredient_list['quantity'] = lst[1]
    ingredient_list['measure'] = lst[2]
    return ingredient_list

def get_shop_list_by_dishes(dishes, person_count):
    list_by_dishes = {}
    ingredients = []
    for dish in dishes:
        ingredients += cook_book[dish]
    for ingredient in ingredients:
        des = {}
        des['measure'] = ingredient['measure']
        quantity = int(ingredient['quantity'])*int(person_count)
        if ingredient['ingredient_name'] in list_by_dishes:
            quantity = list_by_dishes[ingredient['ingredient_name']]['quantity'] + quantity
        des['quantity'] = quantity
        list_by_dishes[ingredient['ingredient_name']] = des
    return list_by_dishes

cook_book = {}
next_dish = True
thisAmount = False
with open('file.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if line.strip() == '':
            next_dish = True
            continue
        if next_dish:
            dish = line.strip()
            next_dish = False
            thisAmount = True
            continue
        if thisAmount:
             cook_book[dish] = list()
             thisAmount = False
             continue
        ingredient_list = ingredients_list(line.strip())
        cook_book[dish].append(ingredient_list)

print(cook_book)
print(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2))





