#!/bin/bash

v_fold=5
#validate for C-svm
svm_type=0
train_data='./data/normalized_train_data2'
test_data='./data/normalized_test_data2'

read -p "select kernel degree: " kernel_degree
for gamma in '0.0025' '0.005' '0.0075' '0.01' '0.0125'
do
    for cost in '0.05' '0.075' '0.1' '0.125' '0.15' '0.175'
    do
	commandToRun="./libsvm-3.17/svm-train -s $svm_type -t 1 -d $kernel_degree -g $gamma -c $cost -v $v_fold $train_data"
	echo $commandToRun >> validation.result
	$commandToRun|grep 'Cross Validation Accuracy' >> validation.result
    done
done
