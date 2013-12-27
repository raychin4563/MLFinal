#!/bin/bash

v_fold=5
#validate for C-svm
svm_type=0
train_data='./data/trainDataWithNormalizedDis'
test_data='./data/testDataWithNormalizedDis'

read -p "select kernel degree: " kernel_degree
for gamma in '0.0025' '0.005' '0.0075' '0.01' '0.0125' '0.015'
do
    for cost in '0.05' '0.075' '0.1' '0.125' '0.15' '0.175' '0.2'
    do
	commandToRun="./libsvm-3.17/svm-train -s $svm_type -t 1 -d $kernel_degree -g $gamma -c $cost -v $v_fold $train_data"
	echo $commandToRun >> "validation.result.d$kernel_degree"
	$commandToRun|grep 'Cross Validation Accuracy' >> "validation.result.d$kernel_degree"
    done
done
