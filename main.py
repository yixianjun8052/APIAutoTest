import pytest
import os

if __name__ == '__main__':
    pytest.main(['-sv', '--alluredir=Outputs/report/allure'])
    os.system("allure generate Outputs/report/allure -o Outputs/report/myallureport --clean")
    # os.system("allure serve Outputs/report/allure")
