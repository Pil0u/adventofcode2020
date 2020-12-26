# adventofcode2020
My personal answers to https://adventofcode.com/2020 (when found...)

## Installation & configuration
```bash
pip install -r requirements.txt
```

When you login once to https://adventofcode.com/, the website generates a `session` cookie with a ~ 1-month validity. Copy the value of this cookie and add it to your `.env` file.
```
# .env
SESSION_COOKIE=your-session-cookie
```
**(Optional)** For timings evaluation, you may specify the number of times to repeat the evaluation for each day. It is equal to `1` if not specified in your `.env`.
```
# .env
N_REPEATS=5
```

## Usage

In a shell, you can run:
``` bash
$ python3 run.py -h
usage: run.py [-h] [-t] [-x] [-d DAYS [DAYS ...]]

Run and/or time daily challenges.

optional arguments:
  -h, --help            show this help message and exit
  -d DAYS [DAYS ...], --days DAYS [DAYS ...]
  -t, --timers          get results along with timings
  -x, --no-solutions    get timings only
```

The expected output is a plain dictionary with `days` as keys. Each `day` value is a dictionnary with two keys:
- `solutions`, which value is a tuple of the two solutions of the day `(part_one, part_two)`
- `timers_ms`, which value is a list of timings (in milliseconds) computed `N_REPEATS` times, or once if not specified *(For evalulation purpose and comparability, it is usually recommended to take the `min()` of these values)*

Example of output:
``` bash
$ python3 run.py -t -d 1
{'day1': {'solutions': (964875, 158661360), 'timers_ms': [72.95027375221252, 73.16023111343384, 73.55176508426666, 72.4656879901886, 71.81123793125153, 72.87500202655792, 73.03334474563599, 72.77190089225769, 72.43489027023315, 73.69080483913422]}}
```

### Days format

The `--days` parameter corresponds to the filename you want to run, without the `.py` extension.  
As a shortcut, for any file with the `day<1-25>.py` pattern, you can also pass the integer as parameter.
Example:
``` bash
$ python3 run.py -d day14 12 06
```
will run the solutions for `day14.py`, `day12.py` and `day06.py`.  
The command line is robust to wrong parameters, so
``` bash
$ python3 run.py -d day14 day964 12 50 wrong day06
```
will still run the solutions for `day14.py`, `day12.py` and `day06.py`.

**Note**: If you don't specify the `--days` parameter, it will run for all the days available.


### Day files format

Days available are found within the directory using this regular expression: `^day(0[1-9]|1\d|2[0-5]|[1-9])[^\d\.]*\.py$`

Examples of valid names: `day1.py`, `day06.py`, `day12updated.py`, `day25_alt.py`, `day1_12.py` *(this one matches day \#1)*  
Examples of invalid names: `day00.py`, `day006.py`, `dayalt25.py`, `day_1.py`, `1day.py`, `day26.py` *(until Christmas only!)*

**Important note: daily files must contain a `result(input_)` method defined, otherwise the `day['solutions']` will contain an error**.

---
---

In the following sections, I try to extract the core programming objects and concepts for each day, mostly based on how I solved it.  
Basic strings manipulation is almost always required, the input being a giant string.

## Day 1
Objects: lists/arrays  
Concepts: **combinations**, loops, conditions

## Day 2
Objects: lists/arrays  
Concepts: loops, conditions

## Day 3
Objects : **2D lists/arrays**  
Concepts: **modulo**, loops, conditions

## Day 4
Objects: lists/arrays, dictionnaries/hashes (probably optional), **sets** (probably optional, but so efficient)  
Concepts: loops, **advanced conditions**

Improvement: use DataFrame ;-)

## Day 5
Objects: sets  
Concepts: loops, **base conversion**

## Day 6
Objects: sets  
Concepts: loops, **sets operations**

## Day 7
TODO

## Day 8
Objects: lists/arrays  
Concepts: (infinite) loops, conditions

## Day 9
Objects: lists/arrays  
Concepts: **advanced indexing**, combinations

## Day 10
Objects: lists/arrays  
Concepts: loops, conditions, **some weird modeling for part 2**

## Day 11
Objects: **2D lists/arrays**  
Concepts: **advanced 2D lists/arrays manipulation**

## Day 12
TODO
