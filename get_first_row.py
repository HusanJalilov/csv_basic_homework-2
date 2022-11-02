def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   rows=data.split('\n')
   s=[]
   for i in rows[1:]:
       s.append(i.split(',')[0])
   return s
    
# Read the csv file

data=open('data.csv').read()
print(get_first_row(data))
