# Дмитрий Трофимович, 8-я кагорта - Финальный проект. Инженер по тестированию плюс
import data
import sender_stand_request


def test_get_order_by_track():
    # Шаг 1: Выполняем запрос на создание заказа
    response = sender_stand_request.post_new_order(data.order_body)

    # Проверяем, что код ответа равен 201 (успешное создание заказа)
    assert response.status_code == 201

    # Извлекаем номер трека заказа из ответа
    track_order = response.json()["track"]
    assert track_order is not None

    # Шаг 2: Выполняем запрос на получение заказа по треку заказа
    response = sender_stand_request.get_order_by_track(track_order)

    # Проверяем, что код ответа равен 200 (успешное получение заказа по треку)
    assert response.status_code == 200
