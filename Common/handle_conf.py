from configparser import ConfigParser
from Common.handle_path import conf_path


class HandleConf(ConfigParser):
    def __init__(self, file_path):
        super().__init__()
        self.read(file_path)


conf = HandleConf(conf_path)

if __name__ == '__main__':
    print(conf.get('server', 'url'))
