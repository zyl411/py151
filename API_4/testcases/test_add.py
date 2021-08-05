
import unittest

from ddt import ddt, data

from API_4.common import contants
from API_4.common import do_excel
from API_4.common.http_request import HTTPRequest2
from API_4.common.config import config
from API_4.common import context



@ddt
class AddTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'add')
    cases = excel.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.http_request = HTTPRequest2()

    @data(*cases)
    def test_add(self, case):
        case.data=eval(case.data)
        if case.data.__contains__('mobile_phone') and case.data['mobile_phone']=='normal_user':
            case.data['mobile_phone']=config.get('data','normal_user')

        if case.data.__contains__('pwd') and case.data['pwd']=='normal_pwd':
            case.data['pwd']=config.get('data','normal_pwd')

        if case.data.__contains__('memberId') and case.data['memberId']=='loan_member_id':
            case.data['memberId']=config.get('data','loan_member_id')

        resp = self.http_request.request(case.method, case.url, case.data)
        # case.data = context.replace(case.data)

        try:
            self.assertEqual(str(case.expected),resp.json()['code'])
            # self.assertEqual(str(case.expected), resp.json()['code'])

            self.excel.write_result(case.case_id + 1, resp.text, 'PASS')
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1, resp.text, 'FAIL')
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
