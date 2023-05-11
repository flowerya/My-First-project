##工具文件包
#读取yaml文件内容
import os
import yaml
def read_Yaml(key):
    with open(os.getcwd()+'/extract.yaml',mode='r',encoding='UTF-8') as f:
        value = yaml.load(stream=f,Loader=yaml.FullLoader)
        return value[key]

# 写入yaml文件内容
def write_Yaml(data):
    with open(os.getcwd()+'/extract.yaml',mode='a',encoding='UTF-8') as f:
        yaml.dump(data,stream=f,allow_unicode=True)
# 清空yaml文件内容
def clean_Yaml():
    with open(os.getcwd()+'/extract.yaml',mode='w',encoding='UTF-8') as f:
        f.truncate()
