import data
import sender_stand_request


# Дмитрий Трофимович, 8-я когорта — Финальный проект. Инженер по тестированию плюс
def test_get_order_by_track():
    # Шаг 1: Выполняю запрос на создание заказа
    response = sender_stand_request.post_new_order(data.order_body)

    # Проверяю, что код ответа равен 201 (успешное создание заказа)
    assert response.status_code == 201

    # Извлекаю номер трека заказа из ответа
    track_order = response.json()["track"]
    assert track_order is not None

    # Шаг 2: Выполняю запрос на получение заказа по треку заказа
    response = sender_stand_request.get_order_by_track()

    # Проверяю, что код ответа равен 200 (успешное получение заказа по треку)
    assert response.status_code == 200
