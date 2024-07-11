
def work_with_phonebook():

    choice=show_menu()

    phone_book=read_txt('phon.txt')

    while (choice!=8):

        if choice==1:
            print_result('phon.txt')
        elif choice==2:
            #last_name=input('lastname ')
            #print(find_by_lastname(phone_book,last_name))
            print("Пункт временно не работает, выберите другой")
        elif choice==3:
            #last_name=input('lastname ')
            #new_number=input('new  number ')
            #print(change_number(phone_book,last_name,new_number))
            print("Пункт временно не работает, выберите другой")
        elif choice==4:
            #lastname=input('lastname ')
            #print(delete_by_lastname(phone_book,lastname))
            print("Пункт временно не работает, выберите другой")
        elif choice==5:
            #number=input('number ')
            #print(find_by_number(phone_book,number))
            print("Пункт временно не работает, выберите другой")
        elif choice==6:
            #user_data=input('new data ')
            #add_user(phone_book,user_data)
            #write_txt('phonebook.txt',phone_book)
            break
        elif choice==7:
            #print(\n)
            source_file=input('введите название исходного справочника:')
            line_number=int(input('введите номер строки для копирования:'))
            destination_file=input('введите название справочника назначения:')
            copy_line_to_file(source_file, line_number, destination_file)
            #print("Строка №", line_number, "из файла", source_file, "скопирована в файл", destination_file)

        choice=show_menu()



def show_menu():
    print("\nВыберите действие:\n"
          "1. отобразить справочник\n"
          "2. найти по фамилии\n"
          "3. найти по номеру\n"
          "4. добавить чел в справочник\n"
          "5. сохранить справочник в тхт\n"
          "6. закончить работу\n"
          "7. копировать абонента из другого справочника")
    choice = int(input())
    return choice


def print_result(filename):
    
    with open(filename,'r',encoding='utf-8') as phb:

        for line in phb:
           print(line)
		    #dict(( (фамилия,Иванов),(имя, Точка),(номер,8928) ))
           
   # return phone_book



def read_txt(filename): 

    phone_book=[]

    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']

#line.split(',') = [Питонов,    Антон,     '777',    'умеет в Питон']

    with open(filename,'r',encoding='utf-8') as phb:

        for line in phb:
           record = dict(zip(fields, line.split(',')))
		    #dict(( (фамилия,Иванов),(имя, Точка),(номер,8928) ))
           phone_book.append(record)	

    return phone_book



def write_txt(filename , phone_book):

    with open(filename,'w',encoding='utf-8') as phout:

        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}\n')



def copy_line_to_file(source_file, line_number, destination_file):
    
    line_for_copy=' '
    with open(source_file,'r',encoding='utf-8') as sfile:
        line_count = sum(1 for line in sfile)
    with open(source_file,'r',encoding='utf-8') as sfile:
        if 1 <= line_number <= line_count :
            for i, line in enumerate(sfile):
                if i == line_number-1:
                    line_for_copy=line
                    line_for_copy='\n' + line_for_copy
                    #print(line_for_copy)
                    break
            with open(destination_file,'a',encoding='utf-8') as dfile:
                dfile.write(line_for_copy)
            print("Строка №", line_number, "из файла", source_file, "скопирована в файл", destination_file)
        else:
            print("Такой строки не существует.")
        


work_with_phonebook()

