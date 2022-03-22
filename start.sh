#!/bin/sh

export APP=${APP-app.main:app}

exec python -m uvicorn --reload "$APP"
