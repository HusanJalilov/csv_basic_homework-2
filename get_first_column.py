def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    return data.split('\n')[1].split(',')
    
# Read the csv file

data=open('data.csv').read()
print(get_first_column(data))
