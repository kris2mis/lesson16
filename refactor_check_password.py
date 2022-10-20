# ПОСЛЕ РЕФАКТЕРИНГА

import string

password = "12345rtye"


def check_password(password):
    # fool-proof
    if (not isinstance(password, str)
            or len(password.strip()) == 0):
        return -1

    password = password.strip()
    digit = string.digits
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase

    # logic
    if len(password) < 8:
        return "too weak"

    # weak
    is_digit = True
    if (all(ch in digit for ch in password)
            or all(ch in lower for ch in password)
            or all(ch in upper for ch in password)):
        return "weak"

    # very strong
    if (any(ch in digit for ch in password)
            and any(ch in lower for ch in password)
            and any(ch in upper for ch in password)):
        return "very strong"

    return "strong"


if __name__ == "__main__":
    assert check_password("") == -1
    assert check_password(" ") == -1
    # assert check_password("!@#$%^&") == -1
    assert check_password(None) == -1
    assert check_password(10) == -1
    assert check_password(10.5) == -1
    assert check_password([1, 2, 3]) == -1

    assert check_password("qwertyu") == "too weak"
    assert check_password("1234567") == "too weak"
    assert check_password("QWERTYU") == "too weak"
    assert check_password("YU344jt") == "too weak"
    assert check_password("t") == "too weak"

    assert check_password("12345678") == "weak"
    assert check_password("123456789") == "weak"
    assert check_password("QWERTYUI") == "weak"
    assert check_password("QWERTYUIOP") == "weak"
    assert check_password("qwertyui") == "weak"
    assert check_password("sekdjfhgkdfgjn") == "weak"

    assert check_password("QWE123rt") == "very strong"
    assert check_password("123QWE123rtryoirtt") == "very strong"

    assert check_password("1234RTYU") == "strong"
    assert check_password("123456789QWERTYUI") == "strong"
    assert check_password("QWERqwer") == "strong"
    assert check_password("QWERTYUIOPqwertyui") == "strong"
    assert check_password("qwer1234") == "strong"
    assert check_password("sekdjfhgk1223356") == "strong"