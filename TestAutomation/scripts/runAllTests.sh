#!/bin/bash

cd TestAutomation/scripts/

sh jython.sh runTests.py

cd ../reports/
xdg-open testReport.html
