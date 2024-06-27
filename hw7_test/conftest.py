import os
import pytest
import zipfile
from pathlib import Path


@pytest.fixture(scope='session', autouse=True)
def create_archive():
    archive_folder = Path('resources')
    files_folder = Path('files')

    archive_path = archive_folder / 'archive.zip'

    archive_folder.mkdir(parents=True, exist_ok=True)
    files_folder.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(archive_path, 'w') as zf:
        files_to_add = ['employee.xlsx', 'report.pdf', 'sampleEcwid.csv']

        for file in files_to_add:
            add_file = os.path.join(files_folder, file)
            zf.write(add_file, os.path.basename(add_file))
