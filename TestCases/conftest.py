import pytest
from Common.handle_excel import HandleExcel
from Common.handle_path import case_path
from Common.handle_data import get_token, EnvAttr, clear_env_attr
from Common.handle_request import send_request


@pytest.fixture(scope='class')
def class_setup_teardown():
    clear_env_attr()
    setattr(EnvAttr, 'jwt_token', get_token())
    yield
    clear_env_attr()


case_excel = case_path + 'apicase.xlsx'
login_cases = HandleExcel(case_excel, 'login').read_all('login')


@pytest.fixture(params=login_cases)
def login_case_fixture(request):
    return request.param


cart_sheet = HandleExcel(case_excel, 'cart')
cart_list_cases = cart_sheet.read_all('cart_list')
cart_add_cases = cart_sheet.read_all('cart_add')


@pytest.fixture(params=cart_list_cases)
def cart_list_case_fixture(request):
    return request.param


@pytest.fixture(params=cart_add_cases)
def cart_add_case_fixture(request):
    return request.param


order_sheet = HandleExcel(case_excel, 'order')
order_create_cases = order_sheet.read_all('order_create')


@pytest.fixture(params=order_create_cases)
def order_create_case_fixture(request):
    return request.param


@pytest.fixture()
def order_create_fixture():
    # 前置：购物车有商品
    case = cart_add_cases[0]
    send_request(case['method'], case['uri'], case['data'], case['data_type'],
                 token=getattr(EnvAttr, 'jwt_token'))
    yield
