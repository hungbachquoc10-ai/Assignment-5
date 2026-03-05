import re
def privacy_tool():
    user = input("Enter the document text here: \n")
    pattern = r"\+84\d+|\b\d{10}\b"
    text = re.sub(pattern, "[REDACTED]", user)
    print(text)
privacy_tool()