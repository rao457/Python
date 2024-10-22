import unittest
from Code_To_Test import *
from AnonymousAgain import *

class TestMyCode(unittest.TestCase):
    """ This class is gonna test my code"""
    def test_first_last(self):
        """ Does name('roa', 'zohaib') return 'Rao Zohaib'?"""
        formate_name = name('Rao', 'Zohaib')
        self.assertEqual(formate_name, 'Rao Zohaib')
    def test_city_country(self):
        """ Does city_country(karachi, pakistan) return "Karachi, Pakistan?"""
        my_formate = cities('karachi', 'pakistan')
        self.assertEqual(my_formate, 'Karachi, Pakistan')
    
    question = 'Which language you wanna learn first? '
    my_survey = AnonySurvey(question)
    my_survey.show_questions()
    print("press q any time to quit: ")
    while True:
            response = input("Language: ")
            if response == 'q':
                 break
            my_survey.store_responses(response)
    def test_store_single_response(self):
         """ Tests that single response is stored properly or not."""
         question = 'which language you wanna learn first? '
         my_survey = AnonySurvey(question)
         my_survey.store_responses("English")
         self.assertIn('English', my_survey.responses)

if __name__ == "__main__":
    unittest.main()
