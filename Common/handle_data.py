from Common.handle_conf import conf
from Common.handle_request import send_request


class EnvAttr:
    """ 通过动态设置类属性，保存环境变量 """
    pass


def clear_env_attr():
    """ 清理 EnvAttr 类中的动态添加的类属性。 """
    for attr in dict(EnvAttr.__dict__):
        if not attr.startswith('__'):
            delattr(EnvAttr, attr)


def get_token():
    login_url = '/loginWithJwt'
    login_data = {"userName": conf.get('server', 'username'), "password": conf.get('server', 'password')}
    return send_request('get', login_url, login_data).json()['data']


if __name__ == '__main__':
    setattr(EnvAttr, 'jwt_token', get_token())
    if hasattr(EnvAttr, 'jwt_token'):
        print(getattr(EnvAttr, 'jwt_token'))
    print(EnvAttr.__dict__)
    clear_env_attr()
    print(EnvAttr.__dict__)
