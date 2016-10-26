Nicholas Vrontakis, Patrick Kwong, and Cas Donoghue 
# CS325-400 Group 31 Project 2 README

## Running the Program
1. Put the makeChange.py program file in the same directory as your input file.
2. Run makeChange.py on the command line with your specific [input filename].txt

   ```
   python makeChange.py Amount.txt
   ```
3. The program will write the results to a file named: [input filename]change.txt

NOTE: The Algorithm changeslow is very slow. We recommend using amount values 40 and lower. For example with coin demonations of 1, 5, 10, 25, 50, it took about 75 seconds to make change for amount of 65.

## Input File Format
NOTE: The input file has to be in the following format. The Amount.txt file has been included as an example. It contains sample values from the example and the Testing for correctness section. The algorithms were tested and all the algorithms returned the correct output.

   ```
   [array of coin values separated by a comma and a space]
   amount of change to make
   ```
