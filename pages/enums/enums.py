from enum import Enum

class SortOption(Enum):
    POSITION = 'Position'
    PRODUCT_NAME = 'Product Name'
    PRICE = 'Price'

class LimiterOption(Enum):
    SET_12 = '12'
    SET_24 = '24'
    SET_36 = '36'