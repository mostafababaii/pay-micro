.PHONY: build migrate-auth migrate-notification

run:
	docker compose up -d

migrate-auth:
	docker compose exec -it auth python manage.py migrate

migrate-notification:
	docker compose exec -it notification python manage.py migrate
