from questionnaire.survey import AnonymousSurvey

# 定义一个问题, 并创建一个表示调查的AnonymousSurvey对象
question = '你想首先学习哪种外语?'
my_survey = AnonymousSurvey(question)

# 显示问题并存储答案
my_survey.show_question()
print("'q'键退出")
while 1:
    response = input("语言: ")
    if response == "q":
        break
    my_survey.store_response(response)

    # 显示结果
    print("\n感谢接受我们的调查!")
    my_survey.show_results()
