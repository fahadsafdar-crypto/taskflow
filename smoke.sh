#!/bin/bash
set -e
curl -sf http://127.0.0.1:8000/health
curl -sf -X POST http://127.0.0.1:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"smoke"}'
curl -sf http://127.0.0.1:8000/tasks | grep smoke
echo OK
