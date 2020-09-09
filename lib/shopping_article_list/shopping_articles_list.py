

class ShoppingArticlesList(list):

    def sort_by_article_name(self):
        self.sort(key=lambda x: x.name)
