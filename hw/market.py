from log_decorators import start_end_log_decorator
from utils import convert_string_to_date

class Market:
    @start_end_log_decorator
    def __init__(self, wines: list = None, beers: list = None) -> None:
        winesDct = {}
        if wines:
            for wine in wines:
                winesDct[wine.title] =  wine

        beersDct = {}
        if beers:
            for beer in beers:
                beersDct[beer.title] =  beer

        self.wines = winesDct
        self.beers = beersDct
        self.allDrinks = wines + beers if wines and beers else []

    @start_end_log_decorator
    def has_drink_with_title(self, title=None) -> bool:
        """
        Проверяет наличие напитка в магазине за О(1)

        :param title:
        :return: True|False
        """
        return title in self.wines or title in self.beers if title else []

    @start_end_log_decorator
    def get_drinks_sorted_by_title(self) -> list:
        """
        Метод получения списка напитков (вина и пива) отсортированных по title

        :return: list
        """
        return sorted(self.allDrinks, key = lambda drink: drink.title)

    @start_end_log_decorator
    def get_drinks_by_production_date(self, from_date=None, to_date=None) -> list:
        """
        Метод получения списка напитков в указанном диапазоне дат: с from_date по to_date

        :return: list
        """
        from_date = convert_string_to_date(from_date)
        to_date = convert_string_to_date(to_date)
        valid_drinks = []

        for drink in self.allDrinks:
            if from_date <= drink.production_date <= to_date:
                valid_drinks.append(drink)
        
        return valid_drinks
