import pandas as pd

def writerXlsx(listAns):
    readDF = pd.read_excel(r'test.xlsx')
    newdf = pd.DataFrame({
        'FavouriteField' : [listAns[0]], 
        'FavouriteCamp': [listAns[1]], 
        'Important': [listAns[2]], 
        'Java' : [listAns[3]], 
        'Python' : [listAns[4]],
        'SQL' : [listAns[5]],
        'Java Script' : [listAns[6]],
        'C#' : [listAns[7]] 
        })
    frames = [readDF, newdf]
    result = pd.concat(frames)

    writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')

    result.to_excel(writer, index = False)
    writer.save()
    print("save xlsx")
