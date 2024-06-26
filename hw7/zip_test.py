import zipfile
import csv
from pypdf import PdfReader
import pandas as pd


def test_csv():
    with zipfile.ZipFile('ziptest.zip') as zip_file:
        with zip_file.open('sampleEcwid.csv') as csv_file:
            content = csv_file.read().decode(
                'utf-8-sig')
            csvreader = list(csv.reader(content.splitlines()))
            second_row = csvreader[1]

            assert second_row[0] == 'Billabong'
            assert second_row[1] == 'M115GTLE'
            assert second_row[2] == 'Pre-order available'


def test_pdf():
    with zipfile.ZipFile('ziptest.zip') as zip_file:
        with zip_file.open('report.pdf') as pdf_file:
            reader = PdfReader(pdf_file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            print(text)
            assert 'БАЛАНС 494669' in text, "Искомый текст не найден в PDF файле"


def test_xlsx():
    with zipfile.ZipFile('ziptest.zip') as zip_file:
        with zip_file.open('employee.xlsx') as xlsx_file:
            df = pd.read_excel(xlsx_file)
            first_row = df.iloc[0]
            print(first_row)
            assert 'Васильков Петр Григорьевич' in first_row.values, "Сотрудник не найден"
