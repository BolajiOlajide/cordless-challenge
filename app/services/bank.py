from datetime import datetime

import requests

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

        return customer_info

    @staticmethod
    def create_urgent_ticket(phone_number, customer_id = None):
        url = f"{BANK_BASE_API_URL}/urgent-tickets"
        data = {
            "phone_number_from": phone_number,
            "time_of_call": datetime.now().strftime("%H:%M:%S")
        }

        if customer_id:
            data["customer_id"] = customer_id

        response = requests.post(url=url, data=data)

        if response.ok:
            return True

        return False

    @staticmethod
    def create_non_urgent_ticket(phone_number, recording_url, transcript):
        url = f"{BANK_BASE_API_URL}/urgent-tickets"
        data = {
            "phone_number_from": phone_number,
            "recording_url": recording_url,
            "transcript": transcript
        }

        response = requests.post(url=url, data=data)

        if response.ok:
            return True

        return False

