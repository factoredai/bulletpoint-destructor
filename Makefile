.PHONY: venv
venv:
	@bash bin/create_venv.sh

.PHONY: api
api:
	python -m src.app.backend.main

.PHONY: frontend
frontend:
	python -m streamlit run src/app/frontend/streamlit_app.py