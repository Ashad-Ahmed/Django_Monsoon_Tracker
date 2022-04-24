import pandas as pd

class GetData:

    def GetDataFrame():
        
        df = pd.read_excel(r'myapp/SampleData.xlsx')
        lables = df[df.columns[0]].to_list()
        data   = list(df[df.columns[1:]].T.to_dict().values())

        return data, lables

GetData.GetDataFrame()