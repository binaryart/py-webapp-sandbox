from dataclasses import dataclass


@dataclass
class __Action:
    name: str
    http_method: str
    id_scoped: bool


INDEX_ACTION = __Action(name="index", http_method="GET", id_scoped=False)
SHOW_ACTION = __Action(name="show", http_method="GET", id_scoped=True)
CREATE_ACTION = __Action(name="create", http_method="POST", id_scoped=False)
UPDATE_ACTION = __Action(name="update", http_method="PUT", id_scoped=True)
DELETE_ACTION = __Action(name="delete", http_method="DELETE", id_scoped=True)


__ALLOWED_ACTIONS = [INDEX_ACTION, SHOW_ACTION, CREATE_ACTION, UPDATE_ACTION, DELETE_ACTION]


def register(flask_app, base_uri, resource_module, id_type="int"):
    for action in __ALLOWED_ACTIONS:
        if hasattr(resource_module, action.name):
            rule = __rule(base_uri, action, id_type)
            endpoint = f'{base_uri}_{action.name}'.replace('/', '_')
            view_func = getattr(resource_module, action.name)

            flask_app.add_url_rule(rule, endpoint, view_func, methods=[action.http_method])


def __rule(base_uri, action, id_type):
    rule = f'/{base_uri}'
    return f'{rule}/<{id_type}:id>' if action.id_scoped else rule
