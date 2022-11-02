import csv

def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    return len(data.split('\n'))


data=open('data.csv').read()
print(find_number_of_columns(data))

# Read the csv file