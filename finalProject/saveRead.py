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