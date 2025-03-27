from os.path import exists
from os import environ
import argparse
from aocd import get_data, submit
from time import perf_counter
import importlib
from tqdm import tqdm
import pyperclip
import webbrowser


argParser = argparse.ArgumentParser()
argParser.add_argument("day", nargs="?", type=int, help="Select the puzzle day")
argParser.add_argument("-t", "--test", action="store_true", help="Apply to test case")
argParser.add_argument("-s", "--submit", action="store_true", help="Submit result")
argParser.add_argument("-r", "--result", action="store_true", help="Check result")
argParser.add_argument("-z", "--reset", action="store_true", help="Reset day files")
argParser.add_argument("-i", "--input_paste", action="store_true", help="Paste input")
argParser.add_argument(
    "-e", "--example_paste", action="store_true", help="Paste example"
)
argParser.add_argument(
    "-p", "--print", default=False, action="store_true", help="Print result"
)
argParser.add_argument(
    "-o",
    "--open",
    default=False,
    action="store_true",
    help="Open respective puzzle in browser",
)
args = argParser.parse_args()

# for i in range(1,26):
#      with open(f'2015\solutions\day{i:02d}.py','w') as f:
#           f.write('')

year_ = int(environ["AOC_YEAR"])
days = [importlib.import_module(f"{year_}.solutions.day{i:02d}") for i in range(1, 26)]


def runDay(day_, path=None):
    path = path or f"{year_}\\data\\inputs\\day{day_:02d}.txt"

    if not exists(path):
        with open(path, "w") as f:
            f.write(get_data(day=day_, year=year_))

    with open(path) as f:
        inp = f.read()
        start_time = perf_counter()
        p1, p2 = days[day_ - 1].main(inp)
        if args.test:
            if not args.print:
                p1 = p1 if p1 is None else str(p1) == environ["aoctest1"]
                p2 = p2 if p2 is None else str(p2) == environ["aoctest2"]
        elapsed = perf_counter() - start_time
        Print_results(p1, p2, elapsed)
    return p1, p2


def Print_results(p1, p2, elapsed):
    if p1 is not None:
        print(" Part1:\n", p1)
        print()
    if p2 is not None:
        print(" Part2:\n", p2)

    if elapsed >= 1:
        print("\n", "Exec_time = ", round(elapsed, 3), "s")
    else:
        print("\n", "Exec_time = ", round(elapsed * 1000, 5), "ms")


def RunTests(day):
    path = f"{year_}\\data\\examples\\day{day:02d}.txt"
    runDay(day, path)


if args.open:
    webbrowser.open(f"https://adventofcode.com/{year_}/day/{args.day}")


if args.reset:

    def reset(x):
        with open(f"{year_}\\solutions\\day{x:02d}.py", "w") as f:
            f.write("""


def main(inp):
        
            


    return None,None
                    """)
        with open(f"{year_}\\data\\inputs\\day{x:02d}.txt", "w") as f:
            f.write("")

    if args.day:
        reset(args.day)
    else:
        for i in tqdm(range(1, 26)):
            reset(i)


if args.test:
    RunTests(args.day)


if args.result or args.submit:
    p1, p2 = runDay(args.day)
if args.submit:
    if p1:
        submit(p1, part="a", day=args.day, year=year_)
    if p2:
        submit(p2, part="b", day=args.day, year=year_)

if args.input_paste:
    with open(f"{year_}\\data\\inputs\\day{args.day:02d}.txt", "w") as f:
        text = pyperclip.paste().replace("\r\n", "\n")
        f.write(text)
if args.example_paste:
    with open(f"{year_}\\data\\examples\\day{args.day:02d}.txt", "w") as f:
        text = pyperclip.paste().replace("\r\n", "\n")
        f.write(text)
