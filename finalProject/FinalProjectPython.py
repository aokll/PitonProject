class Note:
    def __init__(self,id,title,body,date):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

import json

def save_notes(notes):
    with open('notes.txt','w') as file:
        json.dump([note.dict for note in notes], file, indent=4, separators=(',',': '))

def read_notes():
    try:
        with open('notes.txt','r') as file:
            data = json.load(file)
            notes = [Note(**note) for note in data]
    except(json.decoder.JSONDecodeError,FileNotFoundError):
        notes = []
    return notes

import uuid

from datetime import datetime

def add_note():
    title = input('Введите загаловок заметки: ')
    body = input('Введите текст заметки: ')
    date = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    id = str(uuid.uuid4())
    note = Note(id,title,body,date)
    notes.append(note)
    save_notes(notes)

def edit_note():
    id = input('Введите идентификатор заметки для редактиррвания: ')
    note = next((note for note in notes if note.id == id), None )
    if note:
        print(f'Редактирование заметки: {note.title}')
        title = input('Введите новый заголовок заметки (Оставьте пустым чтобы не менять): ')
        body = input('Введите новый текст заметки (Оставьте пустым чтобы не менять): ')
        date = input('Введите новую дату и время заметки в формате dd.mm.yyyy hh:mm:ss (Оставьте пустым чтобы не менять): ')
        if title:
            note.totle = title
        if body:
            note.body = body
        if date:
            note.date = date
        save_notes(notes)
    else: print('Заметка ненайдена')

def delete_note():
    id = input('Введите идентификатор заметки для удаления: ')
    note = next((note for note in notes if note.id == id), None )
    if note:
        notes.remove(note)
        save_notes(notes)
    else:
        print('Заметка не найдена')

def view_notes():
    date_str = input('Введите дату для фильтрации заметок в формате dd.mm.yyyy: ')
    try:
        filter_date = datetime.strptime(date_str, '%d.%m.%y')
        filtered_notes = [note for note in notes if datetime.strptime(note.date, '%d.%m.%Y %H:%M:%S').date() == filter_date.date()]
    except ValueError:
        filtered_notes = notes
    if filtered_notes:
        for note in filtered_notes:
            print(f'{note.id}{note.title}({note.date}):n {note.body}')
        else:
            print('Нет заметок для отображения')

def main():
    global notes
    notes = read_notes()

    while True:
        print('n 1. показать список заметокn 2. Добавить заметкуn 3. Редактировать заметкуn 4. Удалить заметкуn 5. Выходn')
        choise = input('Выберите действие: ')
        if choise == '1':
            view_notes()
        elif choise == '2':
            add_note()
        elif choise == '3':
            edit_note()
        elif choise == '4':
            delete_note()
        elif choise == '5':
            break
        else:
            print('Недопустимый выбор')

main()