# adventofcode2020
My personal answers to https://adventofcode.com/2020 (when found...)

## How to use

When you login once to https://adventofcode.com/, the website generates a `session` cookie with a ~ 1-month validity. You need to add a `SESSION_COOKIE` environment variable with that value for the code to work on your inputs.

### Run on one specific day
In a shell, run:
``` bash
python3 run.py <day>
```
`day` is an integer corresponding to the day you want to execute. The result with your input is then printed to you as a tuple, containing both answers for part 1 and part 2 of the daily challenge.

Example with my input:
``` bash
~$ python3 run.py 1
(964875, 158661360)
```

### (WIP) Run every day at once
In a shell, run:
``` bash
python3 run_all.py
```
This will not only execute solutions for all available days, it will also compute running times using `timeit`.
To improve measurements, you can add the environment variable `N_REPEATS` to repeat calculations and get the best timing. This value is 1 by default (i.e. played only once).

---

In the following sections, I try to extract the core programming objects and concepts for each day, mostly based on how I solved it.

## Day 1
Objects: lists/arrays  
Concepts: **combinations**, loops, conditions

## Day 2
Objects: lists/arrays, strings  
Concepts: loops, conditions

## Day 3
Objects : **2D lists/arrays**, strings  
Concepts: **modulo**, loops, conditions

## Day 4
Objects: lists/arrays, strings, dictionnaries/hashes (probably optional), **sets** (probably optional, but so efficient)  
Concepts: basic loops, **advanced conditions**

## Day 5
TODO
