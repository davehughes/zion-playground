import flask

from zion_playground import zion, demos

app = flask.Flask(__name__)

@app.route('/')
def main():
    program = HELLO_WORLD
    return flask.render_template('playground.html', **{
        'program': program,
        })

@app.route('/rpc/run', methods=['POST'])
def rpc_run():
    program = flask.request.values.get('program')
    output = zion.run(program)
    errors = 'TODO'
    return flask.jsonify({
        'program': program,
        'output': output,
        'errors': errors,
        })

@app.route('/rpc/fmt', methods=['POST'])
def rpc_fmt():
    program = flask.request.values.get('program')
    output = zion.fmt(program)
    errors = 'TODO'
    return flask.jsonify({
        'program': program,
        'formatted': output,
        'errors': errors,
        })

@app.route('/demos')
def demo_list():
    return flask.render_template("demos.html", **{
        "demos": demos.DEMOS,
        })

@app.route('/demos/<slug>')
def demo_detail(slug):
    demo = {d['slug']: d for d in demos.DEMOS}.get(slug)
    if not demo:
        flask.abort(404)

    return flask.render_template('playground.html', **{
        'program': demo['program'],
        })
