.PHONY: venv
venv:
	@bash bin/create_venv.sh

.PHONY: api
api:
	python -m src.app.main