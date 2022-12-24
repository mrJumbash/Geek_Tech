import re

while True:
    user_input = int(input('names [1], emails [2], files [3], colors [4], exit [5]'))
    with open('MOCK_DATA.txt', 'r') as file:
        content = file.read()
    if user_input == 1:
        name_list = re.findall(r"\b[A-Z][a-zA-Z\'\-\. ]+[\s]+[a-zA-Z\'\-\. ]+\b", content)
        with open('names.txt', 'w') as file1:
            for name in name_list:
                file1.write(f'{name.strip("")}\n')

    elif user_input == 2:
        mail_list = re.findall(r'[a-z0-9]+@[a-z0-9|-]+\.[a-z]+', content)
        with open('mail.txt', 'w') as file2:
            for mail in mail_list:
                file2.write(f'{mail}\n')

    elif user_input == 3:
        files_list = re.findall(r'\s[A-Za-z]+\.[a-z0-9]+', content)
        with open('files.txt', 'w') as file3:
            for file in files_list:
                file3.write(f'{file}\n')

    elif user_input == 4:
        color_list = re.findall(r'#[a-z0-9][0-9a-z]+', content)
        with open('colors.txt', 'w') as file4:
            for color in color_list:
                file4.write(f'{color}\n')

    elif user_input == 5:
        break