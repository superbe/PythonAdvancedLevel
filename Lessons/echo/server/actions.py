from functools import reduce
from settings import INSTALLED_APPS

from decorators import logged_def


@logged_def
def get_server_actions():
    modules = reduce(
        lambda value, item: value + [__import__(f'{item}.actions')],
        INSTALLED_APPS,
        [],
    )
    actions = reduce(
        lambda value, item: value + [getattr(item, 'actions', [])],
        modules,
        []
    )
    return reduce(
        lambda value, item: value + getattr(item, 'actionnames', []),
        actions,
        []
    )


@logged_def
def resolve(action_name, actions=None):
    action_list = actions or get_server_actions()
    action_mapping = {
        action.get('action'): action.get('controller')
        for action in action_list
    }
    return action_mapping.get(action_name)
