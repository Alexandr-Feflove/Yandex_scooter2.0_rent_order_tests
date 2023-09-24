import sender_stand_request
import data

 # Проверка, что заказ найден
def test_get_order_number_code():
    order_response = sender_stand_request.get_order_number()
    # Проверяется, что код ответа равен 200
    assert order_response.status_code == 200
    # Отображаем результат ответа(для проверки самого себя)
    print(order_response.json())

