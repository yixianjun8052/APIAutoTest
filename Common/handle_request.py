import requests
from Common.handle_conf import conf
from Common.handle_log import logger


def send_request(method, uri, data=None, data_type=None, token=None):
    headers = __pre_headers(token) if token else None
    url = conf.get('server', 'url') + uri

    logger.info("接口URL：{} {}".format(url, method))
    logger.info("参数数据：{}".format(data))

    method = method.upper()
    if method == 'GET':
        return requests.get(url, params=data, headers=headers)
    elif method == 'POST':
        if data_type == 'form':
            return requests.post(url, data=data, headers=headers)
        else:
            return requests.post(url, json=data, headers=headers)


def __pre_headers(token):
    headers = {'jwt_token': token}
    return headers


if __name__ == '__main__':
    from Common.handle_excel import HandleExcel
    from Common.handle_path import case_path

    cases = HandleExcel(case_path + 'apicase.xlsx', 'login').read_all()
    for case in cases:
        print(case['uri'], case['method'], case['data'], case['data_type'], case['expect'])
        url = conf.get('server', 'url') + case['uri']
        resp = send_request(case['method'], url, case['data'], case['data_type'])
        print(resp.json())
        status = resp.json()['status']
        expect = case['expect']
        print(type(status), status, type(expect), expect, status == expect)
