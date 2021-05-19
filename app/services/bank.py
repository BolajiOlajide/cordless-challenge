import requests
from flask import jsonify

from config import BANK_BASE_API_URL

class Bank:
    @staticmethod
    def lookup_customer_by_phone(phone_number):
        customer_info = None
        url = f"{BANK_BASE_API_URL}/customers?phone={phone_number}"
        response = requests.get(url)
        if response.ok:
            json = response.json()
            customer_info = json['customer']

        if customer_info is None:
            return jsonify({"error": "Customer with the phone number doesnt exist."}), 404

        return jsonify(dict(customer=customer_info)), 201
