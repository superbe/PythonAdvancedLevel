import pytest

from datetime import datetime

from messanger.controllers import send_message


@pytest.fixture
def expected_action():
    return 'test'


@pytest.fixture
def expected_code():
    return 200


@pytest.fixture
def expected_data():
    return 'Some data'


@pytest.fixture
def initial_request(expected_action, expected_data):
    return {
        'action': expected_action,
        'time': datetime.now().timestamp(),
        'data': expected_data
    }


def test_action_make_response(initial_request, expected_action, expected_code, expected_data):
    actual_send_message = send_message(initial_request)
    assert actual_send_message.get('action') == expected_action


def test_code_make_response(initial_request, expected_code):
    actual_send_message = send_message(initial_request)
    assert actual_send_message.get('code') == expected_code


def test_data_make_response(initial_request, expected_data):
    actual_send_message = send_message(initial_request)
    assert not actual_send_message.get('data')
