#!/bin/bash

RED='\033[0;31m'
B_RED='\033[1;31m'
NC='\033[0m'

echo "----------------------------------------------------------------------"
echo -e "${B_RED}CASE 1:${NC} testing filterstring.py with ${RED}\"Hello world\" and 4${NC}"
echo "----------------------------------------------------------------------"
python3 filterstring.py "Hello World" 4
echo

echo "----------------------------------------------------------------------"
echo -e "${B_RED}CASE 2:${NC} testing filterstring.py with ${RED}\"Hello world\" and 99${NC}"
echo "----------------------------------------------------------------------"
python3 filterstring.py "Hello World" 99
echo

echo "----------------------------------------------------------------------"
echo -e "${B_RED}CASE 3:${NC} testing filterstring.py with ${RED}3 and \"Hello world\"${NC}"
echo "----------------------------------------------------------------------"
python3 filterstring.py 3 "Hello World"
echo

echo "----------------------------------------------------------------------"
echo -e "${B_RED}CASE 4:${NC} testing filterstring.py with ${RED}no arguments${NC}"
echo "----------------------------------------------------------------------"
python3 filterstring.py
echo

echo "----------------------------------------------------------------------"
echo -e "${B_RED}CASE 5:${NC} testing filterstring.py with ${RED}\"Hello world\", 4 and 2${NC}"
echo "----------------------------------------------------------------------"
python3 filterstring.py "Hello World" 4 2
echo

echo "----------------------------------------------------------------------"
echo -e "${B_RED}CASE 6:${NC} testing filterstring.py with ${RED}\"This is Marvin speaking\" and 5${NC}"
echo "----------------------------------------------------------------------"
python3 filterstring.py "This is Marvin speaking" 5
echo

echo "----------------------------------------------------------------------"
echo -e "${B_RED}CASE 7:${NC} testing filterstring.py with ${RED}\"This is Marvin speaking\" and 4.2${NC}"
echo "----------------------------------------------------------------------"
python3 filterstring.py "This is Marvin speaking" 4.2
echo

echo "----------------------------------------------------------------------"
echo -e "${B_RED}CASE 8:${NC} testing filterstring.py with ${RED}\"The permanent dentition is\ncomposed of 32 teeth\" and 8${NC}"
echo "----------------------------------------------------------------------"
python3 filterstring.py "The permanent dentition is composed of 32 teeth" 8
echo

echo "----------------------------------------------------------------------"
echo -e "${B_RED}CASE 9:${NC} testing filterstring.py with ${RED}\"Hello      World\" 3${NC}"
echo "----------------------------------------------------------------------"
python3 filterstring.py "Hello      world" 3
echo

echo "----------------------------------------------------------------------"
echo -e "${B_RED}CASE 10:${NC} testing filterstring.py with ${RED}an empty string and 200${NC}"
echo "----------------------------------------------------------------------"
python3 filterstring.py "" 200
echo
