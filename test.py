from lib.lists.list_without_duplicates import ShoppingListWithoutDuplicates
from lib.save_load.events import SAVE_NEEDED
from lib.shop.shop import Shop
from lib.shopping_article.shopping_article import ShoppingArticle
from lib.shopping_article_list.shopping_articles_list import ShoppingArticlesList
from lib.shopping_categories.category_list import CategoryList
from lib.shopping_list_interface import ShoppingListInterface

lst = ShoppingListWithoutDuplicates()
interface = ShoppingListInterface()

# interface.shopping_list.remove_article('dioda')
# interface.shopping_list.add_existing_article(interface.shopping_list.shopping_articles_list.get_article_by_name('dioda'))

# PROSTA BAZA

# interface.shops.add_shop('Auchan')
# interface.shops.add_shop('Lidl')
#
# interface.shopping_articles.add_new_article('słodka papryka', 'przyprawy')
# interface.shopping_articles.add_new_article('arbuz', 'owoce')
# interface.shopping_articles.add_new_article('zarowka', 'elektro')
#
# interface.shopping_list.add_existing_article(interface.shopping_articles.get_article_by_name('słodka papryka'))
# interface.shopping_list.add_existing_article(interface.shopping_articles.get_article_by_name('arbuz'))
#
# interface.shopping_list.add_new_article('mleko', 'nabiał')
# interface.shopping_list.add_new_article('earl grey', 'herbata')

# POWTORZENIA W KATEGORIACH DO TESTOWANIA SORTOWANIA SKLEPU

interface.shops.add_shop('Auchan')
interface.shops.add_shop('Lidl')

interface.shopping_list.add_new_article('słodka papryka', 'przyprawy')
interface.shopping_list.add_new_article('salami', 'wędliny')
interface.shopping_list.add_new_article('pieprz', 'przyprawy')
interface.shopping_list.add_new_article('ziele', 'przyprawy')
interface.shopping_list.add_new_article('parówki', 'wędliny')
interface.shopping_list.add_new_article('cynamon', 'przyprawy')
interface.shopping_list.add_new_article('jabłko', 'owoce')
interface.shopping_list.add_new_article('winogrona', 'owoce')
interface.shopping_list.add_new_article('bagietka', 'pieczywo')
interface.shopping_list.add_new_article('earl grey', 'herbata')
interface.shopping_list.add_new_article('arbuz', 'owoce')
interface.shopping_list.add_new_article('mleko', 'nabiał')
interface.shopping_list.add_new_article('gruszka', 'owoce')
interface.shopping_list.add_new_article('proszek', 'chemia')
interface.shopping_list.add_new_article('żarówka', 'elektro')
interface.shopping_list.add_new_article('dioda', 'elektro')
interface.shopping_list.add_new_article('tranzystor', 'elektro')
interface.shopping_list.add_new_article('pampersy', 'dziecięce')
interface.shopping_list.add_new_article('baterie', 'elektro')

shop = interface.shops.get_shop_by_name('Lidl')
for cat in ['pieczywo', 'herbata', 'dziecięce', 'chemia', 'owoce', 'przyprawy', 'wędliny', 'nabiał']:
    shop.category_list.append(cat)
shop = interface.shops.get_shop_by_name('Auchan')
for cat in ['pieczywo', 'elektro', 'wędliny', 'chemia', 'dziecięce', 'przyprawy', 'herbata', 'owoce', 'nabiał']:
    shop.category_list.append(cat)

interface.save_load.save_data()

new_int = ShoppingListInterface()

new_int.save_load.load_data()

pass

mleko = ShoppingArticle('mleko', 'nabiał')
slodka_papryka = ShoppingArticle('słodka papryka', 'przyprawy')
arbuz = ShoppingArticle('arbuz', 'owoce')
auchan = Shop('Auchan')

lista_artykułów = ShoppingArticlesList()
lista_artykułów.append(mleko)
lista_artykułów.append(slodka_papryka)
lista_artykułów.append(arbuz)

lista_kategorii = CategoryList()
lista_kategorii.append('nabiał')
lista_kategorii.append('przyprawy')
lista_kategorii.append('owoce')

lista_artykułów.sort_by_article_name()

pass