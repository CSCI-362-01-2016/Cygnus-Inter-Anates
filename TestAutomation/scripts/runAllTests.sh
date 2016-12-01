#!/bin/bash

cd scripts/

sh jython.sh runTests.py

cd ../reports/
xdg-open testReport.html
