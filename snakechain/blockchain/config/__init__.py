import os

# redis for buffer
REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = os.environ.get('REDIS_PORT')

# blockchain memory capacity
NUMBER_OF_BLOCKS_IN_MEMORY = int(os.environ.get(
    'NUMBER_OF_BLOCKS_IN_MEMORY',
    default=10,
))

# storage for ledger
BLOCKCHAIN_STORAGE_FILE = os.environ.get(
    'BLOCKCHAIN_STORAGE_FILE',
    default='storage/ledger.json',
)

# node stdout spacer
SPACER = os.environ.get(
    'SPACER',
    default='------*------*------*------*------*------',
)
