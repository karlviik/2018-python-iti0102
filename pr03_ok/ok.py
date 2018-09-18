"""Make everything OK."""
import time


def wants_solving():
    """Prompt the user to make everything OK."""
    while True:

        name = input("Would you like to make everything OK?")

        if name == "Y":
            print("Let's go.")
            return True

        elif name == "N":
            print("Alrighty then.")
            return False

        else:
            print("Sorry, try again.")


def progress_bar(process_name, second):
    """Show the user where the process is."""
    cycle_time = second / 20

    if len(process_name) > 25:
        process_name = process_name[:20] + "..."

    for i in range(21):
        print(f"\r[{'|' * i:.<20}] | Process: {process_name!r} {0.05 * i:4.0%}", end="")
        time.sleep(cycle_time)

    print()


def print_ok():
    """Print that everything is OK."""
    print("Everything is OK now.")


def main():
    """Main function."""
    if wants_solving():
        progress_bar("Making eveything OK.", 5)
        print_ok()


if __name__ == "__main__":
    main()
