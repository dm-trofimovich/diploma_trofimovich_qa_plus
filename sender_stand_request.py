import configuration
import requests
import data


def post_new_order(body):
    response = requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=body,
        headers=data.headers
    )

    # Проверяю, что код ответа равен 201 (успешное создание заказа)
    assert response.status_code == 201

    return response  # Возвращаем объект ответа


def get_order_by_track():
    response = post_new_order(data.order_body)
    track_order = str(response.json()["track"])  # Преобразую номер трека в строку
    new_headers = data.headers.copy()
    new_headers["track"] = track_order

    # Выполняю GET-запрос для получения заказа по треку
    response = requests.get(
        configuration.URL_SERVICE + configuration.RECEIVE_ORDER_PATH + "?t=" + track_order)

    return response
