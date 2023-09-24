# Александр Фефлов, когорта 08-а — Финальный проект. Инженер по тестированию плюс

import sender_stand_request

 # Проверка, что заказ найден
def test_get_order_number_code():
    track = sender_stand_request.get_new_order_track()
    order_response = sender_stand_request.get_order_number(str(track))
    # Проверяется, что код ответа равен 200
    assert order_response.status_code == 200
    # Отображаем результат ответа(для проверки самого себя)
    print(order_response.json())

