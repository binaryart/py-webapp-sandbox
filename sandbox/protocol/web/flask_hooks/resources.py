from dataclasses import dataclass


def register(flask_app, base_uri, resource_module, member_path_rule="<string:guid>"):
    for action in __ALLOWED_ACTIONS:
        if hasattr(resource_module, action.name):
            rule = action.rule_for(base_uri, member_path_rule)
            endpoint = action.endpoint_for(base_uri)
            view_func = getattr(resource_module, action.name)

            flask_app.add_url_rule(rule, endpoint, view_func, methods=[action.http_method])


@dataclass
class __Action:
    name: str
    http_method: str
    is_member: bool

    def rule_for(self, base_uri, member_path_rule):
        rule = f"/{base_uri}"

        if self.is_member:
            rule = f"{rule}/{member_path_rule}"

        return rule

    def endpoint_for(self, base_uri):
        tokens = [
            t
            for t in base_uri.split("/")
            if "<" not in t
        ]

        return f"{'_'.join(tokens)}.{self.name}"


INDEX_ACTION = __Action(name="index", http_method="GET", is_member=False)
SHOW_ACTION = __Action(name="show", http_method="GET", is_member=True)
CREATE_ACTION = __Action(name="create", http_method="POST", is_member=False)
UPDATE_ACTION = __Action(name="update", http_method="PUT", is_member=True)
DELETE_ACTION = __Action(name="delete", http_method="DELETE", is_member=True)


__ALLOWED_ACTIONS = [INDEX_ACTION, SHOW_ACTION, CREATE_ACTION, UPDATE_ACTION, DELETE_ACTION]
