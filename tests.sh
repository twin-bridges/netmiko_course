#!/bin/bash

RETURN_CODE=0

echo "pylama ." \
&& pylama . \
&& echo "black" \
&& black --check . \
&& echo "running pytest..." \
&& cd tests \
\
|| RETURN_CODE=1

exit $RETURN_CODE

# && py.test -x -s -v test_class* \
# && py.test -x -s -v test_bonus* \
