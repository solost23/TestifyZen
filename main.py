import unittest

from config.config import read_config
from service.email import send

from BeautifulReport import BeautifulReport


class TestSample(unittest.TestCase):
    def test_one(self):
        self.assertEqual(1, 1, '1 不等于 1')

    def test_two(self):
        self.assertNotEqual(1, 2, '1 等于 2')

    def test_three(self):
        self.assertTrue(False, '这不是一个真值')


if __name__ == '__main__':
    # 生成测试报告并写入文件
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSample)
    report = BeautifulReport(suite)
    report.report(report_dir='./report', description='')

    send(read_config(), report.title, "测试报告", [f'{report.report_dir}/{report.filename}'])

