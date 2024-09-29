def get_response(user_input) -> str:
    lowered = user_input.lower()

    if lowered == '':
        return "You don't tlak much do you?"
    else:
        return f'You said {user_input}'
