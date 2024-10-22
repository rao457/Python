users = ['Admin', 'zohaib', 'syed noor hussain', 'shoaib']
new = ['Sonia', 'Zohaib', 'zubair', 'sajjad', 'saifi']
for user in new:
    if user in users:
        print(f"{user} username already exists.")
    else:
        print(f"{user} username is available")
    
# if users:
#     for user in users:
#         if user == 'syed noor hussain':
#             print(f"\nI Love You sir, by the way thanks for joining.")
#         else:
#             print(f"Hello {user}, thanks for joining again.")
# else:
#     print("We need to find some users.")