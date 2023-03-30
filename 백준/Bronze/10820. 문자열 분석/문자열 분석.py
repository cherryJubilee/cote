while True:
    try:
        text = input()
        lower = sum(i.islower() for i in text)
        upper = sum(i.isupper() for i in text)
        number = sum(i.isdigit() for i in text)
        blank = sum(i.isspace() for i in text)
        print(lower, upper, number, blank)

    except EOFError:
        break