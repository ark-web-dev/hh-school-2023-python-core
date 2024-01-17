from utils import convert_string_to_date
from wine import Wine
from beer import Beer

wines = [
    Wine('Merlot Reserve', convert_string_to_date('2010-03-15')),
    Wine('Cabernet Sauvignon', convert_string_to_date('2018-07-20')),
    Wine('Pinot Noir', convert_string_to_date('2015-11-10')),
    Wine('Syrah', convert_string_to_date('2008-06-30')),
    Wine('Malbec', convert_string_to_date('2013-04-05')),
    Wine('Chardonnay', convert_string_to_date('2019-09-12')),
    Wine(None, convert_string_to_date('2017-12-25')),
]

beers = [
    Beer('Zhigulevskoe', convert_string_to_date('2023-03-11')),
    Beer('Corona Extra', convert_string_to_date('2023-05-18')),
    Beer('Guinness Stout', convert_string_to_date('2021-08-07')),
    Beer('Heineken', convert_string_to_date('2016-12-03')),
    Beer('Stella Artois', convert_string_to_date('2014-02-28')),
    Beer('Sierra Nevada Pale Ale', convert_string_to_date('2010-10-15')),
    Beer('Blue Moon Belgian White', convert_string_to_date('2018-04-22')),
]
