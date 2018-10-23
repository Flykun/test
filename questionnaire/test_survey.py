import unittest
from questionnaire.survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    '''测试AnonymousSurvey类'''

    def setUp(self):
        '''创建一个调查对象和一组答案, 供使用的测试方法使用'''
        question = '你想首先学习哪种外语?'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['英语', '法语', '西语']

    def test_store_single_response(self):
        '''测试单个答案是否会被保存'''
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_many_response(self):
        '''测试多个答案是否会被保存'''

        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()
