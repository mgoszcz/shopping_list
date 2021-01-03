from lib.shopping_list_interface import ShoppingListInterface


class Dumper:

    def __init__(self, interface: ShoppingListInterface):
        self._interface = interface

    def _get_articles(self):
        result_list = []
        for article in self._interface.shopping_articles:
            result_list.append(
                f'Name: {article.name}, Category: {article.category}, '
                f'Amount: {article.amount}, Selection: {article.selection}')
        return result_list

    def _get_shopping_list(self):
        result_list = []
        for article in self._interface.shopping_list:
            result_list.append(
                f'Name: {article.name}, Category: {article.category}, '
                f'Amount: {article.amount}, Selection: {article.selection}')
        return result_list

    def _get_categories(self):
        result_list = []
        for category in self._interface.categories:
            result_list.append(f'Category: {category}')
        return result_list

    def _get_shops(self):
        results_list = []
        joint = '\n'
        tab = '\t'
        for shop in self._interface.shops:
            categories = f'\n{joint.join([f"{tab}{item}" for item in shop.category_list])}'
            results_list.append(f'Name: {shop.name}, Logo: {shop.logo}, Categories: {categories}')
        return results_list

    def run(self):
        with open('dump.txt', 'w') as file:
            file.write('ARTICLES: \n')
            for article in self._get_articles():
                file.write('\t' + article + '\n')
            file.write('\n\nSHOPPING LIST: \n')
            for article in self._get_shopping_list():
                file.write('\t' + article + '\n')
            file.write('\n\nCATEGORIES: \n')
            for category in self._get_categories():
                file.write('\t' + category + '\n')
            file.write('\n\nSHOPS: \n')
            for shop in self._get_shops():
                file.write('\t' + shop + '\n')
