#!/usr/bin/env bash
set -ex

cd main

export PYTHONPATH=.

module=$1
args="${@:2}"

cmd="pytest -s -l -v ${module} --url=https://devdivision.io --alluredir /tmp/work/alluredir ${args}"

if [ -n "${KEYWORD}" ]; then
    cmd="${cmd} -k ${KEYWORD}"
fi

if [ -n "${TEST_THREADS}" ]; then
    cmd="${cmd} -n ${TEST_THREADS}"
fi

$cmd || e=$? && chmod -R 777 /tmp/work; exit $e
