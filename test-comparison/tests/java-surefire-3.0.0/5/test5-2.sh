#!/bin/bash

output=$(../../../src/decision.sh)

if [ "$output" == "No new errors in the tests." ]; then
    echo "Assertion succeeded."
else
    echo "Assertion failed."
fi
