#!/bin/sh

export APP=${APP-backend.main:backend}

exec python -m uvicorn --reload "$APP"
