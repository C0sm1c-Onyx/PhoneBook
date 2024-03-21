class PhoneBook:
    def __init__(self) -> None:
        data = get_data()
        self.directory = data if data else []

    def add_entrie(self) -> None:
         entry = ['name', 'surname', 'pratronymic', 'organization', 'work_phone', 'personal_phone']
         entrie = {i: input(f'{i.title()}: ') for i in entry}
         self.directory.append(entrie)
         save_directory(self.directory)

    def edit_entrie(self) -> None:
        number_entrie = self.view_entries(text='Введите номер записи - для редактирования\n')
        try:
            entrie = self.directory[number_entrie]
            for key in entrie:
                entry = input(f'{key.title()} (Нажмите Enter, чтобы оставить без изменений): ')
                if entry:
                    entrie[key] = entry

        except:
            print('Такой записи не существует.')
            
        save_directory(self.directory)

    def search_entries(self) -> None:
        result = []
        filters = input('Поиск (характеристики вводить через пробел): ').split()
        for entrie in self.directory:
            for f in filters:
                if f in entrie.values() and entrie not in result:
                    result.append(entrie)

        if result:
            self.view_entries(result)

        else:
            print('Не найдено.')

    def view_entries(self, search_result:list=None, text='') -> [None, int]:
        max_c, min_c = 3, 0
        page_count = 1
        entrie_c = 1
        while True:
            dct = search_result if search_result else self.directory
            if min_c > len(dct):
                break

            print()
            for entrie in dct[min_c:max_c]:
                print(f'{entrie_c}. Запись')
                for key, value in entrie.items():
                    print(f'{key}: {value}')

                print()
                entrie_c += 1

            print(f'Стр. {page_count}\n')
            answer = input(f'{text}Введите next - для перехода на след. страницу\nНажмите Enter - для выбора другого действия\n')
            if answer == 'next':
                min_c = max_c
                max_c += 3
                page_count += 1

            elif answer.isdigit():    
                return int(answer) - 1
                
            else:
                break

                
def save_directory(directory:list) -> None:
    with open('data.txt', 'w') as file:
        file.write(str(directory))


def get_data() -> [list, None]:
    try:
        with open('data.txt', 'r') as file:
            data = file.read()
            return eval(data)
    
    except FileNotFoundError:
        return None
        
if __name__ == '__main__':
    pb = PhoneBook()
    COMMANDS = {'1': pb.view_entries, '2': pb.add_entrie, '3': pb.edit_entrie, '4': pb.search_entries}
    
    while True:
        action = input("\nВыберите действие:\nВывод записей из справочника - 1\nДобавление новой записи в справочник - 2\nРедактирование записи - 3\nПоиск записей - 4\nДля выхода нажмите Enter\n")
        if action not in COMMANDS:
            break
    
        print()
        COMMANDS[action]()
