import pandas
import json


class HandleExcel:
    """ 处理excel文件：可以选择读取哪个文件的哪张表 """
    def __init__(self, filename, sheetname):
        self.filename = filename
        self.sheetname = sheetname

    def read_all(self, api_type=None):
        data = pandas.read_excel(self.filename, self.sheetname)
        if api_type:
            data = data[data['api_type'] == api_type]
        ret = []
        for i in data.index:
            tempd = {}
            for title in data.iloc[[0]]:
                if isinstance(data[title][i], float):
                    data[title][i] = None
                if title == "data" and data[title][i]:
                    tempd[title] = json.loads(data[title][i])
                else:
                    tempd[title] = data[title][i]
            ret.append(tempd)
        return ret


if __name__ == '__main__':
    from Common.handle_path import case_path
    datas = HandleExcel(case_path + 'apicase.xlsx', 'login').read_all('cart_list')
    for x in datas:
        print(x)

    from Common.handle_conf import conf
    from Common.handle_request import send_request

    base_url = conf.get('server', 'url')
    method, url = datas[0]['method'], base_url + datas[0]['uri']
    resp = send_request(method, url)
    print(resp.json())