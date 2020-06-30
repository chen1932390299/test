import unittest
import HTMLReport
from inspect import isfunction
import os
import time
from api.src.test_cases import ApiFrame
cur_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))


def raw_members(class_name: object):
    """ get all unsort members test_* name list eg it also work well : list(filter(lambda x: not x.startswith("__")
     and not x.endswith("__") and x.startswith("test_") ,TestHetero.__dict__.keys())) """

    return list(
        filter(lambda x: not x.startswith("__") and not x.endswith("__") and x.startswith("test_") and isfunction(
            eval(class_name.__name__ + ".%s" % x)) and callable(eval(class_name.__name__ + ".%s" % x)),
               class_name.__dict__.keys()))


def make_suite(class_name):
    suite = unittest.TestSuite()
    suite.addTests([class_name("%s" % value) for value in raw_members(class_name)])
    return suite


def original_order_suite(cls_name: object):
    """cls_name is TestClass Name,return test_* function suite by user write order not ascii order"""
    dict_items = list(
        filter(lambda x: not x[0].startswith("__") and x[0].startswith("test_"), cls_name.__dict__.items()))
    functions = [v for k, v in dict_items if isfunction(v)]
    suite = unittest.TestSuite()
    suite.addTests(functions)
    return suite


def runner_manager(class_name: object):
    """ the method that generate html report by user support unittest.classname """

    # 测试套件
    suite = make_suite(class_name)
    runner = HTMLReport.TestRunner(report_file_name=f"{cur_time}_report",  # 报告文件名，如果未赋值，将采用“test+时间戳”
                                   output_path=DEST,  # 保存文件夹名，默认“report”
                                   title='测试报告',  # 报告标题，默认“测试报告”
                                   description='无测试描述',  # 报告描述，默认“测试描述”
                                   thread_count=4,  # 并发线程数量（无序执行测试），默认数量 1
                                   thread_start_wait=3,  # 各线程启动延迟，默认 0 s
                                   sequential_execution=True,  # 是否按照套件添加(addTests)顺序执行，
                                   # 会等待一个addTests执行完成，再执行下一个，默认 False
                                   # 如果用例中存在 tearDownClass ，建议设置为True，
                                   # 否则 tearDownClass 将会在所有用例线程执行完后才会执行。
                                   # lang='en'
                                   lang='cn'  # 支持中文与英文，默认中文
                                   )
    # 执行测试用例套件
    runner.run(suite)



def runner_html(class_name: object):
    global DEST
    DEST = os.path.join(os.path.dirname(os.getcwd()), "report")
    runner_manager(class_name)


if __name__ == '__main__':
    runner_html(ApiFrame)
