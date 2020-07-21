#!/usr/bin/env bash
uvicorn --host 0.0.0.0 --workers 4 rest:api --reload
