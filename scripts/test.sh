#!/bin/bash

for f in $(ls);
do
  echo "$f"
  echo "scripts"
  if ["$f" == "scripts"]; then
    echo "in"
    cd scripts/
fi
done
pwd
