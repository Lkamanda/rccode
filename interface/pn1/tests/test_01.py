import unittest
from interface.pn1.base.method import Method, IsAssert


class LaGou(unittest.TestCase):
    def setUp(self):
        self.obj = Method()
        self.p = IsAssert()

    def statusCode(self, r):
        # 判断协议状态码是否为零
        self.assertEqual(r.status_code, 200)
        # 判断特定返回参数是否和预期一致
        # self.assertEqual(r.json()['code'], 0)

    def test_la_gou_001(self):
        """拉钩:测试翻页"""
        # 执行excal中的第一条测试用例
        r = self.obj.post(1)
        # 获取请求状态码
        #print(r.status_code)
        # print(r.text)
        self .statusCode(r=r)
        # print(self.p.isContent(row=
        self.assertTrue(self.p.isContent(row=1))


if __name__ == '__main__':
    unittest.main(verbosity=2)

