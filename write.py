import pandas as pd
import xlsxwriter

def writerXlsx(listAns):
    df = pd.DataFrame({
        'FavoriteField' : [listAns[0]], 
        'FavoriteCamp': [listAns[1]], 
        'MostImportantThingOfDesigning': [listAns[2]], 
        'Java' : ['yes' if listAns[3] == '1' else 'no' ], 
        'Python' : ['yes' if listAns[4] == '1' else 'no'],
        'SQL' : ['yes' if listAns[5] == '1' else 'no'],
        'Java Script' : ['yes' if listAns[6] == '1' else 'no'],
        'C#' : ['yes' if listAns[7] == '1' else 'no'] 
        })
    
    writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')
    
    df.to_excel(writer, index = False)
    writer.save()
    print("save xlsx")
