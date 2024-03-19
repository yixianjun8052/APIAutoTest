from Common.handle_request import send_request
from Common.handle_log import logger


class TestLogin:
    def test_login(self, login_case_fixture):
        case = login_case_fixture
        logger.info(">>> 开始执行 {}：{}".format(case["case_id"], case["title"]))

        response = send_request(case['method'], case['uri'], case['data'])

        logger.info("响应状态码：{}".format(response.status_code))
        logger.info("预期结果：{}".format(case['expect']))
        logger.info("实际结果：{} {}".format(response.json()['status'], response.json()['msg']))

        try:
            assert response.json()['status'] == case['expect']
        except AssertionError:
            logger.exception("断言失败！")
            raise
        else:
            logger.info("断言成功！")
