def readCSVMartix(fileName):
    fin=open(fileName)
    data=[]
    lines=fin.readlines()
    for line in lines:
        data.append(line.split(","))
    fin.close()
    return data

def readCSVMatrixWithSelection(fileName,selectedRows):
    fin=open(fileName)
    data=[]
    lines=fin.readlines()
    for line in lines:
        unselected = line.split(",")
        selectedLine=[]
        for i in selectedRows:
            selectedLine.append(unselected[i])
        data.append(selectedLine)
    fin.close()
    return data
def readCSVMatrixWithSelectionAndBeginning(fileName,selectedRows,beginning):
    fin=open(fileName)
    data=[]
    index=0
    lines=fin.readlines()
    for line in lines:
        if(index<beginning):
            index+=1
            continue
        unselected = line.split(",")
        selectedLine=[]
        for i in selectedRows:
            selectedLine.append(unselected[i])
        data.append(selectedLine)
        index+=1
    fin.close()
    return data
def readCSVMatrixWithSelectionAndBeginningAndDivided(fileName,selectedRows,beginning,labelRow):
    fin =open(fileName)
    data = []
    label=[]
    index = 0
    lines = fin.readlines()
    for line in lines:
        if (index < beginning):
            index += 1
            continue
        unselected = line.split(",")
        selectedLine = []
        for i in selectedRows:
            selectedLine.append(unselected[i])
        data.append(selectedLine)
        label.append(unselected[labelRow])
        index += 1
    fin.close()
    return data,label

def readCSVMatrixWithSelectionAndBeginningAndDividedAsNumber(fileName,selectedRows,beginning,labelRow):
    fin =open(fileName)
    data = []
    label=[]
    index = 0
    lines = fin.readlines()
    for line in lines:
        if (index < beginning):
            index += 1
            continue
        unselected = line.split(",")
        selectedLine = []
        for i in selectedRows:
            selectedLine.append(float(unselected[i]))
        data.append(selectedLine)
        label.append(int(unselected[labelRow]))
        index += 1
    fin.close()
    return data,label
def readCSVMatrixWithSelectionAndBeginningAsNumber(fileName,selectedRows,beginning):
    fin=open(fileName)
    data=[]
    index=0
    lines=fin.readlines()
    for line in lines:
        if(index<beginning):
            index+=1
            continue
        unselected = line.split(",")
        selectedLine=[]
        for i in selectedRows:
            selectedLine.append(float(unselected[i]))
        data.append(selectedLine)
        index+=1
    fin.close()
    return data