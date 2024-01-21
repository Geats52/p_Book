def work_with_phonebook():

    def show_menu(phonebook):
        while True:# while (choice!=7): - выдает ошибку почему-то
            print("Выберите необходимое действие:")
            choice = input("1. Файл для добавления в справочник\n"                          
                            "2. Отобразить весь справочник\n"
                            "3. Найти абонента\n"                         
                            "4. Добавить абонента\n"                       
                            "5. Изменить абонента\n"                          
                            "6. Удалить абонента\n"                            
                            "7. Закончить работу\n")                           
            print()
            if choice == "1":
                file_to_add = input("Введите название файла для добавления: ")
                import_data(file_to_add, phonebook)            
            elif choice == "2":
                show_phonebook(phonebook)            
            elif choice == "3":
                contact_list = read_txt_dict(phonebook)
                find_number(contact_list)            
            elif choice == "4":
                add_phone_number(phonebook)            
            elif choice == "5":
                change_phone_number(phonebook)            
            elif choice == "6":
                delete_contact(phonebook)
            elif choice == "7":
                print("Закончить работу")
                break
            else:
                print("Неправильно выбрана команда")
                print()
                continue
    if __name__ == "__main__":
        file = "Phonebook.txt"
        show_menu(file)

#################### Операции со справочником #######################
#1        
def import_data(file_to_add, phonebook):
    try:
        with open(file_to_add, "r", encoding="utf-8") as new_contacts, open(phonebook, "a", encoding="utf-8") as file:
            contacts_to_add = new_contacts.readlines()
            file.writelines(contacts_to_add)
    except FileNotFoundError:
        print(f"{file_to_add} не найден")


#2
def show_phonebook(file_name):
    list_of_contacts = sorted(read_txt_dict(file_name), key=lambda x: x["Фамилия"])
    print_contacts(list_of_contacts)
    print()
    return list_of_contacts        


#3, 5, 6
def search_parameters():
    print("Как выполнить поиск?")
    search_field = input("1 - по фамилии\n2 - по имени\n3 - по номеру телефона\n")
    print()
    search_value = None
    if search_field == "1":
        search_value = input("Введите фамилию для поиска: ")
        print()
    elif search_field == "2":
        search_value = input("Введите имя для поиска: ")
        print()
    elif search_field == "3":
        search_value = input("Введите номер для поиска: ")
        print()
    return search_field, search_value
            # +
def find_number(contact_list):
    search_field, search_value = search_parameters()
    search_value_dict = {"1": "Фамилия", "2": "Имя", "3": "Номер телефона"}
    found_contacts = []
    for contact in contact_list:
        if contact[search_value_dict[search_field]] == search_value:
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        print("Контакт не найден!")
    else:
        print_contacts(found_contacts)
    print()
            # +
def search_to_modify(contact_list: list):
    search_field, search_value = search_parameters()
    search_result = []
    for contact in contact_list:
        if contact[int(search_field) - 1] == search_value:
            search_result.append(contact)
    if len(search_result) == 1:
        return search_result[0]
    elif len(search_result) > 1:
        print("Найдено несколько контактов")
        for i in range(len(search_result)):
            print(f"{i + 1} - {search_result[i]}")
        num_count = int(input("Выберите номер контакта, который нужно изменить/удалить: "))
        return search_result[num_count - 1]
    else:
        print("Контакт не найден")
    print()

#def write_txt(filename , phone_book):
#    with open('phonebook.csv','w+' ,encoding='utf-8') as phout:
#	phout.write('')

#4
def add_phone_number(file_name):
    info = ' '.join(get_new_number())
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(f"{info}\n")
            # +
def get_new_number():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_number = input("Введите номер телефона: ")
    return last_name, first_name, phone_number
            # +
def change_phone_number(file_name):
    contact_list = read_txt_list(file_name)
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    print("Какое поле вы хотите изменить?")
    field = input("1 - Фамилия\n2 - Имя\n3 - Номер телефона\n")
    if field == "1":
        number_to_change[0] = input("Введите фамилию: ")
    elif field == "2":
        number_to_change[1] = input("Введите имя: ")
    elif field == "3":
        number_to_change[2] = input("Введите номер телефона: ")
    contact_list.append(number_to_change)
    with open(file_name, "w", encoding="utf-8") as file:
        for contact in contact_list:
            line = ' '.join(contact) + "\n"
            file.write(line)
            # +
def delete_contact(file_name):
    contact_list = read_txt_list(file_name)
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    with open(file_name, "w", encoding="utf-8") as file:
        for contact in contact_list:
            line = ' '.join(contact) + "\n"
            file.write(line)

#============================================

def read_txt_dict(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()
    headers = ["Фамилия", "Имя", "Номер телефона"]
    contact_list = []
    for line in lines:
        line = line.strip().split()
        contact_list.append(dict(zip(headers, line)))
    return contact_list
            # +
def read_txt_list(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        contact_list = []
        for line in file.readlines():
            contact_list.append(line.split())
    return contact_list

def print_contacts(contact_list: list):
    for contact in contact_list:
        for key, value in contact.items():
            print(f"{key}: {value:12}", end='')
        print()





work_with_phonebook()
