def work_with_phonebook():
	
    choice=show_menu()
    phone_book=read_txt('phonebook.csv')
    while (choice!=7):

        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('lastname ')
            print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            last_name=input('lastname ')
            new_number=input('new  number ')
            print(change_number(phone_book,last_name,new_number))
	    	
        elif choice==4:
            lastname=input('lastname ')
            print(delete_by_lastname(phone_book,lastname))
        elif choice==5:
            number=input('number ')
            print(find_by_number(phone_book,number))
        elif choice==6:
            user_data=input('new data ')
            add_user(phone_book,user_data)
            write_txt('phonebook.csv',phone_book)

        choice=show_menu()





def show_menu():
	print("\nВыберите необходимое действие:\n"
		"1. Отобразить весь справочник\n"
		"2. Найти абонента по фамилии\n"
		"3. Найти абонента по номеру телефона\n"
		"4. Добавить абонента в справочник\n"
		"5. Сохранить справочник в текстовом формате\n"
		"6. Закончить работу")
	choice = int(input())
	return choice





# Иванов,		    Иван,           111,	описание Иванова

# Петров,		    Петр,           222,	описание Петрова

# Васичкина,	    Василиса,	    333,    описание Васичкиной

# Питонов,	        Антон,          777,	умеет в Питон




def print_result(phone_book):
    print(phone_book)

def find_by_lastname(phone_book, last_name):#поиск по  значению
    if last_name in phone_book:
        for i in phone_book:
            0
        return last_name
    else:
        return "Ошибка"

def change_number(phone_book, last_name, new_number):#поиск по  значению?
    if new_number in phone_book:
        for i in phone_book:
            0
        return last_name
    else:
        return "Ошибка"
	    	
def delete_by_lastname(phone_book, lastname):#добавление значения в список?
    phone_book.append(lastname)
    return phone_book

def find_by_number(phone_book, number):#сохранение в .txt?
    a=open('phonebook.csv','w+')
    return a

def add_user(phone_book, user_data):#
    if user_data == 7:
        phone_book.close()

def read_txt(filename):# Читатет тел. справочник

    phone_book=[]

    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
                #dict(( (фамилия, Иванов),(имя, Точка),(номер,8928) ))
            phone_book.append(record)
        return phone_book

def write_txt(filename , phone_book):#Создает новый файл и переносит в него информацию

    with open('phonebook.csv','w' ,encoding='utf-8') as phout:

        for i in range(len(phone_book)):

            s='' 
            for v in phone_book[i].values():#
                s+=v+','
            phout.write(f'{s[:-1]}\n')

#def write_txt(filename , phone_book):
#    with open('phonebook.csv','w+' ,encoding='utf-8') as phout:
#	phout.write('')





work_with_phonebook()