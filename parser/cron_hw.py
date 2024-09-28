import json
import os

try:
    # Ваш код
    print("Скрипт запущен")

    # Путь к директории скрипта и директории parsed_data
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parsed_data_dir = os.path.join(script_dir, "parsed_data")

    # Проверка существования папки parsed_data
    if not os.path.exists(parsed_data_dir):
        print(f"Ошибка: Папка 'parsed_data' не найдена в директории {script_dir}")
    else:
        # Создание файла helloWorld.json
        file_path = os.path.join(parsed_data_dir, "helloWorld.json")
        data = {"message": "helloWorld"}

        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)

        print(f"Файл 'helloWorld.json' успешно создан в директории {parsed_data_dir}")

        # Создание пустого файла empty.json
        empty_file_path = os.path.join(parsed_data_dir, "empty.json")

        # Открытие файла для записи (создаст пустой файл)
        with open(empty_file_path, "w") as empty_file:
            pass  # Создаем пустой файл без содержимого

        print(f"Пустой файл 'empty.json' успешно создан в директории {parsed_data_dir}")

except Exception as e:
    print(f"Произошла ошибка: {str(e)}")
