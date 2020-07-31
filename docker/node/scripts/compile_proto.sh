#!/usr/bin/env bash
PROTO_DIR="/app/blockchain/server/proto/"
protoc -I ${PROTO_DIR} --python_betterproto_out=python hello.proto
