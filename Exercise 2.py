import re
def hex_color():
    pattern = r"^#[0-9A-Fa-f]{6}$"
    while True:
        str = input("Enter a hex color code(exit to quit): ")
        if str.lower() == 'exit':
            break
        x = re.findall(pattern, str)
        if bool(x):
            print("The given string is a valid hex color.")
        else:
            print("The given string is NOT a valid hex color.")
hex_color()