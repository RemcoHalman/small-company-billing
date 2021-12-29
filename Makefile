# ================================================================== *
# 							  Makefile help							 *
# ================================================================== *

define USAGE

Small Billing/invoicing app
_____________________________________________________

Commands:

	Base:
	_____________________________________________
	Docker:
	build           : Build Docker image
	run             : Run Docker image
	destroy_empty   : Destroy empty docker images
	_____________________________________________
endef

export USAGE

# ========================================== *
# 							Docker Variables						 *
# ========================================== *

PREFIX=remcoha
APP_NAME=billingsystem
IMG_REGISTRY=docker.io/$(PREFIX)
VERSION=0.0.1
LOCAL_PORT=8000
EXPOSE_PORT=3250
IMG_NAME=$(IMG_REGISTRY)/$(APP_NAME):$(VERSION)

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

# ============================================ *
# 						Docker specific tasks						 *
# ============================================ *

build:
	docker build -t $(IMG_NAME) .

run:
	docker run -d -p $(EXPOSE_PORT):$(LOCAL_PORT) $(IMG_NAME)

buildrun: build run

stats:
	@docker ps --format 'CONTAINER ID : {{.ID}} | Name: {{.Names}} | Image:  {{.Image}} |  Ports: {{.Ports}}'

stop: ## Stop and remove a running container
	docker stop $$(docker ps -q --filter ancestor=$(PREFIX)/$(APP_NAME):$(VERSION) --format="{{.ID}}" )

destroy_empty:
	docker rmi $$(docker images --filter "dangling=true" -q --no-trunc)
