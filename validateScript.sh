#!/bin/bash

v_fold=5
#first validate for C-svm
svm_type=0
train_data='./data/'
test_data='./data'

for kernel_degree in '1' '2' '3' '4'
do
    for gamma in '0.005' '0.0075' '0.01' '0.0125' '0.015' '0.02'
    do
	for cost in '0.075' '0.1' '0.125' '0.15' '0.175' '0.2' '0.225'
	do
	    commandToRun="./libsvm-3.17/svm-tran -s $svm_type -t 1 -d $kernel_degree -g $gamma -c $cost -v $v_fold $train_data"
	    echo $commandToRun >> validation.result
	    $commandToRun|grep 'Cross Validation Accuracy' >> validation.result
	done
    done
done
