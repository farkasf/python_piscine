import os
from time import sleep


def ft_tqdm(lst: range) -> None:
    '''
    [FT_TQDM] Displays a progress bar in the terminal while iterating over
    a range or iterable object. Automatically adjusts to terminal size and
    handles errors (division by zero, incorrect range, OS error).
    '''
    try:
        term_width = os.get_terminal_size().columns
        bar_width = int(term_width * 0.8) + 1
        total = len(lst)
        if not total:
            raise TypeError
    except TypeError:
        print("TypeError: incorrect range")
        return
    except OSError:
        bar_width = 120

    iter_num = 1
    for item in lst:
        progress = iter_num / total
        filled = int(bar_width * progress)
        bar = "█" * filled
        padding = " " * (bar_width - len(bar))
        print(f'\r{progress:4.0%}|{bar}{padding}| {iter_num}/{total}', end='')
        iter_num += 1
        yield item


def main():
    '''
    [MAIN] Runs a loop using ft_tqdm() to display progress while iterating
    over a range of 333, simulating a delay with sleep(0.005).
    '''
    for elem in ft_tqdm(range(333)):
        sleep(0.005)
    print()


if __name__ == "__main__":
    main()
