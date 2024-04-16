import pandas as pd


# lst - список списков строк
# 'head.csv' - заголовки разделенные ;
def create_csv(lst,filename):
    try:
        df = pd.read_csv('head.csv',delimiter=';')
        if len(lst[0])!= df.shape[1]:
            print("Error: Количество строк и столбцов не совпадают")
        else:
            for x in range(len(lst)):
                df.loc[x] = lst[x]
            df.to_csv(filename,index=False)
    except Exception as e:
        print(e)
    
test = create_csv([[11,21,31,41,51,61,71],[12,22,32,42,52,62,72],[13,23,33,43,53,63,73],[14,24,34,44,54,64,74],[15,25,35,45,55,65,75]],"test.csv")
    
