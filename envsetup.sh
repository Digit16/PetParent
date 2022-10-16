#!/bin/bash

if [-d "venv"]
then
  echo "Python venv folder already exists"
else
  python3 -m venv venv
fi
