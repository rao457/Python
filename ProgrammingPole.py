# This program is related to the polling for the people that why they like 
# programming
message = ''
while True:
    print("***Press Q any time to quit polling***")
    Poller_name = input("Enter Your name: ")
    Poll = input("Why do you like programming: ")
    if Poller_name == 'q' or Poll == 'q':
        break
    else: 
        with open("Poll.txt", 'w') as f:
            message += f"I am {Poller_name}:\n and I do programming because of {Poll}\n"
            f.write(message)
        
