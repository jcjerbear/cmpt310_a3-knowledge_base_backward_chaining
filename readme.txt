readme.txt
1)run main.py with "python3.4 main.py" command in terminal on a CSIL machine
2)please run my code with Python3.0 or above
3)before running the python file, make sure you have testing data ready in "data.txt" file

data set in the "data.txt" file has to be in the following exmaple's format:
example 1 below is already given in the "data.txt" file
please change the data in "input.txt" file if further testing is needed

example 1:
r
p
q p
r p q
r s

example 2:
a
p
q p
d
g q j
e f
c f d
c d g
c e d
b j
a b c
j

4)example of code output:
Query: r
Adding query into goals...

goals: r
Current searching head: r
Rest of goals: NULL
Chosen rule we are looking at right now: pʌq => r
Rule body: pʌq
Append these atoms into goals...
goals after append: p,q

goals: p,q
Current searching head: p
Rest of goals: q
Chosen rule we are looking at right now: p
Message: p is a FACT
Rule body: NULL
Append these atoms into goals...
goals after append: q

goals: q
Current searching head: q
Rest of goals: NULL
Chosen rule we are looking at right now: q
Message: q is a FACT
Rule body: NULL
Append these atoms into goals...
goals after append:

goals:
goal is NULL
This KB is True