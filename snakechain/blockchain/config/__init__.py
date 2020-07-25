import os

# redis for buffer
BUFFER_HOST = os.environ.get('BUFFER_HOST')
BUFFER_PORT = os.environ.get('BUFFER_PORT')

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
