# ========================================== *
# 							  Makefile help							 *
# ========================================== *

define USAGE

Small Billing/invoicing app
______________________________________________________

Commands:

	Base:
	______________________________________________
	Docker:
	build           : Build Docker image
	run             : Run Docker image
	destroy_empty   : Destroy empty docker images
	______________________________________________
endef

export USAGE

# ============================= *
# 						Utils 						*
# ============================= *

help:
	@echo "$$USAGE"

# ============================================ *
# 						Django specific tasks						 *
# ============================================ *

clean_up:
	@echo ""
	@echo "Cleaning Cache and DB"
	@echo ""
	@sleep .5
	find . | grep -E '/(__pycache__|\.pyc|\.pyo$/)' | xargs rm -rf
	rm -rf db.sqlite3
	@echo ""

dummy_db:
	@echo ""
	@echo "Rebuilding the database with dummy data"
	@echo ""
	./manage.py makemigrations
	./manage.py migrate
	./manage.py loaddata fixtures/*
	@echo ""

rebuild: clean_up dummy_db

linter:
	@flake8 . --exit-zero --ignore E501,F401 --exclude .git,venv > linter-todo.md

# ============================================ *
# 						Docker specific tasks						 *
# ============================================ *

destroy_empty:
	docker rmi $$(docker images --filter "dangling=true" -q --no-trunc)
