# программа надежность пароля
# conditions
# 1.   len <8  - too weakr
# 2. 2345678  or QWERTY  or wertyu - weak
# 3. 2345 and WERTY and werty or QWERT and qwer
# 4.  2345 and QWERT and qwerty - very strong


def reliability_password():
    pass


main ():




if __name__ == "__main__":
    assert get_feedback("10") == -1
    assert get_feedback(7.5) == -1
    assert get_feedback(True) == -1
    assert get_feedback(None) == -1
    assert get_feedback([1,2,3]) == -1
    assert get_feedback(20) == -1
    assert get_feedback(-20) == -1
    assert get_feedback(0) == BAD_MARK
    assert get_feedback(-1) == -1
    assert get_feedback(10) == EXELLENT_MARK

    assert get_feedback(1) == BAD_MARK
    assert get_feedback(2) == "unsatisfactory"
    assert get_feedback(3) == "unsatisfactory"
    assert get_feedback(4) == "satisfactory"
    assert get_feedback(5) == "you could better"
    assert get_feedback(6) == "you could better"
    assert get_feedback(7) == "good"
    assert get_feedback(8) == "good"
    assert get_feedback(9) == "Excellent!"
