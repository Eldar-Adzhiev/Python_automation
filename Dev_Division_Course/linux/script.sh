#!/usr/bin/env bash

#set -e
#set -x
#echo 12345


param1=$1
param2=$2
param_all=$@


echo $param1
echo $param2
echo $param_all

procs1=$(ps axuwf)
procs2=`ps axuwf`

echo $procs1

echo --------------

echo "${procs2//root/kirillov}"

echo ---------
echo "${procs2^^}"


echo ------
echo "${fkjdsfjkdsfjkdsfjks:-DEFAULT}"




echo -------
pids=$(ps axuwf | grep root | awk '{print $2}')

echo "${pids}"

for pid in $pids; do

   if [[ ! "${pid}" =~ "6" ]]; then
       echo "CURR PID: ${pid}"
   fi

done

echo --------

ls -la fdsklfjsdlkfkldsjfkldsjfkljdslkfjsdfkl
ls -la 12345



echo ------

func() {
    local param1=$1
    local param_all=$@

    echo $param1
    echo $param_all
}


func 123 456
func 666 777

res=$(func 999 999 999)
echo "${res}"


cmd="ps axuwf | grep root"
echo "${cmd}"

$cmd
