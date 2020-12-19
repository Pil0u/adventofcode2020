import argparse
import importlib
import os
import re
import requests
import sys
import timeit

from dotenv import load_dotenv

load_dotenv()
SESSION_COOKIE = os.getenv('SESSION_COOKIE')
N_REPEATS = int(os.getenv('N_REPEATS')) if 'N_REPEATS' in os.environ else 1


def get_args():
    parser = argparse.ArgumentParser(description='Run and/or time daily challenges.')
    parser.add_argument('-t', '--timers', dest='timers', action='store_true', help='get results along with timings')
    parser.add_argument('-x', '--no-solutions', dest='solutions', action='store_false', help='get timings only')
    parser.add_argument('-d', '--days', nargs='+', help='specify days to execute')

    parser.set_defaults(timers=False, solutions=True)

    namespace = parser.parse_args()
    namespace.timers = True if namespace.timers == False and namespace.solutions == False else namespace.timers

    return namespace


def preload(name):
    f = importlib.import_module(f"{name}").result

    number = int(re.search(r"\d+", name)[0])
    response = requests.get(f'https://adventofcode.com/2020/day/{number}/input', cookies={'session': SESSION_COOKIE})
    input_ = response.content.decode('UTF-8').splitlines()

    return f, input_


def timers(function, input_):
    first_try = timeit.Timer(lambda: function(input_)).autorange()
    n_run = first_try[0]
    timers = [first_try[1]]
    timers.extend(timeit.Timer(lambda: function(input_)).repeat(N_REPEATS-1, n_run))

    return [1000 * timer / n_run for timer in timers]


def main():
    args = get_args()

    allowed_days = set([file[:-3] for file in os.listdir() if re.match(r"^day.*\.py$" ,file)])
    if args.days is None:
        days_to_compute = allowed_days
    else:
        possible_days = set(args.days + [f"day{x}" for x in args.days])
        days_to_compute = possible_days.intersection(allowed_days)

    print(f"""
        Days to compute:\t{', '.join(days_to_compute)}
        Compute solutions?\t{'✓' if args.solutions else '✘'}
        Compute timings?\t{'✓' if args.timers else '✘'}
    """)

    output_ = {}
    for day in days_to_compute:
        solver, input_ = preload(day)
        daily = {}

        if args.solutions:
            daily['solutions'] = solver(input_)

        if args.timers:
            daily['timers_ms'] = timers(solver, input_)

        output_[day] = daily

    print(output_)


if __name__ == '__main__':
    main()
