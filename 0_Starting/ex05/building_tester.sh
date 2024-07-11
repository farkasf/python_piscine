#!/bin/bash

RED='\033[0;31m'
B_RED='\033[1;31m'
NC='\033[0m'

test_cases=("Marvin@42.fr" "..@.. +.% .[.. .~. -]--" "aBcD42 !" "write(1, &str[i], 1)")

echo "----------------------------------------------------------------------"
echo -e "${B_RED}CASE 0:${NC} testing building.py with ${RED}\"Python 3.0, released in 2008, was a\nmajor revision that is not completely backward-compatible with earlier\nversions. Python 2 was discontinued with version 2.7.18 in 2020.\"${NC}"
echo "----------------------------------------------------------------------"
python3 building.py "Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."

for ((i=0; i<${#test_cases[@]}; i++)); do
	input_string="${test_cases[i]}"
		
	echo "----------------------------------------------------------------------"
	echo -e "${B_RED}CASE $((i+1)):${NC} testing building.py with ${RED}\"$input_string\"${NC}"
	echo "----------------------------------------------------------------------"
	python3 building.py "$input_string"

done

echo "----------------------------------------------------------------------"
echo -e "${B_RED}CASE 5:${NC} testing building.py with ${RED}\"multiple\" \"inputs\"${NC}"
echo "----------------------------------------------------------------------"
python3 building.py "multiple" "inputs"

echo "----------------------------------------------------------------------"
echo -e "${B_RED}CASE 6:${NC} testing building.py with ${RED}\"A \\\t\\\3\\\0\"${NC}"
echo "----------------------------------------------------------------------"
python3 building.py $'A\t\r\0'

echo "----------------------------------------------------------------------"
echo -e "${B_RED}CASE 7:${NC} testing building.py with ${RED}\"toto\\\n\"${NC}"
echo "----------------------------------------------------------------------"
python3 building.py $'toto\n'
