# endpoint.py
# Handles endpoint deployment tasks: JWT and communication objects

import util

# Main handler functions
def handle_endpoint_in(data: dict):
    payload_type = data.get("payload_type")

    if payload_type:

        match payload_type:
            case "enc_key":
                if util.check_keys_in_dict(["type", "name", "value"], data):
                    pass
                return 400,{"message": "Missing one or more required keys: type, name, value"}
            case _:
                return 400,{"message": "Invalid payload type."}

    else:
        return 400,{"message": "Missing payload type."}
    
