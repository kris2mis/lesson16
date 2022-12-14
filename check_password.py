# программа надежность пароля
# conditions
# 1.   len < 8  - too weak
# 2. 2345678  or QWERTY  or wertyu - weak
# 3. 2345 and WERTY and werty or QWERT and qwer - strong
# 4.  2345 and QWERT and qwerty - very strong

# ДО РЕФАКТЕРИНГА

DIGITS = "0123456789"
LOWER_CASE = "qwertyuiopasdfghjklzxcvbnm"
UPPER_CASE = "QWERTYUIOPASDFGHJKLZXCVBNM"


def check_password(password):
    # fool-proof
    if (not isinstance(password, str)
            or len(password.strip()) == 0):
        return -1

    password = password.strip()  # убрали все пробелы в пароле

    # logic
    if len(password) < 8:
        return "too weak"

    # проверка есть ли символ (ch) в DIGIT
    is_digit = True
    for ch in password:
        if ch not in DIGITS:
            is_digit = False
            break

    # проверка есть ли символ (ch) в LOWER_CASE
    is_lower = True
    for ch in password:
        if ch not in LOWER_CASE:
            is_lower = False
            break

    # проверка есть ли символ (ch) в UPPER_CASE
    is_upper = True
    for ch in password:
        if ch not in UPPER_CASE:
            is_upper = False
            break

    if is_upper or is_lower or is_digit:
        return "weak"

    # проверка на   very strong
    is_digit = False
    for ch in password:
        if ch in DIGITS:
            is_digit = True
            break

    is_lower = False
    for ch in password:
        if ch in LOWER_CASE:
            is_lower = True
            break

    is_upper = False
    for ch in password:
        if ch in UPPER_CASE:
            is_upper = True
            break

    if is_digit and is_lower and is_upper:
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
    assert check_password("123456789") == "weak"  # проверка граничного значения
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
