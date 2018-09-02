def show_message(message, border="-"):
    line = border * len(message)
    print(line)
    print(message)
    print(line)


def show_menu(menu=[]):
    menu.append("spam")
    print(menu)


def show_menu_alt(menu=None):
    if menu is None:
        menu = []
    menu.append("spam")
    print(menu)


if __name__ == "__main__":
    # show_message("This is Rita")
    # show_message("This is Rita", "*")
    # show_message("This is Rita", border="*")
    # show_message(border="*", message="This is Rita")
    lunch = ["rice"]
    show_menu_alt(lunch)
    show_menu_alt()
    show_menu_alt()
