from datetime import datetime

from decorators import log


@log
def validate_request(request):
    if 'action' in request and 'time' in request:
        return True
    return False


@log
def make_response(request, code, data=None):
    return {
        'action': request.get('action'),
        'time': datetime.now().timestamp(),
        'code': code,
        'data': data
    }
