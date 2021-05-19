from flask import request, jsonify

from . import ivr_blueprint
from .commands import ivr_commands


@ivr_blueprint.route('', methods=['POST', 'OPTIONS'])
def ivr():
    phone_number = request.json['phone_number_from']
    digit = request.json['digit']

    if digit in ivr_commands:
        command_to_execute = ivr_commands[digit]
        return command_to_execute(phone_number)

    return jsonify({ "error": "Command for the digit provided doesn't exist." }), 400
