import mysql.connector

from model.dollar import Dollar
from util.dollar_none import NoneException
from util.list_empty import EmptyException


def connection_factory():
    connection = mysql.connector.connect(
        host='192.168.0.9',  # host='10.10.167.180',
        user='root',
        password='root',
        database='dollar'
    )
    return connection


def connection_close(cursor, connection):
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()


def create(dollar):
    if dollar is not None:
        cursor = None
        connection = None
        try:
            connection = connection_factory()
            cursor = connection.cursor()
            sql = 'INSERT INTO dollar (preco, preco_max, preco_min, data_cotacao) VALUES (%s,%s,%s,%s)'
            values = (dollar.price, dollar.max_price, dollar.min_price, dollar.last_update)
            cursor.execute(sql, values)
            connection.commit()
            dollar.id_dollar = cursor.lastrowid
        except mysql.connector.Error as error:
            print(error)
        finally:
            connection_close(cursor, connection)
    else:
        raise NoneException
    return dollar


def selectall():
    dollars = []
    connection = None
    cursor = None
    try:
        connection = connection_factory()
        cursor = connection.cursor()
        sql = 'select * from dollar'
        cursor.execute(sql)
        result = cursor.fetchall()
        dollars = instance(result)
    except mysql.connector.Error as error:
        print(error)
    finally:
        connection_close(cursor, connection)
    return dollars


def select(number):
    connection = None
    cursor = None
    new_dollar = None
    try:
        connection = connection_factory()
        cursor = connection.cursor()
        sql = 'select * from dollar where id_dollar = %s'
        value = number
        cursor.execute(sql, value)
        result = cursor.fetchall()
        new_dollar = instance(result)
    except mysql.connector.Error as error:
        print(error)
    finally:
        connection_close(cursor, connection)
    return new_dollar


def instance(result):
    dollars = []
    for n in result:
        dollar = Dollar(
            n[1], n[2], n[3], n[4], n[0]
        )
        dollars.append(dollar)
    if len(dollars) == 0:
        raise EmptyException
    else:
        return dollars


def update(dollar):
    test = None
    if dollar is not None and dollar.id_dollar != 0 or None:
        connection = None
        cursor = None
        try:
            connection = connection_factory()
            cursor = connection.cursor()
            sql = 'update dollar set preco = %s, preco_max = %s, preco_min = %s, data_cotacao = %s where id_dollar = %s'
            values = (dollar.price, dollar.max_price, dollar.min_price, dollar.last_update, dollar.id_dollar)
            cursor.execute(sql, values)
            connection.commit()
            test = cursor.rowcount
        except mysql.connector.Error as error:
            print(error)
        finally:
            connection_close(cursor, connection)
    else:
        raise NoneException
    return f'Quantidade de itens afetados {test}'


print(select(1))
