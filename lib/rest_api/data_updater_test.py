# {'data_set': <list_name>, 'item', <item_name>, 'action': <add/remove/update>, data: <dict>}
import json

import requests

from lib.rest_api.data_updater import DataUpdater, RequestError
from lib.rest_api.data_updater_model import DataUpdaterRequestModel
from lib.rest_api.server_addr import REST_API_SERVER, SHOPPING_LIST_NAME

with open('backup_for_testing.json') as file:
    data1 = json.load(file).get('shopping_list')

data_updater = DataUpdater(data1)

AUCHAN_DEFAULT_CATEGORIES = ["kwiatki", "grill", "przybory szkolne", "prasa", "świąteczne", "ogrodowe", "elektro",
                             "imprezowe", "świeczki", "baterie", "narzędzia", "pudełka", "samochodowe", "ręczniki",
                             "kuchenne", "łazienka", "pieczywo", "zabawki", "garmażeria", "wędlinynew", "ubrania",
                             "kosmetyki", "dziecięce", "domowe", "wędliny", "konserwowe", "chemia", "mąka", "herbata",
                             "przyprawy", "słodycze", "sosy", "makarony", "bio", "bakaliebababb", "owoce", "warzywa",
                             "ryby", "mięso", "alkohol", "chipsy", "woda", "soki", "napoje", "nabiał", "mrożonki"
                             ]
AUCHAN_NEW_CATEGORIES = ["kwiatki", "grill", "przybory szkolne", "prasa", "świąteczne", "ogrodowe", "elektro",
                         "imprezowe", "baterie", "świeczki", "narzędzia", "pudełka", "samochodowe", "ręczniki",
                         "kuchenne", "łazienka", "pieczywo", "zabawki", "garmażeria", "wędlinynew", "ubrania",
                         "kosmetyki", "dziecięce", "domowe", "wędliny", "konserwowe", "chemia", "mąka", "herbata",
                         "przyprawy", "słodycze", "sosy", "makarony", "bio", "bakaliebababb", "owoce", "warzywa",
                         "ryby", "mięso", "alkohol", "chipsy", "woda", "soki", "napoje", "nabiał", "mrożonki",
                         "leclerc"]


def send_and_update(request):
    data_updater.update(request)
    return send_request(request)


def send_request(request):
    server_response = requests.post(f'{REST_API_SERVER}/{SHOPPING_LIST_NAME}/update', json=request)
    return server_response

def get_data_from_server():
    objects = requests.get(f'{REST_API_SERVER}/{SHOPPING_LIST_NAME}')
    return objects.json().get('shopping_list')

def request_dict(data_set, item_name, action, data=None):
    return {'data_set': data_set, 'item': item_name, 'action': action, 'data': data}


def find_item_on_list(search_list, id_field_name, item_id):
    for item in search_list:
        if item.get(id_field_name) == item_id:
            return item
    return None

def remove_verification(test_list_name, id_field_name, item_id, resp=None):
    verify_item_not_on_list(data1.get(test_list_name), id_field_name, item_id)
    if resp:
        verify_201(resp)
    verify_item_not_on_list(get_data_from_server().get(test_list_name), id_field_name, item_id)

def existence_verification(test_list_name, item_dict, resp=None):
    verify_item_on_list(data1.get(test_list_name), item_dict)
    if resp:
        verify_201(resp)
    verify_item_on_list(get_data_from_server().get(test_list_name), item_dict)

def verify_item_not_on_list(search_list, id_field_name, item_id):
    if not find_item_on_list(search_list, id_field_name, item_id):
        print(f'Passed, item {item_id} not found on list')
    else:
        print(f'Failed, item {item_id} found on list')


def verify_item_on_list(search_list, item):
    if item in search_list:
        print(f'Passed, item {item} found on list')
    else:
        print(f'Failed, item {item} not found on list')


def verify_201(resp):
    if resp.status_code == 201:
        print(f'POST response test passed with response 201, message: {resp.json()}')
    else:
        print(f'POST response test failed with response {resp.status_code} and messgae: {resp.json()}')


def negative_test(request):
    try:
        data_updater.update(request)
        print('Negative update test failed, no exception')
    except RequestError as m:
        print(f'Negative update test passed, message: {m}')
    resp = send_request(request)
    if resp.status_code == 400:
        print(f'Negative POST test passed, server returned 400 with message: {resp.json()}')
    else:
        print(f'Negative POST test failed, server returned {resp.status_code} with message: {resp.json()}')


def empty_send_test():
    print('*** Empty data send test')
    resp = send_and_update([])
    print(f'passed, response: {resp.status_code}')


MULTI_CHANGE_EXPECTED_NOT_ON_LIST = [
    (DataUpdaterRequestModel.data_set.shopping_articles_list, 'salami')
]

MUTLI_CHANGE_EXPECTED_ON_LIST = [
    (DataUpdaterRequestModel.data_set.shopping_articles_list,
     {'name': 'bagietka', 'category': 'owoce', 'amount': 1, 'selection': 1}),
    (DataUpdaterRequestModel.data_set.shopping_articles_list,
     {'name': 'MultiNew', 'category': 'MultiNewCat', 'amount': 1, 'selection': 1}),
    (DataUpdaterRequestModel.data_set.shopping_list,
     {'article_name': 'MultiNew', 'amount': 1, 'checked': False})
]

MULTI_CHANGE = [request_dict(DataUpdaterRequestModel.data_set.shopping_articles_list, 'salami',
                             DataUpdaterRequestModel.actions.remove),
                request_dict(DataUpdaterRequestModel.data_set.shopping_articles_list, 'bagietka',
                             DataUpdaterRequestModel.actions.update, {'category': 'owoce'}),
                request_dict(DataUpdaterRequestModel.data_set.shopping_articles_list, '',
                             DataUpdaterRequestModel.actions.add, {'name': 'MultiNew', 'category': 'MultiNewCat'}),
                request_dict(DataUpdaterRequestModel.data_set.shopping_list, '',
                             DataUpdaterRequestModel.actions.add, {'article_name': 'MultiNew'}),
                request_dict(DataUpdaterRequestModel.data_set.categories, 'MultiNewCat',
                             DataUpdaterRequestModel.actions.add)
                ]


def invalid_data_test():
    print('*** Negative test 1')
    negative_test([request_dict('bad_set', 'item', 'add', {'name': 'abc'})])
    print('*** Negative test 2')
    negative_test([request_dict(DataUpdaterRequestModel.data_set.shopping_list, 'item', 'bad_action', {'name': 'abc'})])
    negative_test(
        [request_dict(DataUpdaterRequestModel.data_set.shopping_articles_list, 'item', 'bad_action', {'name': 'abc'})])
    print('*** Negative test 3')
    negative_test(
        [request_dict(DataUpdaterRequestModel.data_set.shopping_list, 'non-existing-item', 'update', {'name': 'abc'})])
    print('*** Negative test 4')
    negative_test(
        [request_dict(DataUpdaterRequestModel.data_set.shopping_list, 'new_item', 'add', {'invalid_data': 'abc'})])
    print('*** Negative test 5')
    negative_test(
        [request_dict(DataUpdaterRequestModel.data_set.shopping_list, 'new_item', 'add', ['list_instead_of_dict'])])
    print('*** Negative test 6')
    negative_test(
        [request_dict(DataUpdaterRequestModel.data_set.shopping_list, 'new_item', 'add', {})])
    print('*** Negative test 7')
    negative_test(
        [request_dict(DataUpdaterRequestModel.data_set.categories, 'new_item', 'update', {})])
    print('*** Negative test 8')
    negative_test(
        [request_dict(DataUpdaterRequestModel.data_set.current_shop, 'new_shop', 'remove', {})])
    print('*** Negative test 9')
    negative_test(
        [request_dict(DataUpdaterRequestModel.data_set.current_shop, '', 'update', {})])


def shopping_articles_test():
    test_list = DataUpdaterRequestModel.data_set.shopping_articles_list
    print('*** Shopping articles test 1 remove')
    resp = send_and_update([request_dict(test_list, 'mleko1', DataUpdaterRequestModel.actions.remove)])
    remove_verification(test_list, 'name', 'mleko1', resp)
    print('*** Shopping articles test 2 add')
    resp = send_and_update([request_dict(test_list, 'new_item', DataUpdaterRequestModel.actions.add,
                                      {'name': 'new item', 'category': 'elektro'})])
    existence_verification(test_list, {'name': 'new item', 'category': 'elektro', 'amount': 1, 'selection': 1}, resp)
    print('*** Shopping articles test 3 update category')
    resp = send_and_update(
        [request_dict(test_list, 'gwrtgwrtg', DataUpdaterRequestModel.actions.update, {'category': 'kosmetyki'})])
    existence_verification((test_list),
                        {'name': 'gwrtgwrtg', 'category': 'kosmetyki', 'amount': 1, 'selection': 1}, resp)


def shopping_list_test():
    test_list = DataUpdaterRequestModel.data_set.shopping_list
    print('*** Shopping list test 1 remove')
    resp = send_and_update([request_dict(test_list, 'mleko', DataUpdaterRequestModel.actions.remove)])
    remove_verification(test_list, 'article_name', 'mleko', resp)
    print('*** Shopping list test 2 add')
    resp = send_and_update([request_dict(test_list, '', DataUpdaterRequestModel.actions.add, {'article_name': 'rtrtrtr'})])
    existence_verification(test_list, {'article_name': 'rtrtrtr', 'amount': 1, 'checked': False}, resp)
    print('*** Shopping list test 3 update amount')
    resp = send_and_update([request_dict(test_list, 'masło', DataUpdaterRequestModel.actions.update, {'amount': 3})])
    existence_verification(test_list, {'article_name': 'masło', 'amount': 3, 'checked': False}, resp)
    print('*** Shopping list test 4 update checked')
    resp = send_and_update([request_dict(test_list, 'rtrtrtr', DataUpdaterRequestModel.actions.update, {'checked': True})])
    existence_verification(test_list, {'article_name': 'rtrtrtr', 'amount': 1, 'checked': True}, resp)


def categories_test():
    test_list = DataUpdaterRequestModel.data_set.categories
    print('*** categories list test 1 remove')
    resp = send_and_update([request_dict(test_list, 'alkohol', DataUpdaterRequestModel.actions.remove)])
    if 'alkohol' not in data1.get(test_list):
        print('Passed, alkohol not found on category list')
    else:
        print('Failed, alkohol found on category list')
    verify_201(resp)
    if 'alkohol' not in get_data_from_server().get(test_list):
        print('Passed, alkohol not found on category list on server')
    else:
        print('Failed, alkohol found on category list on server')
    print('*** categories list test 2 add')
    resp = send_and_update([request_dict(test_list, 'new-category', DataUpdaterRequestModel.actions.add)])
    if 'new-category' in data1.get(test_list):
        print('Passed, new-category found on category list')
    else:
        print('Failed, new-category not found on category list')
    verify_201(resp)
    if 'new-category' in get_data_from_server().get(test_list):
        print('Passed, new-category found on category list on server')
    else:
        print('Failed, new-category not found on category list on server')


def shops_test():
    test_list = DataUpdaterRequestModel.data_set.shops
    print('*** Shops test 1 remove')
    resp = send_and_update([request_dict(test_list, 'Lidl', DataUpdaterRequestModel.actions.remove)])
    remove_verification(test_list, 'name', 'Lidl', resp)
    print('*** Shops test 2 add - no logo and no categories')
    resp = send_and_update(
        [request_dict(test_list, '', DataUpdaterRequestModel.actions.add, {'name': 'NewShopNoLogoNoCategories'})])
    existence_verification(test_list, {'name': 'NewShopNoLogoNoCategories', 'logo': None, 'category_list': []}, resp)
    print('*** Shops test 3 add - logo and no categories')
    resp = send_and_update(
        [request_dict(test_list, '', DataUpdaterRequestModel.actions.add,
                      {'name': 'NewShopLogoNoCategories', 'logo': 'a/b/c.jpg'})])
    existence_verification(test_list,
                        {'name': 'NewShopLogoNoCategories', 'logo': 'a/b/c.jpg', 'category_list': []}, resp)
    print('*** Shops test 4 add - logo and categories')
    resp = send_and_update(
        [request_dict(test_list, '', DataUpdaterRequestModel.actions.add,
                      {'name': 'NewShopLogoCategories', 'logo': 'a/b/d.jpg',
                       'category_list': ['owoce', 'makarony', 'domowe']})])
    existence_verification(test_list,
                        {'name': 'NewShopLogoCategories', 'logo': 'a/b/d.jpg',
                         'category_list': ['owoce', 'makarony', 'domowe']}, resp)
    print('*** shops test 5 - logo update')
    resp = send_and_update(
        [request_dict(test_list, 'Auchan', DataUpdaterRequestModel.actions.update, {'logo': 'new/logo/path.png'})])
    existence_verification(test_list,
                        {'name': 'Auchan', 'logo': 'new/logo/path.png',
                         "category_list": AUCHAN_DEFAULT_CATEGORIES}, resp)
    print('*** shops test 6 - categories update')
    resp = send_and_update(
        [request_dict(test_list, 'Auchan', DataUpdaterRequestModel.actions.update,
                      {'category_list': AUCHAN_NEW_CATEGORIES})])
    existence_verification(test_list,
                        {'name': 'Auchan', 'logo': 'new/logo/path.png',
                         "category_list": AUCHAN_NEW_CATEGORIES}, resp)


def current_shop_test():
    test_set = DataUpdaterRequestModel.data_set.current_shop
    print('*** current shop test')
    resp = send_and_update(
        [request_dict(test_set, 'NewShopLogoCategories', DataUpdaterRequestModel.actions.update)])
    if data1.get(test_set) == 'NewShopLogoCategories':
        print('Passed, current shop updated to NewShopLogoCategories')
    else:
        print(f'Failed, current shop should be NewShopLogoCategories but it is {data1.get(test_set)}')
    verify_201(resp)
    if get_data_from_server().get(test_set) == 'NewShopLogoCategories':
        print('Passed, current shop updated to NewShopLogoCategories on server')
    else:
        print(f'Failed, current shop should be NewShopLogoCategories but it is {data1.get(test_set)} on server')


def multi_change_test():
    print('*** Multi change test')
    resp = send_and_update(MULTI_CHANGE)
    verify_201(resp)
    for test_list, item in MULTI_CHANGE_EXPECTED_NOT_ON_LIST:
        remove_verification(test_list, 'name', item)
    for test_list, item in MUTLI_CHANGE_EXPECTED_ON_LIST:
        existence_verification(test_list, item)
    if 'MultiNewCat' in data1.get(DataUpdaterRequestModel.data_set.categories):
        print('*** PAssed, MultiNewCat found on category list')
    else:
        print('*** Failed, MultiNewCat not found on category list')
    if 'MultiNewCat' in get_data_from_server().get(DataUpdaterRequestModel.data_set.categories):
        print('*** PAssed, MultiNewCat found on category list on server')
    else:
        print('*** Failed, MultiNewCat not found on category list on server')


empty_send_test()
invalid_data_test()
shopping_articles_test()
shopping_list_test()
categories_test()
shops_test()
current_shop_test()
multi_change_test()
pass
