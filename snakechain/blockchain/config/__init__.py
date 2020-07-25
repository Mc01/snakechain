import os

# redis for buffer
BUFFER_HOST = os.environ.get('BUFFER_HOST')
BUFFER_PORT = os.environ.get('BUFFER_PORT')

# couchbase for storage
STORAGE_HOST = os.environ.get('STORAGE_HOST')
STORAGE_USER = os.environ.get('STORAGE_USER')
STORAGE_PASSWORD = os.environ.get('STORAGE_PASSWORD')

# blockchain memory capacity
NUMBER_OF_BLOCKS_IN_MEMORY = int(os.environ.get(
    'NUMBER_OF_BLOCKS_IN_MEMORY',
    default=10,
))

# node stdout spacer
SPACER = os.environ.get(
    'SPACER',
    default='------*------*------*------*------*------',
)
