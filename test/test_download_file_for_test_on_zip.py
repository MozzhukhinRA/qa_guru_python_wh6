import os
import requests
from selene import browser, query
from paths import TMP_DIR


def test_download_and_save_pdf():
    browser.open('/file-format/pdf')
    download_url = browser.element('[title="Скачать example.pdf"]').get(query.attribute('href'))
    content = requests.get(url=download_url).content
    with open(f'{TMP_DIR}/example.pdf', 'wb') as file_pdf:
        file_pdf.write(content)
    assert os.path.exists(f'{TMP_DIR}/example.pdf')


def test_download_and_save_xlsx():
    browser.open('/file-format/xlsx')
    download_url = browser.element('[title="Скачать example.xlsx"]').get(query.attribute('href'))
    content = requests.get(url=download_url).content
    with open(f'{TMP_DIR}/example.xlsx', 'wb') as file_xlsx:
        file_xlsx.write(content)
    assert os.path.exists(f'{TMP_DIR}/example.xlsx')

def test_download_and_save_csv():
    browser.open('/file-format/csv')
    download_url = browser.element('[title="Скачать example.csv"]').get(query.attribute('href'))
    content = requests.get(url=download_url).content
    with open(f'{TMP_DIR}/example.csv', 'wb') as file_csv:
        file_csv.write(content)
    assert os.path.exists(f'{TMP_DIR}/example.csv')