freeze:
	@poetry export --without-hashes --format=requirements.txt > requirements.txt

run:
	@cd project && python manage.py runserver localhost:57424

mig:
	@cd project && python manage.py makemigrations
	@cd project && python manage.py migrate

su:
	@cd project && python manage.py createsuperuser
