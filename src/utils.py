from datetime import datetime


def format_number(number):
	return "{:,}".format(number)


def get_now_datetime(date_format='%Y-%m-%d %H:%M:%S'):
	return datetime.now().strftime(date_format)
