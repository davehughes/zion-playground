.PHONY: bootstrap
bootstrap:
	virtualenv env
	env/bin/pip install -r requirements.txt

.PHONY: serve
serve:
	FLASK_APP=zion_playground/app.py \
	FLASK_DEBUG=1 \
	env/bin/flask run
