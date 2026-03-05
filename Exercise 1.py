import re
def valid_course(text):
    str = r"^[A-Z]{2,3}\d{3}$"
    x = re.findall(str, text)
    return bool(x)
test_input = input("Enter your University course code: ")
is_valid = valid_course(test_input)
print(f" {is_valid}")