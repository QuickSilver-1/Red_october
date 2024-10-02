from time import sleep
from requests import get
import openpyxl
from base64 import b64encode


def request():
    file_str = ""

    wb = openpyxl.load_workbook("intimissimi.xlsx")
    for i in wb['Sheet1'].values:
        file_str += ",".join([str(j) for j in i]) + "\n"

    get(url="https://vmesteplus.bitrix24.ru/rest/18/6x0d2i73b2bljn05/disk.file.uploadversion.json", params={"id": 2520, "fileContent": b64encode(file_str.encode("UTF-8")).decode()})
    
    file_str = ""

    wb = openpyxl.load_workbook("intersharm.xlsx")
    for i in wb['Sheet1'].values:
        file_str += ",".join([str(j) for j in i]) + "\n"

    get(url="https://vmesteplus.bitrix24.ru/rest/18/6x0d2i73b2bljn05/disk.file.uploadversion.json", params={"id": 4494, "fileContent": b64encode(file_str.encode("UTF-8")).decode()})

while True:
    request()
    sleep(300)
    