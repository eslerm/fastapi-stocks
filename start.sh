#!/bin/sh

exec python -m uvicorn --reload backend.main:app
