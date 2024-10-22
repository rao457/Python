def get_names(first, last):
    full_name = f"{first} {last}"
    return full_name.title()
while True:
    print("Please tell me your name")
    print("Press q any time to quit")
    first = input("Enter First name: ")
    if first == 'q':
        break
    last = input("Enter Last name: ")
    if last == 'q':
        break
    formatted_name = get_names(first, last)
    print(f"Hello {formatted_name}!")
