#!/bin/bash

RETURN_CODE=0

echo "pylama ." \
&& pylama . \
&& echo "black" \
&& black --check . \
&& echo "running pytest..." \
&& cd tests \
&& py.test -x -s -v test_class1.py \
&& py.test -x -s -v test_class2.py \
&& py.test -x -s -v test_class3.py \
&& py.test -x -s -v test_class4.py \
&& py.test -x -s -v test_class5.py \
&& py.test -x -s -v test_class6.py \
&& py.test -x -s -v test_class7.py \
&& py.test -x -s -v test_class8.py \
&& py.test -x -s -v test_class9.py \
&& py.test -x -s -v test_class10.py \
&& py.test -x -s -v test_class11.py \
&& py.test -x -s -v test_class12.py \
&& py.test -x -s -v test_bonus1.py \
\
|| RETURN_CODE=1

exit $RETURN_CODE
