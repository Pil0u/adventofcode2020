import importlib
import os
import requests
import sys

from dotenv import load_dotenv

load_dotenv()
SESSION_COOKIE = os.getenv('SESSION_COOKIE')


def compute(n):
    f = importlib.import_module(f"day{n}")

    response = requests.get(f'https://adventofcode.com/2020/day/{n}/input', cookies={'session': SESSION_COOKIE})
    input_ = response.content.decode('UTF-8').splitlines()

    return f.result(input_)

def main():
    if len(sys.argv) >= 2:
        try:
            i = int(sys.argv[1])
        except:
            return "Argument is not a number"

        if f"day{i}.py" not in os.listdir():
            return "This day does not exist"
        else:
            return compute(i)
    else:
        return "Please pass a number corresponding to the day you want to execute"


if __name__ == '__main__':
    print(main())
