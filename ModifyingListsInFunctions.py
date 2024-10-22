# We can give all members of a list to a new list with a very efficient way like this
remaining_skills = ['nmap', 'wireshark', 'Hydra', 'hashcat']
learned_skills = []
while remaining_skills:
    current_skill = remaining_skills.pop()
    print(f"learning_skills: {current_skill}")
    learned_skills.append(current_skill)
print("Following Skills are learned.")
for learned_skill in learned_skills:
    print(f"Learnt_skil: {current_skill}")  
# Doing this in the function
def print_design():
    
    while remaining_skills:
        current_skill = remaining_skills.pop()
        
        
        learned_skill.append(current_skill)
        print(f"Learning Skill: {current_skill}")    
def completed_skills():
    for learned_skill in learned_skills:
        print(f"Learnt Skill: {learned_skill}")
print_design()
completed_skills()  