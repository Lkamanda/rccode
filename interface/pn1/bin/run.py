from interface.pn1.utils.operationExcal import OperationExcal
import os
import unittest


class Runner:
    def __init__(self):
        self.excal = OperationExcal()

    def getSuite(self):
        """获取执行测试套件"""
        suite = unittest.TestLoader().discover(
            start_dir=os.path.join(os.path.dirname(os.path.dirname(__file__))),
            pattern='test_*,py',
            top_level_dir=None
        )
        return suite

    def main_run(self):
        """批量执行所有的测试用例"""
        unittest.TextTestRunner().run(self.getSuite())
        content = '通过数:{0},失败数:{1},通过率{2} '.format(
            self.excal.run_success_result(),
            self.excal.run_fail_result(),
            self.excal.run_pass_rate()
        )
