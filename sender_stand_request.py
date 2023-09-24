import configuration
import data
import requests

# Функция создания нового заказа
def post_new_order_track():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER_PATH,  # подставляем полный url
                         json=data.order_body)  # а здесь заголовки

# Функция получения трека заказа
def get_new_order_track():
    # Создать новый заказ
    track_order = post_new_order_track()
    # Запомнить трек заказа
    return track_order.json()["track"]

# Функция получение заказа по его номеру
def get_order_number(track):
    # Выполняем запрос на получение заказа по его номеру
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_NUMBER_PATH + track);


