import os
import shutil
import argparse


def copy_and_sort_files(src_dir, dest_dir):
    try:

        for item in os.listdir(src_dir):
            src_path = os.path.join(src_dir, item)

            if os.path.isdir(src_path):
                copy_and_sort_files(src_path, dest_dir)
            else:
                file_extension = os.path.splitext(item)[1].lower()
                if file_extension == '':
                    file_extension = 'no_extension'
                dest_extension_dir = os.path.join(dest_dir, file_extension[1:] if file_extension.startswith(
                    '.') else file_extension)
                os.makedirs(dest_extension_dir, exist_ok=True)
                dest_path = os.path.join(dest_extension_dir, item)
                shutil.copy2(src_path, dest_path)
                print(f"Скопійовано: {src_path} -> {dest_path}")

    except Exception as e:
        print(f"Помилка: {e}")


def main():
    parser = argparse.ArgumentParser(description="Копіювання файлів за розширенням з однієї директорії до іншої.")
    parser.add_argument("src_dir", help="Шлях до вихідної директорії.")
    parser.add_argument("dest_dir", nargs="?", default="dist",
                        help="Шлях до директорії призначення (за замовчуванням 'dist').")
    args = parser.parse_args()
    src_dir = args.src_dir
    dest_dir = args.dest_dir
    if not os.path.exists(src_dir):
        print(f"Директорія {src_dir} не існує.")
        return
    os.makedirs(dest_dir, exist_ok=True)
    copy_and_sort_files(src_dir, dest_dir)

# Приклад використання: python task1.py ./sample Буде створенаа директорія dist з відсортованими файлами за розширенням
if __name__ == "__main__":
    main()
