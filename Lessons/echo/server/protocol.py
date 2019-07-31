from datetime import datetime


def validate_request(request):
    """
    Проверить правильность клиентского запроса.
    :param request: пользовательский запрос.
    :return: результат проверки.
    """
    if 'action' in request and 'time' in request:
        return True
    return False


def make_response(request, code, data=None):
    """
    Сформировать ответ сервера.
    :param request: запрос клиента.
    :param code: код ответа сервера.
    :param data: данные передаваемые клиенту.
    :return: ответ сервера.
    """
    return {
        'action': request.get('action'),
        'time': datetime.now().timestamp(),
        'code': code,
        'data': data
    }
