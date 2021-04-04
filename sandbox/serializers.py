from pydantic_sqlalchemy import sqlalchemy_to_pydantic


def serialize(content, as_list=False):
    if as_list and not content:
        return []

    orm_model = content[0] if as_list else content
    serializer = sqlalchemy_to_pydantic(orm_model.__class__)

    if as_list:
        return [
            serializer.from_orm(element).dict()
            for element in content
        ]
    else:
        return serializer.from_orm(content).dict()
