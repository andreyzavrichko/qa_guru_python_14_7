import os

CURRENT_FILE = os.path.abspath(__file__) # получаем абсолютный путь к текущему файлу
CURRENT_DIRECTORY = os.path.dirname(CURRENT_FILE) # получаем абсолютный путь к текущей директории где находится файл с которым работаем
FILES_DIR = os.path.join(CURRENT_DIRECTORY, 'files') # делаем склейку пути к текущей директории и папки files
FOLDER_DIR = os.path.join(CURRENT_DIRECTORY, 'resource') # делаем склейку пути к текущей директории и папки files
ZIP_DIR = os.path.join(FOLDER_DIR, 'archive.zip') # делаем склейку пути к папке resource и зип файлу archive.zip