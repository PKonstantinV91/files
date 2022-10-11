cook_book = {}
with open('file1.txt', 'rt', encoding='utf8') as file:
    for l in file:
        dish = l.strip()
        ingredients = []
        ingredients_count = file.readline()
        for i in range(int(ingredients_count)):
            ingr = file.readline()
            ingredient_name, quantity, measure = ingr.strip().split(' | ')
            ingredients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        blank_line = file.readline()
        cook_book.update({dish: ingredients})
print(cook_book)
print()

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for i in dishes:
        if i in cook_book.keys():
            for l in cook_book[i]:
                person_quantity = int(l['quantity']) * person_count
                shop_list.update({l['ingredient_name']: {'measure': l['measure'], 'quantity': person_quantity}})
    return shop_list

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


def number_of_line(*files):
    lines = {}
    for file in files:
        with open(file, encoding='utf-8') as file_obj:
            lines.update({file: len(file_obj.readlines())})
    lines2 = {}
    for i in sorted(lines, key=lines.get):
        lines2[i] = lines[i]
    return lines2


def writing_file(*files):
    text_dict = {}
    for i in number_of_line('files/1.txt', 'files/2.txt', 'files/3.txt'):
        with open(i, encoding='utf-8') as file_obj:
            f = file_obj.read()
            text_dict.update({i: f})
    for key, value in text_dict.items():
        with open('files/total.txt', 'a', encoding='utf-8') as file:
            file.writelines([f"{key}\n{number_of_line(*files)[key]}\n{value}\n"])


writing_file('files/1.txt', 'files/2.txt', 'files/3.txt')
