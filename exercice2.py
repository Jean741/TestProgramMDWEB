#import des bibliotheques
import json
import os
import xlrd
import numpy as np


def saveJsonTofile(filename,donnees):
    with open(filename.split(".")[0]+'.json', "w+") as jsonFile:
        json.dump(donnees, jsonFile)

def getJsonFromExel(filename,start_line,end_line):
    #Ouverture du document Excel
    workbook = xlrd.open_workbook(filename)
    SheetNameList = workbook.sheet_names()


    #Recupération de la premiere feuille du document
    worksheet = workbook.sheet_by_name(SheetNameList[0])

    #Definitions des parameres de l'exercice le traitement concerne la ligne 4 a la ligne 32
    num_rows = end_line
    curr_row = start_line
    liste_Of_Items=[]
    order = 0
    while curr_row < num_rows:
        item={}
        item["order"]= order    
        row = worksheet.row(curr_row)
        # Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
        if worksheet.cell_type(curr_row, 2) == 1:
            item["type"]= "CELL"
            item["description"]= worksheet.cell_value(curr_row, 1)
            item["unity"]= worksheet.cell_value(curr_row, 2)
            item["quantity"]= int(worksheet.cell_value(curr_row, 3))
            if worksheet.cell_type(curr_row, 0) == 1:
                 item["reference"]= worksheet.cell_value(curr_row, 0)
        else:
            item["type"]= "SECTION"
            item["reference"]= worksheet.cell_value(curr_row, 0)
            item["level"]= 1
            item["description"]= worksheet.cell_value(curr_row, 1)
        if worksheet.cell_type(curr_row, 1) == 1:
            liste_Of_Items.append(item)
            order+=1
        curr_row += 1
    #Creation du json
    donnees = {}
    donnees["items"]=liste_Of_Items
    return donnees


def convertExelFileToJson(filename,start_line,end_line):
    saveJsonTofile(filename,getJsonFromExel(filename,start_line,end_line))
    


convertExelFileToJson('test.xlsx',3,32)