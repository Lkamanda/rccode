import unittest
from interface.pn1.base.method import Method, IsAssert
from interface.pn1.page.lagou import *
from interface.pn1.utils.public import *


class LaGou(unittest.TestCase):
    def setUp(self):
        self.obj = Method()
        self.p = IsAssert()

    def statusCode(self, r):
        # 判断协议状态码是否为零
        self.assertEqual(r.status_code, 200)
        # 判断特定返回参数是否和预期一致
        # self.assertEqual(r.json()['code'], 0)

    def isContent(self, r, row):
        # 对测试用例常用不骤进行重构
        self.statusCode(r=r)
        self.assertTrue(self.p.isContent(row=row))

    def test_la_gou_001(self):
        """拉钩:测试翻页"""
        # 执行excal中的第一条测试用例
        r = self.obj.post(1)
        self.isContent(r, row=1)
        # 获取请求状态码
        # print(r.status_code)
        # print(r.text)
        # self .statusCode(r=r)
        # print(self.p.isContent(row=
        # self.assertTrue(self.p.isContent(row=1))

    def test_la_gou_002(self):
        """模拟不同页数解决方法"""
        # 1.发送请求
        r = self.obj.post(2)
        # 2.增加断言
        self.isContent(r=r, row=2)
        # self.statusCode(r=r)
        # self.assertTrue(self.p.isContent(row=2))

    def test_lagou_003(self):
        """解决动态参数问题"""
        kd_list = ['自动化', '功能', '性能', '理论']
        for kd in kd_list:
            r = self.obj.post2(row=2, data=setSo(kd))
            self.isContent(r=r, row=2)

    def test_la_go_04(self):
        """
        1.请求搜索
        2.搜索成功,服务端返回数据
        3.拿待返回数据中的职位ID
        4.然后把职位ID当作参数一样传到职位详情
        """
        r = self.obj.post2(row=1, data=setSo('测试'))
        positionId_list = []
        for i in range(1, 15):
            positionId = r.json()['content'][i]['postionId']
            positionId_list.append(positionId)
        # 现将list类型序列化在写入文件中
        write_PositionId(json.dumps(positionId_list))

    def test_la_go_05(self):
        """解决动态参数"""
        for item in range(15):
            r = self.obj.get(url=getUrl()[item])
            print(r.text)
            self.assertTrue(self.isContent(row=2, r=r.text))
            break


if __name__ == '__main__':
    unittest.main(verbosity=2)

