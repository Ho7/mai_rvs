import flask
from werkzeug.exceptions import BadRequest
from consts import HTTP_CODE_BAD_REQUEST
from jsonschema import validate, ValidationError
from service_layler import check_number

app = flask.Flask(__name__)


@app.route('/increment', methods=['POST'])
def increment():
    try:
        request = flask.request.get_json()
    except BadRequest as e:
        app.logger.warn(str(e))
        return flask.abort(HTTP_CODE_BAD_REQUEST)

    try:
        validate(request, './jsonscheme/increment/request.json')
    except ValidationError as e:
        app.logger.warn(str(e))
        return flask.abort(HTTP_CODE_BAD_REQUEST, e)

    number = request.get('number')

    try:
        check_number(number, app.redis)
    except Exception as e:
        app.logger.warn(str(e))
        return flask.abort(HTTP_CODE_BAD_REQUEST, e)

    app.redis.set(number, True)

    return flask.jsonify({'result': number+1}, success=True)
