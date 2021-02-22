from django.shortcuts import render
from therapist.models import Psychotherapists
from load import getAirtableRec
# Create your views here.


def showTherapist(request):
    insertTherapist()
    showall = Psychotherapists.objects.all()
    return render(request, 'index.html', {"data": showall})


def insertTherapist():
    # load json from Airtable
    airtableRecords = getAirtableRec()
    saveRecord = Psychotherapists()
    print(saveRecord.name)
    for row in airtableRecords:
        saveRecord.id = row['id']
        fields = row['fields']
        print(fields)
        if (fields['Имя']):
            saveRecord.name = fields['Имя']
            print(fields['Имя'])
        if (fields['Методы']):
            saveRecord.metod = fields['Методы']
            print(fields['Методы'])
        if (fields['Фотография']):
            print('вот Фотография')
            photo = fields['Фотография']
            saveRecord.photo = photo[0]['url']
            print(saveRecord.photo)
    saveRecord.save()
