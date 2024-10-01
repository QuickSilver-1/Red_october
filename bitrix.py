from time import sleep
from requests import get
import openpyxl
from base64 import b64encode


def request():
    file_str = ""

    wb = openpyxl.load_workbook("intimissimi.xlsx")
    for i in wb['Sheet1'].values:
        file_str += ",".join([str(j) for j in i]) + "\n"

    get(url="https://b24-zlccg7.bitrix24.ru/rest/1/h976b7yi1427d5lm/disk.file.uploadversion.json", params={"id": 97, "fileContent": b64encode(file_str.encode("UTF-8")).decode()})
    file_str = ""

    wb = openpyxl.load_workbook("intersharm.xlsx")
    for i in wb['Sheet1'].values:
        file_str += ",".join([str(j) for j in i]) + "\n"

    get(url="https://b24-zlccg7.bitrix24.ru/rest/1/h976b7yi1427d5lm/disk.file.uploadversion.json", params={"id": 95, "fileContent": b64encode(file_str.encode("UTF-8")).decode()})

while True:
    request()
    sleep(300)
    