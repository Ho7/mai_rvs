import json

import flask
from werkzeug.exceptions import BadRequest
from consts import HTTP_CODE_BAD_REQUEST
from jsonschema import validate, ValidationError
from service_layler import processing
import config


blueprint = flask.Blueprint('api', __name__)


@blueprint.route('/increment', methods=['POST'])
def increment():
    try:
        request = flask.request.get_json()
    except BadRequest as e:
        flask.current_app.logger.warn(str(e))
        return flask.jsonify({'error': str(e)}), HTTP_CODE_BAD_REQUEST

    with open(config.JSONSCHEMA_PATH, 'r') as schema:
        try:
            validate(request, json.load(schema))
        except ValidationError as e:
            flask.current_app.logger.warn(str(e))
            return flask.jsonify({'error': str(e)}), HTTP_CODE_BAD_REQUEST

    number = request.get('number')

    try:
        result = processing(flask.current_app.redis, number)
    except Exception as e:
        flask.current_app.logger.warn(str(e))
        return flask.jsonify({'error': str(e)}, HTTP_CODE_BAD_REQUEST)

    return flask.jsonify({'result': result})
