from sqlalchemy.orm import DeclarativeBase, declared_attr

from notelink.tools.case_converter import camel_case_to_snake_case


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(self) -> str:
        return f"{camel_case_to_snake_case(self.__name__)}s"
