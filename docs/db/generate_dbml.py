from os import system
from typing import Final


def export_db_description() -> None:
    with open('./db_description.md') as f:
        md: list[str] = f.readlines()

    proj: Final[str] = 'Project VMAP'
    db_type: Final[str] = 'database_type'
    db: Final[str] = 'PostgreSQL'
    otpt: Final[str] = ''.join(md)

    struct: Final[str] = f"{proj} {{\n\t{db_type}: '{db}'\n\tNote: '''{otpt}'''}}\n\n"

    with open('schema.dbml', 'w') as f:
        f.write(
            '// Docs: https://dbml.dbdiagram.io/docs\n\n'
        )

        f.write(struct)


def export_tables() -> None:
    with open('_schema.dbml') as f:
        schema: list[str] = f.readlines()

    with open('schema.dbml', 'a') as f:
        f.writelines(schema)


def generate_docs() -> None:
    system('dbdocs build schema.dbml --project VMAP')


def main() -> None:
    export_db_description()
    export_tables()
    generate_docs()


if __name__ == '__main__':
    main()
