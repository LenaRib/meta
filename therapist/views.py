from django.shortcuts import render
from therapist.models import Psychotherapists, Log
from loadFromAirtable import getAirtableRec


def moveAirtableToDB():
    # load records from Airtable
    airtableRecords = getAirtableRec()

    # load records from DB
    recordsDB = Psychotherapists.objects.all()

    # check that record from Airtable exist in DB
    if (recordsDB.count() > 0):
        print('смотри сколько')
        print(recordsDB.count())
    # for record in
    # if (recordsDB[id] ==)
    # insertRecords(airtableRecords)


def insertRecords(airtableRecords):
    newRecord = Psychotherapists()
    # add to db
    for record in airtableRecords:
        newRecord.id = record['id']
        fields = record['fields']
        if (fields['Имя']):
            newRecord.name = fields['Имя']
        if (fields['Методы']):
            newRecord.metod = fields['Методы']
        if (fields['Фотография']):
            photo = fields['Фотография']
            newRecord.photo = photo[0]['url']
        newRecord.save()


def updateRecord(id, name, photo, metod):
    updateRec = Psychotherapists.objects.get(id=id)
    if (updateRec.name != name):
        updateRec.name = name
    updateRec.metod = metod
    updateRec.photo = photo
    updateRec.save()


def deleteRecord(id):
    deleteRec = Psychotherapists.objects.get(id=id)
    deleteRec.delete()


def showRecords(request):
    # insertRecords()
    showall = Psychotherapists.objects.all()
    return render(request, 'index.html', {"data": showall})
