from market import Market
from drinks_data import wines
from drinks_data import beers

"""
TODO: Доработать заготовки классов вина (Wine), пива (Beer) и магазина (Market) таким образом, чтобы через класс Market можно было:

    * получить список всех напитков (вина и пива) отсортированный по наименованию
    * проверить наличие напитка в магазине (за время О(1))
    * получить список напитков (вина и пива) в указанном диапазоне даты производства
    * (*) написать свой декоратор, который бы логировал начало выполнения метода и выводил время выполнения
"""

market = Market(wines, beers)

print('* получить список всех напитков (вина и пива) отсортированный по наименованию')
for drink in market.get_drinks_sorted_by_title():
    print(drink.title, drink.production_date)

print('\n * проверить наличие напитка в магазине (за время О(1))')
print(f'Жигули в наличии: {market.has_drink_with_title("Zhigulevskoe")}')

print('\n * получить список напитков (вина и пива) в указанном диапазоне даты производства')
for drink in market.get_drinks_by_production_date('2018-01-18', '2022-01-22'):
    print(drink.title, drink.production_date)