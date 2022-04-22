import pandas as pd

def writerXlsx(listAns):
    readDF = pd.read_excel(r'test.xlsx')
    newdf = pd.DataFrame({
        'FavoriteField' : [listAns[0]], 
        'FavoriteCamp': [listAns[1]], 
        'MostImportantThingOfDesigning': [listAns[2]], 
        'Java' : ['yes' if listAns[3] == '1' else 'no' ], 
        'Python' : ['yes' if listAns[4] == '1' else 'no'],
        'SQL' : ['yes' if listAns[5] == '1' else 'no'],
        'Java Script' : ['yes' if listAns[6] == '1' else 'no'],
        'C#' : ['yes' if listAns[7] == '1' else 'no'] 
        })
    frames = [readDF, newdf]
    result = pd.concat(frames)

    writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')

    result.to_excel(writer, index = False)
    writer.save()
    print("save xlsx")
