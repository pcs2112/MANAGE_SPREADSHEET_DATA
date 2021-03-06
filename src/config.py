"""Application configuration."""
import os
from dotenv import load_dotenv

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# load dotenv
dotenv_path = os.path.join(ROOT_DIR, '.env')
load_dotenv(dotenv_path)

# Source IN dir
IN_DIR = os.path.join(ROOT_DIR, 'in')

# Source OUT dir
OUT_DIR = os.path.join(ROOT_DIR, 'out')

# Set the settings
config = {
	'DB_SERVER': os.getenv('DB_HOST'),
	'DB_NAME': os.getenv('DB_NAME'),
	'DB_USER': os.getenv('DB_USER'),
	'DB_PASSWORD': os.getenv('DB_PASSWORD'),
	'DB_DRIVER': os.getenv('DB_DRIVER'),
	'DB_TRUSTED_CONNECTION': os.getenv('DB_TRUSTED_CONNECTION') == '1',
	'ROOT_DIR': ROOT_DIR,
	'IN_DIR': IN_DIR,
	'OUT_DIR': OUT_DIR
}


def get_config():
	return config
