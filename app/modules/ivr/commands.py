from app.services.bank import Bank

ivr_commands = {
    1: Bank.lookup_customer_by_phone
}
