from time import sleep
import requests
import openpyxl
from base64 import b64encode
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


def request():
    file_str = ""
    
    session = requests.Session()

    retries = Retry(total=5,
                backoff_factor=0.1,
                status_forcelist=[500, 502, 503, 504],
                allowed_methods=frozenset(['GET', 'POST']))

    session.mount('http://', HTTPAdapter(max_retries=retries))
    session.mount('https://', HTTPAdapter(max_retries=retries))

    wb = openpyxl.load_workbook("intimissimi.xlsx")
    for i in wb['Sheet1'].values:
        file_str += ",".join([str(j) for j in i]) + "\n"

    x = requests.get(url="https://vmesteplus.bitrix24.ru/rest/18/b51j140hlvfrfwwu//disk.file.uploadversion.json", params={"id": 2520, "fileContent": b64encode(file_str.encode("UTF-8")).decode()})
    file_str = ""

    wb = openpyxl.load_workbook("intersharm.xlsx")
    for i in wb['Sheet1'].values:
        file_str += ",".join([str(j) for j in i]) + "\n"

    y = requests.get(url="https://vmesteplus.bitrix24.ru/rest/18/b51j140hlvfrfwwu/disk.file.uploadversion.json", params={"id": 4494, "fileContent": b64encode(file_str.encode("UTF-8")).decode()})
    print(x, y)

while True:
    request()
    sleep(300)
    