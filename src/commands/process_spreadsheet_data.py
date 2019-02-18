import os
import ntpath
from src.config import get_config
from src.csv_utils import read_workbook_columns, read_workbook_data
from src.mssql_connection import init_db, close, execute_sp
from src.utils import format_number


def process_spreadsheet_data(file):
	if os.path.exists(file) is False:
		raise FileExistsError(f"{file} is an invalid file.")

	# Init DB connection
	config = get_config()
	db_config = {
		'DB_SERVER': config['DB_SERVER'],
		'DB_NAME': config['DB_NAME'],
		'DB_USER': config['DB_USER'],
		'DB_PASSWORD': config['DB_PASSWORD'],
		'DB_DRIVER': config['DB_DRIVER'],
		'DB_TRUSTED_CONNECTION': config['DB_TRUSTED_CONNECTION']
	}

	init_db(db_config)

	filename = ntpath.basename(file)
	filepath = ntpath.dirname(file)
	total = 0
	insert_count = 0
	update_count = 0
	error_count = 0

	# CSV file columns
	columns = read_workbook_columns(file)

	# CSV file rows
	rows = read_workbook_data(file)

	print(f"Processing ...")

	for row_num, row in enumerate(rows):
		for col_pos, col in enumerate(columns):
			result = execute_sp('MWH_FILES.MANAGE_CSV_DATA', {
				'message': 'SAVE',
				'PATH': filepath,
				'FILE_NAME': filename,
				'COLUMN_NAME': col,
				'COLUMN_POSITION': str(col_pos + 1),
				'ROW_NUMBER': str(row_num + 1),
				'VALUE': row[col_pos]
			}, 'RETURN_FLG')

			result_count = len(result)
			processed = result[result_count - 1][0][0]
			
			total += 1

			if processed == 1:
				insert_count += 1
			elif processed == 2:
				update_count += 1
			else:
				error_count += 1

	# Close DB connection
	close()

	print("")
	print(f"TOTAL: {format_number(total)}")
	print(f"INSERT COUNT: {format_number(insert_count)}")
	print(f"UPDATE COUNT: {format_number(update_count)}")
	print(f"ERROR COUNT: {format_number(error_count)}")
