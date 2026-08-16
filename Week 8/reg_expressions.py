import re
def find_digits(a_str):
    for match in re.findall("\d", a_str):
        print(match)

def main():
    a_str = "01abc02def03ghi"
    find_digits(a_str)

if __name__ == "__main__":
    main()