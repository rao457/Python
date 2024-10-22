import time
def connect():
    print('Connecting to Internet....')
    time.sleep(3)
    print('You are connected!')

connect()
persons: list[str] = ['zohaib', 'shoaib', 'Noor Hussain Shah', 'Muhammad Sajid']
long_name: list[str] = [person for person in persons if len(person)>= 7]
print(long_name)
      
      
      
      
      
      
      
      
      
      