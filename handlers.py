import json

import flask
from werkzeug.exceptions import BadRequest
from consts import HTTP_CODE_BAD_REQUEST
from jsonschema import validate, ValidationError
from service_layler import processing, AlreadyExistException, OneLessThatItWasException
import config


blueprint = flask.Blueprint('api', __name__)


@blueprint.route('/increment', methods=['POST'])
def increment():
    try:
        request = flask.request.get_json()
    except BadRequest as e:
        flask.current_app.logger.warn(str(e))
        return flask.jsonify({'error': str(e), 'type': 3}), HTTP_CODE_BAD_REQUEST

    with open(config.JSONSCHEMA_PATH, 'r') as schema:
        try:
            validate(request, json.load(schema))
        except ValidationError as e:
            flask.current_app.logger.warn(str(e))
            return flask.jsonify({'error': str(e), 'type': 3}), HTTP_CODE_BAD_REQUEST

    number = request.get('number')

    try:
        result = processing(flask.current_app.redis, number)
    except (AlreadyExistException, OneLessThatItWasException) as e:
        flask.current_app.logger.warn(str(e))
        return flask.jsonify({'error': str(e), 'type': e.code}), HTTP_CODE_BAD_REQUEST

    return flask.jsonify({'result': result})


@blueprint.route('/_info', methods=['GET'])
def info():
    return flask.jsonify({'result': 'ok'})
