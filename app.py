#!flask/bin/python

from flask import Flask, jsonify
from flask import abort
from flask import request
from flask import make_response
import configuration


app=Flask(__name__)

from service import get_configs, get_all_configs, add_config, remove_config, update_config_by_name, search_by_query


#method to GET all the configs
@app.route('/configs', methods=['GET'])
def get_all():
    return jsonify({'configs': get_all_configs()})

#method to GET data for specific config
@app.route('/configs/<name>', methods=['GET'])
def get_by_name(name):
    config = get_configs(name)
    if len(config) == 0:
        abort(404)
    return jsonify({'config': config[0]})

#method to GET data in application/json format
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

#method for POST call
@app.route('/configs', methods=['POST'])
def create_config():
    if not request.json or not 'name' in request.json:
        abort(400)

    new_config = add_config(request.json.get('name', ""), request.json.get('metadata').get('monitoring').get('enabled'), request.json.get('metadata').get('limits').get('cpu').get('enabled'))
    return jsonify({'config': new_config}), 201

#method to PUT/PATCH changes in config
@app.route('/configs/<name>', methods=['PUT'])
def update_config(name):
    if len(get_configs(name)) == 0:
        return make_response(jsonify({'error': 'Not found'}), 404)
    updated_config = update_config_by_name(name, request.json),
    return jsonify({'config': updated_config}), 200


#method to DELETE a specific config
@app.route('/configs/<name>', methods=['DELETE'])
def delete_config(name):
    if len(name) == 0:
        abort(404)
    result= remove_config(name)
    return jsonify({'result': result})

#method to QUERY specific config
@app.route('/search', methods=['GET'])
def get_query_configs():
    query_string = request.query_string.split("=")
    configs = search_by_query(query_string[0], query_string[1])
    return jsonify({'config': configs})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=configuration.PORT, debug=configuration.DEBUG_MODE)




