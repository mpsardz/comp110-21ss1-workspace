"""Exploring command line arguments."""

# gives us access to the arguments our program begins with
import sys

# argv is just the list of arguments our program is begun with
# by feault, when you beging a program from the command line
# the first argument is the file you are trying to run

# args: list[str] = sys.argv
# print(len(args))
# print(args)

# spaces bewteen words determine the seeration of arguments
# can put quotes to have a mutltiple word argument

# specify the program we want to solve
# run our program as a module with two command line arguments
# 1. name of the file we'd like to search
# 2. searc term we are looking for
# print out all the lines containing the search terms and
# give the total number of matches

def read_args() -> dict[str, str]:
    """Check for valid CLI arguments and return them in a dictionary."""
    if len(sys.argv) != 3:
        print("Usage: python -m lessons.ls26_cli_args [file] [keyword]")
        exit ()
    return{
        "file_path": sys.argv[1],
        "keyword": sys.argv[2]
    }

def search_file(file_path: str, keyword: str) -> list[str]:
    """Open a file, read each_line, return matching lines."""
    matches: list[str] = []
    file_handle = open(file_path, "r", encoding="utf8")
    for line in file_handle:
        if keyword in line:
            matches.append(line)
    file_handle.close()
    return matches

def main() -> None:
    """Entrypoint."""
    args: dict[str,str] = read_args()
    print(args)

if __name__ == "__main__":
    main()