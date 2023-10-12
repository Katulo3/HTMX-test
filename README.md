# Scripts principales

1. Instalar dependencias Python (ver pyproject.toml)
   - `pdm install`
  
2. Instalar dependencias Node (ver package.json)
   - `npm install`

3. Ejecutar servidor mkdocs para la documentación:
   - Ejecutar: `pdm docs`
   - Abrir `localhost:7000`

4. Ejecutar servidor Django del proyecto:
   - Ejecutar: `pdm server`
   - Abrir `localhost:8000`

## Más scripts para PDM

cov: `pytest project --cov=project --cov-report=html`

cov-view: `htmlcov\\index.html`

docs: `mkdocs serve -a localhost:7000 -f ./project/mkdocs.yml`

format: `black project`

indent: `djhtml project -t 4`

linter: `ruff project`

makemigrations: `project/manage.py makemigrations`

migrate: `project/manage.py migrate`

createsuperuser: `python project/manage.py createsuperuser --username='admin' --email='ioseph.dev@gmail.com'`

server: `project/manage.py runserver`

test: `pytest project`

tail: `npx tailwindcss -i project/staticfiles/css/input.css -o project/staticfiles/css/output.css --watch`

## Superusuario

admin: 123
