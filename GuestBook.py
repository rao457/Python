# this program is basically helps in keeping the note of guests which arrive to your party.
message = ''
while True:

    guest_name = input("Enter Your name or q any time to quit: ")
    if guest_name == 'q':
        break
    else:
        with open("Guest.txt", 'a') as f:
            message += f"Hello {guest_name}! I am Happy you came here.\n"
            f.write(message)
print(message)