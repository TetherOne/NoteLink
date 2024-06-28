from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column

from notelink.utils.case_converter import camel_case_to_snake_case


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(self) -> str:
        return f"{camel_case_to_snake_case(self.__name__)}s"

    id: Mapped[int] = mapped_column(primary_key=True)
