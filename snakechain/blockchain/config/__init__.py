import os

# redis as buffer
BUFFER_HOST = os.environ.get("BUFFER_HOST")
BUFFER_PORT = os.environ.get("BUFFER_PORT")

# couchbase as storage
STORAGE_HOST = os.environ.get("STORAGE_HOST")
STORAGE_USER = os.environ.get("STORAGE_USER")
STORAGE_PASSWORD = os.environ.get("STORAGE_PASSWORD")
STORAGE_BUCKET = os.environ.get("STORAGE_BUCKET", default="default",)
STORAGE_BLOCK_COLLECTION = "blocks"
STORAGE_CONFIG_COLLECTION = "config"
STORAGE_LATEST_KEY = "latest"
STORAGE_BUCKET_CREATION_DELAY = 5
STORAGE_BUCKET_CREATION_MAX_RETRIES = 6

# genesis block hash
GENESIS_HASH = "0x0"

# blockchain memory capacity
NUMBER_OF_BLOCKS_IN_MEMORY = int(
    os.environ.get("NUMBER_OF_BLOCKS_IN_MEMORY", default=10,)
)

# node stdout spacer
SPACER = os.environ.get("SPACER", default="------*------*------*------*------*------",)
