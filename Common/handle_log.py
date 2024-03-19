import logging
from Common.handle_conf import conf
from Common.handle_path import log_path


class MyLogger(logging.Logger):
    def __init__(self, file=None):
        super().__init__(conf.get('log', 'name'), conf.get('log', 'level'))

        hdlr_console = logging.StreamHandler()

        fmt_out = "%(asctime)s %(name)s %(process)d %(thread)d %(filename)s(%(lineno)d) %(levelname)s: %(message)s"
        fmt = logging.Formatter(fmt=fmt_out, datefmt="%Y-%m-%d %H:%M:%S")
        hdlr_console.setFormatter(fmt=fmt)
        self.addHandler(hdlr_console)

        if file:
            hdlr_file = logging.FileHandler(file, encoding="utf-8")
            hdlr_file.setFormatter(fmt=fmt)
            self.addHandler(hdlr_file)


logger = MyLogger(log_path) if conf.getboolean('log', 'file_ok') else MyLogger()


if __name__ == '__main__':
    logger.debug('debug msg')
    logger.info('info msg')
    logger.warning('warning msg')
    logger.error('error msg')
    logger.critical('critical msg')
