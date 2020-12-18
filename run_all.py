import importlib
import os
import re
import requests
import timeit

from dotenv import load_dotenv

load_dotenv()
SESSION_COOKIE = os.getenv('SESSION_COOKIE')
N_REPEATS = int(os.getenv('N_REPEATS')) if 'N_REPEATS' in os.environ else 1


if __name__ == '__main__':

    available_days = sorted([int(file[3:-3]) for file in os.listdir() if re.match(r"^day\d*.py$", file)])

    results = []
    timings = []

    for i in available_days:
        f = importlib.import_module(f"day{i}")

        response = requests.get(f'https://adventofcode.com/2020/day/{i}/input', cookies={'session': SESSION_COOKIE})
        input_ = response.content.decode('UTF-8').splitlines()

        # Calculate actual result
        results.append((f.result(input_)))

        # Measure time taken
        first_try = timeit.Timer("f.result(input_)", setup="from __main__ import f, input_").autorange()
        n_run = first_try[0]
        timers = [first_try[1]]
        timers.extend(timeit.Timer("f.result(input_)", setup="from __main__ import f, input_").repeat(N_REPEATS-1, n_run))

        timings.append(1000 * min(timers) / n_run)

    print(results)
    print(timings)
