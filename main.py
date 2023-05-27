from pathlib import Path
import file_parser as parser
from normalize import normalize


def scan(folder: Path) -> None:
    for item in folder.iterdir():
        if item.is_file():
            extension = item.suffix[1:].upper()  # Отримуємо розширення файлу
            if extension in ['JPEG', 'JPG', 'PNG', 'SVG']:
                # Додати файл до відповідного списку для зображень
                pass
            elif extension in ['AVI', 'MP4', 'MOV', 'MKV']:
                # Додати файл до відповідного списку для відео
                pass
            elif extension in ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX']:
                # Додати файл до відповідного списку для документів
                pass
            elif extension in ['MP3', 'OGG', 'WAV', 'AMR']:
                # Додати файл до відповідного списку для аудіо
                pass
            elif extension in ['ZIP', 'GZ', 'TAR']:
                # Додати файл до відповідного списку для архівів
                pass
            else:
                # Додати файл до списку для невідомих розширень
                pass
        elif item.is_dir():
            # Додати папку до списку папок
            pass
