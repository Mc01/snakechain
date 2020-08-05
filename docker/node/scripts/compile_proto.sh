#!/usr/bin/env bash
PROTO_DIR="/app/blockchain/server/proto/"
OUTPUT_DIR="/app/blockchain/server/proto/python"
protoc -I ${PROTO_DIR} --python_betterproto_out=${OUTPUT_DIR} block.proto element.proto stats.proto
