# Actividad-1
# DFA State Equivalence Checker

## Group Members
- Jose Manuel Carvajal Aristizabal
- Miguel Angel Montoya

## System and Tools Versions
- Operating System: [Windows 11]
- Programming Language: Python 3.8+
- Tools: no one (at the beggining we used sublime text but at the end no because it was more easier for us)

## Running the Implementation

### Prerequisites
Ensure you have Python installed. You can check your Python version by running:
```bash
python --version

##Instructions
git clone https://github.com/your-repo-url.git
cd your-repo-url
or: Save the code in one part of your computer, les said that in owr case is: PS C:\Users\57304\Downloads\DFA_Minimization> & C:/Users/57304/AppData/Local/Programs/Python/Python312/python.exe c:/Users/57304/Downloads/DFA_Minimization/dfa_minimizacion_interactivo.py

#Example of use:
Input
4
6
a b
1 2 5
0 1 2
1 3 4
2 4 3
3 5 5
4 5 5
5 5 5
6
a b
3 4 5
0 1 2
1 3 4
2 4 3
3 5 5
4 5 5
5 5 5
6
a
1 4
0 1
1 2
2 3
3 4
4 5
5 0
4
a b
0 1
0 1 2
1 1 2
2 3 1
3 3 3
Output
(1, 2) (3, 4)
(1, 2) (3, 4) (3, 5) (4, 5)
(0, 3) (1, 4) (2, 5)
(0, 1)
This is what is going to show our code with this input, obviosly we have to said that this input and this output can be checked using our code.

##Example of use
Menu:
1. Read DFA input
2. Find equivalent states
3. Exit
Select an option: 1
Please enter the number of cases: 1
Please enter the number of states: 3
Please enter the alphabet (space-separated): a b
Please enter the final states (space-separated): 2
Please enter transitions for state 0: 1 2
Please enter transitions for state 1: 0 2
Please enter transitions for state 2: 2 2
DFA cases read successfully.

Menu:
1. Read DFA input
2. Find equivalent states
3. Exit
Select an option: 2
Equivalent states: (0, 1)

