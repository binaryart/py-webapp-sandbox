def serialize(content, as_list=False):
    if as_list and not content:
        return []

    if as_list:
        return [
            _to_dict(element)
            for element in content
        ]
    else:
        return _to_dict(content)


def _to_dict(element):
    return {
        k: v
        for k, v in element.__dict__.items()
        if k[0] != "_"
    }
