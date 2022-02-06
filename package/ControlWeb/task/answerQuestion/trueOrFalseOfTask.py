# -*- encoding = utf-8 -*-
# @Time : 2022-02-06 22:28
# @Author : Levitan
# @File : trueOrFalseOfTask.py
# @Software : PyCharm

from package.ControlWeb.Spider.questionType import TrueOrFalse

class TrueOrFalseOfTask(TrueOrFalse):
    def __init__(self, qType, question, answer, answerWebElementList):
        """
        :param qType: 题目类型（单选题，多选题）
        :param question: 题目问题
        :param answer: 查找到的题目答案
        :param answerWebElementList: 题目选项的WebElement对象， 列表类型
        """
        super(TrueOrFalseOfTask, self).__init__(qType, question, answer)
        self.__answerWebElementList = answerWebElementList

    def getAnswerWebElement(self):
        """
        :return: 返回正确答案的WebElement对象
        """
        answer = self.getAnswer()[0]
        index = 0 if answer else 1
        return [self.__answerWebElementList[index]]