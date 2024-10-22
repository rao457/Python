# This program writes personal information of user in the file
def Take_Write_Info(filename):
    """ This method will take user info and write it to a file."""
    Formatted_info = ''
    while True:

        print("***Press q any time to quit***")
        Name = input("Enter Your Name (In Alphabets): ")
        Age = input("Enter Your Age (In integers): ")
        if Name == 'q' or Age == 'q':
            break
        
        
        
        else:
            with open(filename, 'w') as file_object:
                Formatted_info += f"Name : {Name}\nAge : {Age}\n"
                file_object.write(Formatted_info)
# Calling the Function
Take_Write_Info("Personal_info.txt")

