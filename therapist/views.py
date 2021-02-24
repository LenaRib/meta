from django.shortcuts import render
from therapist.models import Psychotherapists, Log
from loadFromAirtable import getAirtableRec


def moveAirtableToDB():
    # load records from Airtable
    airtableRecords = getAirtableRec()

# load records from DB
    recordsDB = Psychotherapists.objects.all()

# create list of record in DB, not in Airtable
    listDBid = []
    for record in recordsDB:
        listDBid.append(record.id)
    for airRecord in airtableRecords:
        # or result=list(set(listDBid) - set(airRecordID))
        if (airRecord['id'] in listDBid):
            listDBid.remove(airRecord['id'])

# delete records from DB that are not in Airtable
    for i in listDBid:
        deleteRecord(i)


# update or insert from Airtable
    for record in airtableRecords:
        try:
            print(Psychotherapists.objects.get(id=record['id']))
            updateRecord(record)
        except:
            insertRecords(record)


def insertRecords(record):
    newRecord = Psychotherapists()
    newRecord.id = record['id']
    fields = record['fields']
    try:
        newRecord.name = fields['Имя']
        newRecord.metod = fields['Методы']
        photo = fields['Фотография']
        newRecord.photo = photo[0]['url']
    except:
        print('EMPTY FIELDS detected in id: ' + record['id'])
    newRecord.save()

# todo move Log logic to one function and call it
    logRecord = Log()
    logRecord.event = 'insert record with id = ' + record['id']
    print(logRecord.event)
    logRecord.save()


def updateRecord(record):
    recID = record['id']
    updateRec = Psychotherapists.objects.get(id=recID)
    newRec = Psychotherapists()
    logMessage = ''
    try:
        fields = record['fields']
        newRec.name = fields['Имя']
        newRec.metod = fields['Методы']
        photoList = fields['Фотография']
        newRec.photo = photoList[0]['url']
    except:
        print('EMPTY FIELDS detected in id: ' + recID)
    if (updateRec.name != newRec.name):
        updateRec.name = newRec.name
        logMessage = ' update name to ' + newRec.name

    if (str(updateRec.metod) != str(newRec.metod)):
        updateRec.metod = newRec.metod
        logMessage = ' update metod to ' + str(updateRec.metod)

    if (updateRec.photo != newRec.photo):
        updateRec.photo = newRec.photo
        logMessage = ' update photo to ' + newRec.photo

    if(logMessage):
        logRecord = Log()
        logRecord.event = 'id: ' + recID + logMessage
        logRecord.save()
        print(logRecord.event)
    updateRec.save()


def deleteRecord(id):
    deleteRec = Psychotherapists.objects.get(id=id)
    deleteRec.delete()
    logRecord = Log()
    logRecord.event = 'delete record with id = ' + id
    logRecord.save()
    print(logRecord.event)


def showRecords(request):
    moveAirtableToDB()
    showall = Psychotherapists.objects.all()
    return render(request, 'index.html', {"data": showall})
