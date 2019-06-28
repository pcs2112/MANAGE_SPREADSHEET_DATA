import os
import csv

from src.config import get_config
from src.excel_utils import read_workbook, read_workbook_data


def process_orders_spreadsheet_data(file, prefix='i-dan', seq=1, sheet=0):
    if os.path.exists(file) is False:
        raise FileExistsError(f"{file} is an invalid file.")

    seq = int(seq)
    sheet = int(sheet)

    print('')

    config = get_config()

    wb = read_workbook(file)
    
    rows = read_workbook_data(wb, sheet)
    
    curr_batch_index = -1
    batches = []
    batch_idx = {}
    curr_batch = None
    
    for row_num, row in enumerate(rows):
        if row['QTY'] == '':
            if curr_batch is not None:
                batches.append(curr_batch.copy())
                
            curr_batch_index += 1
            batch_idx[curr_batch_index] = seq
            curr_batch = [['SKU', 'QTY']]

            seq += 1
            continue
        
        curr_batch.append([int(row['SKU']), round(row['QTY'])])

    if curr_batch is not None:
        batches.append(curr_batch.copy())

    for batch_num, batch in enumerate(batches):
        with open(f"{config['OUT_DIR']}/{prefix}-{batch_idx[batch_num]}.csv", 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(batch)

        writeFile.close()
