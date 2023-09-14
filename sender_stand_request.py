import configuration
import requests


def post_new_order(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=body
    )


def get_order_by_track(track_order):
    response = requests.get(
        configuration.URL_SERVICE + configuration.RECEIVE_ORDER_PATH + f"?t={track_order}"
    )
    return response
