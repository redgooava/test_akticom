from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
import csv
from .models import CSVModel


def cleaningData(badList):  # Приведение данных к нормальному "небитому" виду
    copyList = badList.copy()
    massOfBadSymbols = ['"', '<br>']
    for i in range(0, len(copyList), 1):  # Очистка от единичных артефактов
        for j in range(0, len(copyList[0]), 1):
            for symbol in massOfBadSymbols:
                if symbol in copyList[i][j]:
                    copyList[i][j] = copyList[i][j].replace(symbol, '')
    # запятые
    for i in range(0, len(copyList), 1):  # Очистка от груповых артефактов с запятыми
        for j in range(0, len(copyList[0]), 1):
            if copyList[i][j].count(',', 0, len(copyList[i][j])) > 3:
                copyList[i][j] = copyList[i][j].replace(',', '')
                # copyList[i][j] = ''
    return copyList


def csvToList():  # Приведение данных файла к читабельному виду
    with open('media/Тестовое задание Python_Django - import_0945-1 (1) (1).csv',
              'r', newline='\n', encoding='UTF-8') as f:
        reader = csv.reader(f, delimiter=';', quotechar='\r')
        # next(reader)
        # for row in reader:
        #     print(row)
        readerList = list(reader)
        readerList = cleaningData(readerList)

    return readerList


def saveInDatabase(listData):  # Сохранение в БД
    CSVModel.objects.all().delete()
    print(len(listData))
    for i in listData:
        CSVModel.objects.create(code=i[0],
                                name=i[1],
                                lvl1=i[2],
                                lvl2=i[3],
                                lvl3=i[4],
                                price=i[5],
                                priceSP=i[6],
                                amount=i[7],
                                propertyFields=i[8],
                                purchases=i[9],
                                unit=i[10],
                                img=i[11],
                                onGeneral=i[12],
                                description=i[13])


def openCSVFile(request):  # трансфер файла из формы в папку и БД
    # POST - обязательный метод
    if request.method == 'POST' and request.FILES:
        # получаем загруженный файл
        file = request.FILES['filecsv']
        fs = FileSystemStorage()
        # сохраняем на файловой системе
        filename = fs.save(file.name, file)
        saveInDatabase(csvToList())
    return render(request, 'pages/inputpage.html')


def output(request):  # Отображение данных из БД
    modelAllData = CSVModel.objects.all()
    context = {
        'modelAllData': modelAllData,
    }
    return render(request, 'pages/outputpage.html', context)
