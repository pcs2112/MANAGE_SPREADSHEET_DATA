import xlrd


def read_workbook(file_path):
    """ Returns the workbook instance for the specified file. """
    return xlrd.open_workbook(file_path)


def read_workbook_columns(wb, sheet_index=0):
    """ Returns a list of columns for the specified workbook sheet. """
    sheet = wb.sheet_by_index(sheet_index)
    columns = []
    
    for i in range(sheet.ncols):
        value = sheet.cell_value(0, i)
        if isinstance(value, str):
            value = value.strip()
        columns.append(value)
    
    return columns


def read_workbook_data(wb, sheet_index=0):
    """
    Returns the specified workbook sheet's data as an array of objects
    using the header columns as the keys
    """
    header_columns = read_workbook_columns(wb, sheet_index)
    sheet = wb.sheet_by_index(sheet_index)
    num_columns = sheet.ncols
    num_rows = sheet.nrows
    data = []
    
    for row in range(1, num_rows):
        obj = {}
        for col in range(num_columns):
            value = sheet.cell_value(row, col)
            if isinstance(value, str):
                value = value.strip()
            obj[header_columns[col]] = value
        
        data.append(obj)
    
    return data
