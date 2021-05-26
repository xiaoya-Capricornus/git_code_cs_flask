import os
import configparser
import getpathInfo #引入自己写好的获取绝对路径的方法

path = getpathInfo.get_path()  # 返回的路径为：/Users/xy/PycharmProjects/pythonProject/xiaoya/cs
config_path = os.path.join(path, 'config.ini')
config = configparser.ConfigParser()  # 调用外部的读取配置文件的方法
config.read(config_path, encoding='utf-8')

class ReadConfig():
    def get_http(self, name):
        value = config.get('HTTP', name)
        return value
    def get_email(self, name):
        value = config.get('EMAIL', name)
        return value
    def get_mysql(self, name):
        value = config.get('DATABASE', name)
        return value

if __name__ == '__main__':#测试一下，我们读取配置文件的方法是否可用
    scheme = ReadConfig().get_http('scheme')
    print(scheme)

