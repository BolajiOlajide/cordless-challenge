import logging

from flask import jsonify

from app.services.bank import Bank
from app.services.recording import Recording


logger = logging.getLogger()

class Ivr:
    @staticmethod
    def customer_lookup(payload):
        try:
            phone_number = payload['phone_number_from']
            customer_info = Bank.lookup_customer_by_phone(phone_number)

            if customer_info is None:
                return jsonify({"error": "Customer with the phone number doesnt exist."}), 404

            return jsonify(dict(customer=customer_info)), 201
        except:
            error = "An error occurred while looking up customer by phone number."
            logger.error(error)
            return jsonify(dict(error=error)), 400

    @staticmethod
    def process_voicemail(payload):
        try:
            transcript = None
            is_ticket_created = False
            recording_url = payload["recording_url"]
            phone_number = payload['phone_number_from']

            if recording_url:
                transcript = Recording.transcribe(recording_url)

            if transcript:
                is_ticket_created = Bank.create_non_urgent_ticket(phone_number, recording_url, transcript)
            else:
                customer_id = None
                customer_info = Bank.lookup_customer_by_phone(phone_number)

                if customer_info:
                    customer_id = customer_info["id"]

                is_ticket_created = Bank.create_urgent_ticket(phone_number, customer_id)

            return jsonify(dict(message="Ticket has been succesfully created.")), 201
        except:
            error = "An error occurred while processing the voicemail."
            logger.error(error)
            return jsonify(dict(error=error)), 400
