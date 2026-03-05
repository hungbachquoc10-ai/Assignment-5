import re
def interactive_sum():
    while True:
        text = input("Enter your paragraph(exit to quit): ")
        if text.lower() == 'exit':
            break
        x = re.findall(r"d+", text)
        total = sum([int(n) for n in x])
        print(f"{total}")

interactive_sum()
