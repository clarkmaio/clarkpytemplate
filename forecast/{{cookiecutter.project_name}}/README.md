# {{cookiecutter.project_name}}

## Requirements
Install required packages with the command:

```
cd {{cookiecutter.project_name}}
pip install -r requirements.txt
```

## Template structure

The entry point should always be `__main__.py` in `src`.

Use `conf/parser.yml` to control parser arguments.
Use `conf/config.yml` for global variables.
Use `conf/catalog.yml` to map dataset to a key toghether with the file type in order to easily load file using `DataCatalog` class