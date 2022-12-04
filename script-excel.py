import pandas as pd

dataframe = pd.DataFrame({
  'name': ['Afrid', 'Asif', 'Shoyab'],
  'age': [16, 17, 15]
})

dataframe.to_excel('./students.xlsx', index=False)
dataframe.to_json('./students.json', orient ='split')