import os

base_dir = os.path.dirname(os.path.dirname(__file__))

case_path = os.path.join(base_dir, "TestDatas\\")

conf_path = os.path.join(base_dir, "Conf\\conf.ini")

log_path = os.path.join(base_dir, "Outputs\\log\\apitest.log")

# report_path = os.path.join(base_dir, "Outputs\\report\\")

if __name__ == '__main__':
    print(case_path)
    print(conf_path)
    print(log_path)
