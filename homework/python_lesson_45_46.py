# def find_and_replace(content, replacements):
#     for old_word, new_word in replacements:
#         content = content.replace(old_word, new_word)
#     return content
#
#
# try:
#     name_file = "hi.txt"
#
#     with open(name_file, 'r') as file:
#         content = file.read()
#
#     example = ["Tunar", "Aydan", "Rasul", "Kamal", "Leyla", "Samir", "Farid", "Nariman"]
#
#     old_name = input("Введите имя для замены: ")
#
#     if old_name in example:
#         new_name = input(f"Введите новое имя для замены '{old_name}': ")
#         replacements = [(old_name, new_name)]
#         updated_content = find_and_replace(content, replacements)
#     else:
#         print(f"Имя '{old_name}' не найдено в списке.")
#         updated_content = content
#
#     with open(name_file, 'w') as file:
#         file.write(updated_content)
#
# except BaseException as exc:
#     print(f"Произошла ошибка: {exc}")
# finally:
#     print("Код выполнен")
#
