class Note:
    def __init__(self, last_name, first_name, phone_number, birth_date):
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number
        self.birth_date = birth_date

class OpenHashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        return sum(ord(c) for c in key) % self.size

    def insert(self, note):
        index = self.hash_function(note.phone_number)

        while self.data[index] is not None:
            index = (index + 1) % self.size

        self.data[index] = note

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for note in self.data:
                if note is not None:
                    file.write(f'{note.last_name};{note.first_name};{note.phone_number};{".".join(note.birth_date)}\n')

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    last_name, first_name, phone_number, birth_date = line.strip().split(';')
                    birth_date = birth_date.split('.')
                    self.insert(Note(last_name, first_name, phone_number, birth_date))
        except FileNotFoundError:
            print(f'файл {filename} не знайдено')

    def display(self):
        for index, note in enumerate(self.data):
            if note is not None:
                print(f'[{index}] {note.last_name} {note.first_name}, {note.phone_number}, {note.birth_date}')
            else:
                print(f'[{index}] Порожньо')
    def find_by_criteria(self, criteria, value):
        result = []
        for note in self.data:
            if note is not None:
                if criteria == 'Імя' and (note.last_name.lower() == value.lower() or note.first_name.lower() == value.lower()):
                    result.append(note)
                elif criteria == 'Телефон' and note.phone_number == value:
                    result.append(note)
                elif criteria == 'Дата нородження' and note.birth_date == value:
                    result.append(note)
        return result
    def remove_by_criteria(self, criteria, value):
        removed = False
        for index, note in enumerate(self.data):
            if note is not None:
                if criteria == 'Імя' and (note.last_name.lower() == value.lower() or note.first_name.lower() == value.lower()):
                    self.data[index] = None
                    removed = True
                elif criteria == 'Телефон' and note.phone_number == value:
                    self.data[index] = None
                    removed = True
                elif criteria == 'Дата нородження' and note.birth_date == value:
                    self.data[index] = None
                    removed = True

        if removed:
            self.rehash()

        return removed
    
    def rehash(self):
        old_data = self.data[:]
        self.data = [None] * self.size
        for note in old_data:
            if note is not None:
                self.insert(note)


table_size = 10
table = OpenHashTable(table_size)

while True:
        print('1. Додати запис')
        print('2. Знайти запис')
        print('3. Видалити запис')
        print('4. Зберегти до файлу')
        print('5. Завантажити з файлу')
        print('6. Показати таблицю')
        print('0. Вихід')
        choice = input('Виберіть опцію: ')

        if choice == '1':
            last_name = input('Ведіть прізвище: ')
            first_name = input('Введіть імя: ')
            phone_number = input('Ведіть номер телефону: ')
            birth_date = input('Ведіть дату народження (dd.mm.yyyy): ').split('.')
            table.insert(Note(last_name, first_name, phone_number, birth_date))
            print('Запис додано')
        elif choice == '2':
            print('1. Знайти за іменем')
            print('2. Знайти за номером телефону')
            print('3. Знайти за датою народження')
            search_choice = input('Оберіть критерій пошуку: ')

            if search_choice == '1':
                name = input('Введіть ім\'я або прізвище: ')
                found_notes = table.find_by_criteria('Імя', name)
            elif search_choice == '2':
                phone_number = input('Введіть номер телефону: ')
                found_notes = table.find_by_criteria('Телефон', phone_number)
            elif search_choice == '3':
                birth_date = input('Введіть дату народження (dd.mm.yyyy): ')
                birth_date = birth_date.split('.')
                found_notes = table.find_by_criteria('Дата нородження', birth_date)

            if not found_notes:
                print('Запис не знайдено')
            else:
                for note in found_notes:
                    print(f'{note.last_name} {note.first_name}, {note.phone_number}, {note.birth_date}')
        elif choice == '3':
            print('1. Видалити за іменем')
            print('2. Видалити за номером телефону')
            print('3. Видалити за датою народження')
            remove_choice = input('Оберіть критерій видалення: ')

            if remove_choice == '1':
                name = input('Введіть ім\'я або прізвище: ')
                removed = table.remove_by_criteria('Імя', name)
            elif remove_choice == '2':
                phone_number = input('Введіть номер телефону: ')
                removed = table.remove_by_criteria('phone', phone_number)
            elif remove_choice == '3':
                birth_date = input('Введіть дату народження (dd.mm.yyyy): ')
                birth_date = birth_date.split('.')
                removed = table.remove_by_criteria('birthdate', birth_date)

            if removed:
                print('Запис(и) видалено')
            else:
                print('Запис не знайдено')
        elif choice == '4':
            filename = input('Введіть файл: ')
            table.save_to_file(filename)
            print('Запис занесоно до файлу')
        elif choice == '5':
            filename = input('Введіть файл: ')
            table.load_from_file(filename)
            print('Запис завантажено')
        elif choice == '6':
            print('Відкрита хеш таблиця:')
            table.display()
        elif choice == '0':
            print('Бувайте!')
            break
        else:
            print('Неправильний вибір спробуйте щераз')