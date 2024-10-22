class AnonySurvey:
    """ This class takes survey of anonymous person to learn what language they
    wanna learn first."""
    def __init__(self, question):
        self.question = question
        self.responses = []
    def show_questions(self):
        print(self.question)
    def store_responses(self, new_response):
        self.responses.append(new_response)
    def show_responses(self):
        for response in self.responses:
            print(f"-{response}")
            