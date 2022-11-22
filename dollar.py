class Dollar(object):
    def __init__(self, price, max_price, min_price, last_update, id_dollar=None, ):
        self.__id_dollar = id_dollar
        self.__price = price
        self.__max_price = max_price
        self.__min_price = min_price
        self.__last_update = last_update

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def max_price(self):
        return self.__max_price

    @max_price.setter
    def max_price(self, max_price):
        self.__max_price = max_price

    @property
    def min_price(self):
        return self.__min_price

    @min_price.setter
    def min_price(self, min_price):
        self.__min_price = min_price

    @property
    def last_update(self):
        return self.__last_update

    @last_update.setter
    def last_update(self, last_update):
        self.__last_update = last_update

    @property
    def id_dollar(self):
        return self.__id_dollar

    @id_dollar.setter
    def id_dollar(self, id_dolar):
        self.__id_dollar = id_dolar

    def __str__(self):
        return f'''
COTAÇÃO DO DÓLAR
Id dólar {self.id_dollar}
Data da consulta {self.last_update}
Preço atual {self.price} 
Preço máximo atingido no dia {self.max_price}
Preço mínimo atingido no dia {self.min_price}
'''
