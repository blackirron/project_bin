import argparse
from runtime import run_container

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", nargs="+")
    args = parser.parse_args()

    run_container(args.command)

if __name__ == "__main__":
    main()
