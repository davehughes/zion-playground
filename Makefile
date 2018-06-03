PROJECT_ROOT = $(dir $(realpath $(firstword $(MAKEFILE_LIST))))
FLASK_APP ?= zion_playground/app.py
FLASK_DEBUG ?= 0
FLASK_PORT ?= 5000
FLASK_HOST ?= 127.0.0.1
FLASK_PORT_LOCAL ?= 5000

.PHONY: bootstrap
bootstrap:
	virtualenv env
	env/bin/pip install -r requirements.txt
	virtualenv --relocatable env

.PHONY: serve
serve:
	FLASK_APP=$(FLASK_APP) \
	FLASK_DEBUG=$(FLASK_DEBUG) \
	env/bin/flask run --port $(FLASK_PORT) --host $(FLASK_HOST)

.PHONY: docker-build
docker-build:
	docker build \
		--tag zion-playground:latest \
		--file docker/Dockerfile \
		.

.PHONY: docker-run
docker-run:
	docker run -it \
		--publish $(FLASK_PORT_LOCAL):$(FLASK_PORT) \
		zion-playground:latest

.PHONY: docker-dev-build
docker-dev-build:
	docker build \
		--tag zion-playground:dev \
		--file docker/Dockerfile.dev \
		.

.PHONY: docker-dev-run
docker-dev-run: docker-dev-build
	virtualenv --relocatable env
	docker run -it \
		--mount type=bind,source=$(PROJECT_ROOT),target=/opt/zion-playground \
		--publish $(FLASK_PORT_LOCAL):$(FLASK_PORT) \
		zion-playground:dev

.PHONY: clean
clean:
	rm -rf **/*.pyc
