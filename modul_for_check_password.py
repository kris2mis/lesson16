import check_password


def main():
    password = input("Input your password: ")

    result = check_password.check_password(password)

    msg = f"Your password is {result}" if isinstance(result, str) \
        else "User data invalid"

    print(msg)


if __name__ == "_main__":
    main()
