from django.shortcuts import render
from therapist.models import Psychotherapists
from load import getAirtableRec
# Create your views here.


def showRecords(request):
    insertRecords()
    showall = Psychotherapists.objects.all()
    return render(request, 'index.html', {"data": showall})


def insertRecords():
    # load records from Airtable
    airtableRecords = getAirtableRec()
    newRecord = Psychotherapists()

    # add to db
    for record in airtableRecords:
        recordsDB = Psychotherapists.objects.all()
        newRecord.id = record['id']
        fields = record['fields']
        if (fields['Имя']):
            newRecord.name = fields['Имя']
        if (fields['Методы']):
            newRecord.metod = fields['Методы']
        if (fields['Фотография']):
            photo = fields['Фотография']
            newRecord.photo = photo[0]['url']
        # saveRecord.save()


def updateRecord(id, name, photo, metods):
    updateObj = Psychotherapists.objects.get(id=id)
