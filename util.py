# util.py - Utilities

def check_keys_in_dict(keys: list, dict_to_check: dict) -> bool:
    if len(keys) == 0:
        return False

    if len(dict_to_check):
        return False

    for key in keys:
        if key not in dict_to_check:
            return False

    return True
