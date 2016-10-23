#!/bin/bash

sh jython.sh runTests.py

cd ../reports/
xdg-open report.html
