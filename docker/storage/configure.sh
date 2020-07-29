set -x
set -m

USER=${STORAGE_USER}
PASSWORD=${STORAGE_PASSWORD}

/entrypoint.sh couchbase-server &

# TODO: Should be replaced with successful curl on http://127.0.0.1:8091
sleep 15

curl -v -X POST http://127.0.0.1:8091/pools/default -d memoryQuota=512 -d indexMemoryQuota=512
curl -v http://127.0.0.1:8091/node/controller/setupServices -d services=kv%2Cn1ql%2Cindex
curl -v http://127.0.0.1:8091/settings/web -d port=8091 -d username="${USER}" -d password="${PASSWORD}"
curl -i -u "${USER}":"${PASSWORD}" -X POST http://127.0.0.1:8091/settings/indexes -d 'storageMode=forestdb'

fg 1
