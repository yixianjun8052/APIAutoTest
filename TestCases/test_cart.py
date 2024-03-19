import pytest
from Common.handle_request import send_request
from Common.handle_log import logger
from Common.handle_data import EnvAttr


@pytest.mark.usefixtures('class_setup_teardown')
class TestCart:

    # @pytest.mark.skip
    def test_cart_list(self, cart_list_case_fixture):
        case = cart_list_case_fixture
        logger.info(">>> 开始执行 {}：{}".format(case["case_id"], case["title"]))

        response = send_request(case['method'], case['uri'], case['data'], token=getattr(EnvAttr, 'jwt_token'))

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

    def test_cart_add(self, cart_add_case_fixture):
        case = cart_add_case_fixture
        logger.info(">>> 开始执行用例 {}：{}".format(case["case_id"], case["title"]))

        response = send_request(case['method'], case['uri'], case['data'], case['data_type'],
                                token=getattr(EnvAttr, 'jwt_token'))

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
