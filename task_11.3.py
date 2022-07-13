class All_nums(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


if __name__ == "__main__":

    lst = []
    while True:
        try:
            inp = input()
            if inp == "stop":
                break
            elif not inp.isdigit():
                raise All_nums()
            else:
                lst.append(int(inp))
        except All_nums:
            print("You have input not a number")

    print(*lst)