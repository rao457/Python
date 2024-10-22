### this program is gonna start survey of anonymous to know them
class AnonymousSurvey:
    """ Let's take survey and unveil anonymous"""
    def __init__(self, *args):
        self.args = args
        self.responses = []
    def show_question(self):
        print("You have to Answer following questions.")
        for index,arg in enumerate(self.args, start=1):
            print(f"{index} - {arg}")
    def anonymous_responses(self, *new_response):
        self.responses.append(new_response)
    def show_responses(self):
        for index,response in enumerate(self.responses, start=1):
            print(f"{index} - {response}\n")
anonymous_1 = AnonymousSurvey('What is Your name?', 'How old You are?', 'What is your religion?', 'In which country do you live?', 'Why did you come here?')
anonymous_1.show_question()
anonymous_1.anonymous_responses("Zohaib",20,'Islam', 'Pakistan', 'To Visit' )
anonymous_1.show_responses()            