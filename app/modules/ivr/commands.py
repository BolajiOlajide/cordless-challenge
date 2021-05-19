from app.services.ivr import Ivr

ivr_commands = {
    1: Ivr.customer_lookup,
    2: Ivr.process_voicemail
}
