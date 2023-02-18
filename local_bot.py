import json
from datetime import *

history = []

def load():
           
            fname='operations.json' 
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
            history =[]
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
                history.append([str(exp_date.strftime("%d-%m-%Y")), exp_sum, exp_category])
                print('Расход успешно добавлен')
                save()
        except:
            print('Некорректный формат даты')
        
    elif command == '/list':
        print(f'Дата \t\tСумма \tОписание')
        for i in history:
            print('\t'.join(map(str,i)))

    elif command == '/report':
        print('Получение отчета о расходах')
        start_date = input('Введите начальную дату отчета в формате dd-mm-yyyy: ')
        end_date = input('Введите конечную дату отчета в формате dd-mm-yyyy. Для текущей даты нажмите Enter: ')
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
                    print('\t'.join(map(str,i)))
                print(f'Общая сумма расходов за период {summa} рублей')              
        except:
           print('Некорректный формат')
    elif command == '/help':
        print('Доступные команды:')
        print('/start - запуск бота\n/stop - остановка бота\n/add - добавить расход \n/list - список всех расходов\n/report - отчет за заданный период\n/help - список команд')     
    else:
        print('Введена некорректная команда. Для отображения списка команд введите /help')

    

                
                  
                  

         
  

            
            
    
