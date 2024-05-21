import os
import zipfile


def read_zip(zip_file, extract_folder):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)


def find_common_numbers(folder_path, file_extension):
    common_numbers = set()
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(file_extension):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    numbers_in_file = {int(line.strip()) for line in f}
                    common_numbers = common_numbers.intersection(numbers_in_file) if common_numbers else numbers_in_file
    return common_numbers


def main():
    extract_folder = 'extracted_data/'
    read_zip('data.zip', extract_folder)
    common_numbers = find_common_numbers(extract_folder, '.txt')
    print("共通する数値:")
    for number in common_numbers:
        print(number)


if __name__ == "__main__":
    main()
