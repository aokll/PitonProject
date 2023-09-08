class Note:
    def __init__(self,id,title,body,date):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

import json

def save_notes(notes):
    with open('botes.txt','w') as file:
        json.dump([note.dict for note in notes], file, indent=4, separators=(',',': '))

def read_notes():
    try:
        with open('botes.txt','r') as file:
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