import json
from copy import deepcopy

with open('backup.json') as file:
    data1 = json.load(file).get('shopping_list')

data2 = deepcopy(data1)


def test():
    print('******TEST******')
    print('***Test1***')
    data2.get('shopping_articles_list').pop(24)
    data_comparator(data1, data2)
    print('***Test2***')
    data2.get('shopping_articles_list')[45]['category'] = 'kategoria'
    data_comparator(data1, data2)
    print('***Test3***')
    data2.get('shopping_articles_list')[77]['name'] = 'fryty'
    data_comparator(data1, data2)
    print('***Test4***')
    data2.get('shopping_list').pop(1)
    data_comparator(data1, data2)
    print('***Test5***')
    data2.get('shopping_list')[3]['amount'] = 3
    data_comparator(data1, data2)
    print('***Test6***')
    data2.get('shopping_list')[2]['checked'] = True
    data2.get('shopping_list')[3]['checked'] = True
    data_comparator(data1, data2)
    print('***Test7***')
    data2.get('shopping_list')[1]['article_name'] = 'salami'
    data_comparator(data1, data2)
    print('***Test8***')
    data2.get('shopping_list').append({'article_name': 'adddsdsddd', 'amount': 1, 'checked': False})
    data_comparator(data1, data2)
    print('***Test8_2***')
    data2.get('shopping_list').insert(4, {'article_name': 'rtrtyrtyyy', 'amount': 1, 'checked': False})
    data_comparator(data1, data2)
    print('***Test9***')
    data2.get('categories').pop(2)
    data_comparator(data1, data2)
    print('***Test10***')
    data2.get('categories')[11] = 'nowosc'
    data_comparator(data1, data2)
    print('***Test11***')
    data2.get('categories').append('ahhhhhh')
    data_comparator(data1, data2)
    print('***Test12***')
    data2.get('shops').pop(1)
    data_comparator(data1, data2)
    print('***Test13***')
    data2.get('shops')[0]['category_list'][16], data2.get('shops')[0]['category_list'][17] = \
    data2.get('shops')[0]['category_list'][17], data2.get('shops')[0]['category_list'][16]
    data_comparator(data1, data2)
    print('***Test14***')
    data2.get('shops')[1]['name'] = 'nowy'
    data_comparator(data1, data2)
    print('***Test15***')
    data2['current_shop'] = 'nowy'
    data_comparator(data1, data2)
    print('***Test16***')
    del data2.get('shops_icons')['asd.png']
    data_comparator(data1, data2)
    print('***Test17***')
    data2.get('shops_icons')['nowy.png'] = data2.get('shops_icons')['Lidl2.png']
    data_comparator(data1, data2)
    print('***Test18***')
    data2.get('shops_icons')['Auchan.png'] = 'wuripgnwiprugntwiprugntwirugntwrotu  wnepogntu rtrtrsw'
    data_comparator(data1, data2)

    print('***Test19***')
    data_comparator(data1, data2)


def find_dict_by_field(field_name, field_value, dict_list):
    for item in dict_list:
        if item.get(field_name) == field_value:
            return item
    return None


def compare_articles(pd, cd, id_field_name):
    index_to_remove = []
    for i, pattern_dict in enumerate(pd):
        incoming_item = find_dict_by_field(id_field_name, pattern_dict.get(id_field_name), cd)
        if not incoming_item:
            print(f'Pattern item {pattern_dict} not found in incoming data')
            index_to_remove.append(i)
            continue
        for key, value in pattern_dict.items():
            if incoming_item.get(key) != value:
                print(f'Pattern item {pattern_dict} and incoming {incoming_item} differs by {key}')
                pattern_dict[key] = incoming_item.get(key)
    for index in index_to_remove:
        pd.pop(index)
    for i, incoming_item in enumerate(cd):
        pattern_item = find_dict_by_field(id_field_name, incoming_item.get(id_field_name), pd)
        if not pattern_item:
            print(f'Incoming item {incoming_item} not found in pattern data')
            pd.insert(i, incoming_item)


def compare_categories(pl, inl):
    for i, category in enumerate(pl):
        if category not in inl:
            print(f'Pattern category {category} not found in incoming list')
            pl.pop(i)
    for i, category in enumerate(inl):
        if category not in pl:
            print(f'Incoming category {category} not found in pattern list')
            pl.insert(i, category)


def compare_shops_icons(pd, ind):
    result_dict = deepcopy(pd)
    for key, value in pd.items():
        if key not in ind:
            print(f'PAttern key does not exist in incoming dict: {key}')
            del result_dict[key]
            continue
        if value != ind.get(key):
            print(f'Pattern item {value} and incoming item {ind.get(key)} differs ')
            result_dict[key] = ind.get(key)
    for key, value in ind.items():
        if key not in pd:
            print(f'Incoming key does not exist in pattern dict: {key}')
            result_dict[key] = value
            continue
    return result_dict


def data_comparator(pattern, to_check):
    print('Compare shopping articles')
    compare_articles(pattern.get('shopping_articles_list'), to_check.get('shopping_articles_list'), 'name')
    print('Compare shopping list')
    compare_articles(pattern.get('shopping_list'), to_check.get('shopping_list'), 'article_name')
    print('Compare categories')
    compare_categories(pattern.get('categories'), to_check.get('categories'))
    print('Compare shops')
    compare_articles(pattern.get('shops'), to_check.get('shops'), 'name')
    print('Compare current shop')
    if pattern.get('current_shop') != to_check.get('current_shop'):
        print(f'Current shop differs, pattern: {pattern.get("current_shop")}, incoming: {to_check.get("current_shop")}')
        pattern['current_shop'] = to_check.get('current_shop')
    print('Compare shops icons')
    pattern['shops_icons'] = compare_shops_icons(pattern.get('shops_icons'), to_check.get('shops_icons'))


data_comparator(data1, data2)
test()
pass
