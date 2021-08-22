"""Module contains ArticleSearch class"""
from typing import List

import unidecode

from lib.shopping_article.shopping_article import ShoppingArticle
from lib.shopping_article_list.shopping_articles_list import ShoppingArticlesList


class ArticleSearch:
    """Implement mechanism of searching articles"""
    def __init__(self, articles_list: ShoppingArticlesList) -> None:
        self._articles_list = articles_list

    def search_by_name(self, search_string: str) -> List[ShoppingArticle]:
        """Search articles by name"""
        results = []
        for article in self._articles_list:
            if search_string == article.name:
                results.append(article)
        for article in self._articles_list:
            if search_string in article.name and article not in results:
                results.append(article)
        for article in self._articles_list:
            if unidecode.unidecode(search_string) in unidecode.unidecode(article.name) and article not in results:
                results.append(article)
        return results
