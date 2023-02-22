import json
from datetime import *

history = []


def Selection():
    
    print('1 - Поиск по дате\n2 - Поиск по сумме \n3 - Поиск по описанию\nдругой вариант - отмена')
  #  choice_mode = ''
    choice_mode = input('Выберите режим поиска: ')
    res = []
    if choice_mode == '1':
        event = input('Введите дату расхода в формате dd-mm-yyyy :')
    elif choice_mode == '2':
        event = int(input('Введите сумму расхода :'))
    elif choice_mode == '3':
        event = input('Введите описание расхода :')
    else:
        return ''

    for i in history:
        if event in i:
            res.append(i)
            res[-1].append(history.index(i))
    return res


def load():

    fname = 'operations.json'
    with open(fname, 'r', encoding='utf-8') as em:
        history = json.load(em)
    print('История расходов успешно загружена')
    return history


def save():
    with open('operations.json', 'w', encoding='utf-8') as em:
        em.write(json.dumps(history, ensure_ascii=False))
    print('История расходов успешно сохранена')


print('Expences manager приветствует вас! Для начала работы и загрузки истории операций введите /start')
while True:
    command = input('Введите команду :')
    if command == '/start':
        print('Expences manager начал работу')
        try:
            history = load()
        except:
            history = []
            print('Создана новая история')
    elif command == '/stop':
        save()
        print('Expences manager закончил работу')
        break
    elif command == '/add':
        print('Добавление расхода')
        exp_date = input('Введите дату расхода в формате dd-mm-yyyy. Для текущей даты нажмите Enter: ')
        try:
            if exp_date == '':
                exp_date = datetime.now()
            else:
                exp_date = datetime.strptime(exp_date, "%d-%m-%Y")
            if exp_date > datetime.now():
                print('Добавление будующих расходов невозможно')
            else:
                exp_sum = int(input('Введите сумму расхода: '))
                exp_category = input('Введите описание расхода: ')
                history.append(
                    [str(exp_date.strftime("%d-%m-%Y")), exp_sum, exp_category])
                print('Расход успешно добавлен')
                save()
        except:
            print('Некорректный формат даты')

    elif command == '/list':
        print(f'Дата \t\tСумма \tОписание')
        for i in history:
            print('\t'.join(map(str, i)))

    elif command == '/report':
        print('Получение отчета о расходах')
        start_date = input(
            'Введите начальную дату отчета в формате dd-mm-yyyy: ')
        end_date = input(
            'Введите конечную дату отчета в формате dd-mm-yyyy. Для текущей даты нажмите Enter: ')
        try:
            start_date = datetime.strptime(start_date, "%d-%m-%Y")
            if end_date == '':
                end_date = datetime.now()
            else:
                end_date = datetime.strptime(end_date, "%d-%m-%Y")
            if start_date > end_date:
                print('Начальная дата не может быть больше конечной')
            else:
                report = []
                summa = 0
                for i in history:
                    if datetime.strptime(i[0], "%d-%m-%Y") >= start_date and datetime.strptime(i[0], "%d-%m-%Y") <= end_date:
                        report.append(i)
                        summa += i[1]
                print(f'Дата \t\tСумма \tОписание')
                for i in report:
                    print('\t'.join(map(str, i)))
                print(f'Общая сумма расходов за период {summa} рублей')
        except:
            print('Некорректный формат')
    elif command == '/search':
        print('Поиск и работа с расходом')
        search_res = Selection()
        while search_res != '':
       # print(search_res)
            search_res = list(enumerate(search_res))
            print(f'Номер \tДата \t\tСумма \tОписание')
            for i in search_res:
                print(i[0]+1, end='\t')
                print(f'{i[1][0]}\t{i[1][1]}\t{i[1][2]}')
            while True:
 #               try:
                    expence = input('Выберите номер расхода для изменения или Enter для нового поиска')
                    if expence == '':
                        break
                    elif int(expence) > len(search_res):
                        print('Введен неверный номер')
                    else:
                        action = int(input("Выберите требуемое действие. 1 - Изменить, 2 - удалить: "))
                        if action == 1:
                            new_date = input('Введите дату расхода в формате dd-mm-yyyy. Для текущей даты нажмите Enter: ')
                            try:
                                if new_date == '':
                                    new_date = datetime.now()
                                else:
                                    new_date = datetime.strptime(new_date, "%d-%m-%Y")
                                if new_date > datetime.now():
                                    print('Добавление будующих расходов невозможно')
                                else:
                                    new_sum = int(input('Введите сумму расхода: '))
                                    new_category = input('Введите описание расхода: ')
                                    print(search_res[0])
                                    history_index = search_res[int(expence)-1][1][-1]
                                    print(history_index)
     #                               history.append([str(exp_date.strftime("%d-%m-%Y")), exp_sum, exp_category])
     #                               print('Запись изменена')
     #                               save()
                            except:
                                 print('Некорректный формат даты')


         #                   ....__annotations__
          #              elif action == '2':
         #                   ....__annotations__
                        else:
                            print ('Введен некорректный номер')

 #                       ....__annotations__
#                except:
#                    print('Введены некорректные данные')
            search_res = Selection()



            

    elif command == '/help':
        print('Доступные команды:')
        print('/start - запуск бота\n/stop - остановка бота\n/add - добавить расход \n/list - список всех расходов\n/report - отчет за заданный период\n/help - список команд')
    else:
        print('Введена некорректная команда. Для отображения списка команд введите /help')
