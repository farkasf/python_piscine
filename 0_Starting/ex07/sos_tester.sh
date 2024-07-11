#!/bin/bash

RED='\033[0;31m'
B_RED='\033[1;31m'
NC='\033[0m'

echo "----------------------------------------------------------------------"
echo -e "${B_RED}CASE 1:${NC} testing sos.py with ${RED}\"sos\"${NC}"
echo "----------------------------------------------------------------------"
python3 sos.py 'sos' | cat -e
echo

echo "----------------------------------------------------------------------"
echo -e "${B_RED}CASE 2:${NC} testing sos.py with ${RED}\"h\$llo\"${NC}"
echo "----------------------------------------------------------------------"
python3 sos.py 'h$llo'
echo

echo "----------------------------------------------------------------------"
echo -e "${B_RED}CASE 3:${NC} testing sos.py with ${RED}an empty string${NC}"
echo "----------------------------------------------------------------------"
python3 sos.py ''
echo

echo "----------------------------------------------------------------------"
echo -e "${B_RED}CASE 4:${NC} testing sos.py with ${RED}\"sos\" and \"sos\"${NC}"
echo "----------------------------------------------------------------------"
python3 sos.py 'sos' 'sos'
echo

echo "----------------------------------------------------------------------"
echo -e "${B_RED}CASE 5:${NC} testing sos.py with ${RED}\"Hello World\"${NC}"
echo "----------------------------------------------------------------------"
echo "expected: .... . .-.. .-.. --- / .-- --- .-. .-.. -.." | cat -e
echo -n "output:   "
python3 sos.py 'Hello World' | cat -e
echo

echo "----------------------------------------------------------------------"
echo -e "${B_RED}CASE 6:${NC} testing sos.py with ${RED}\"Marvin 42\"${NC}"
echo "----------------------------------------------------------------------"
echo "expected: -- .- .-. ...- .. -. / ....- ..---" | cat -e
echo -n "output:   "
python3 sos.py 'Marvin 42' | cat -e
echo

echo "----------------------------------------------------------------------"
echo -e "${B_RED}CASE 7:${NC} testing sos.py with ${RED}\"L O L\"${NC}"
echo "----------------------------------------------------------------------"
echo "expected: .-.. / --- / .-.." | cat -e
echo -n "output:   "
python3 sos.py 'L O L' | cat -e
echo

echo "----------------------------------------------------------------------"
echo -e "${B_RED}CASE 8:${NC} testing sos.py with ${RED}\"řeřicha\"${NC}"
echo "----------------------------------------------------------------------"
python3 sos.py 'řeřicha'
echo

echo "----------------------------------------------------------------------"
echo -e "${B_RED}CASE 9:${NC} testing sos.py with ${RED}\"3xpl01t m3\"${NC}"
echo "----------------------------------------------------------------------"
echo "expected: ...-- -..- .--. .-.. ----- .---- - / -- ...--" | cat -e
echo -n "output:   "
python3 sos.py '3xpl01t m3' | cat -e
echo

echo "----------------------------------------------------------------------"
echo -e "${B_RED}CASE 10:${NC} testing sos.py with ${RED}\"123 456 789\"${NC}"
echo "----------------------------------------------------------------------"
echo "expected: .---- ..--- ...-- / ....- ..... -.... / --... ---.. ----." | cat -e
echo -n "output:   "
python3 sos.py '123 456 789' | cat -e
echo
