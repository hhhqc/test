#主要是生成测试报告相关
import datetime
import unittest
import HTMLTestReportCN



#测试用例



#添加Suite
def Suite():
    #定义一个单元测试容器
    suiteTest = unittest.TestSuite()
    #将测试用例加入到容器
    suiteTest.addTest(MyTestCase("testCase1"))

    return suiteTest

'''
问题：代码写的没问题，执行也成功了，但就是无法生成HTMLTestRunner的报告
其实这是编辑器搞得鬼，编辑器为了方便用户执行测试，都有一项功能，可以用编辑器来调用unittest或者nose来执行测试用例，这种情况下，执行的只是用例或者套件，而不是整个文件，写在main里的代码是不会被执行的！！自然无法生成测试报告
我们在如果想要生成测试报告，那么一定要注意右键执行时选择的右键菜单，一定要当做文件执行，不要让编辑器当做用例执行
if __name__ == ‘__main__‘:
if __name__ == ‘python‘:
# 把main修改成自己的文件夹名就可以了
---试了不行
'''
if __name__ == '__main__':

    time = datetime.datetime.now().strftime('%Y-%m-%d')
    #确定生成报告的路径
    filePath ='../result/'+time+'HTMLTestReportCN.html'
    fp = open(filePath,'wb')
    #生成报告的Title,描述
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title='自动化测试报告',
        #description='详细测试用例结果',
        tester='Findyou'
        )
    #运行测试用例
    runner.run(Suite())
    # 关闭文件，否则会无法生成文件
    #fp.close()