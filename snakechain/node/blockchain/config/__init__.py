# blockchain memory size
import os

NUMBER_OF_BLOCKS_IN_MEMORY = 10

# storage for ledger
BLOCKCHAIN_STORAGE_FILE = 'storage/ledger.json'

# node stdout spacer
SPACER = '------*------*------*------*------*------'

# redis for buffer
REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = os.environ.get('REDIS_PORT')
