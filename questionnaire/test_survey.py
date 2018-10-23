import unittest
from questionnaire.survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    '''测试AnonymousSurvey类'''

    def test_store_single_response(self):
        '''测试单个答案是否会被保存'''
        question = '你想首先学习哪种外语?'
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('英语')

        self.assertIn('英语', my_survey.responses)

    def test_store_many_response(self):
        '''测试多个答案是否会被保存'''
        question = '你想首先学习哪种外语?'
        my_survey = AnonymousSurvey(question)
        responses = ['英语', '法语', '西语']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)


if __name__ == '__main__':
    unittest.main()
