import sys
import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def convert_numbers(num_str: str | int | float) -> float:
    '''
    [CONVERT_NUMBERS] converts str, int, or float number into a float.
    Handles thousands (k), millions (M), and billions (B).
    '''
    if isinstance(num_str, (int, float)):
        num = float(num_str)
    elif num_str.endswith("k"):
        num = float(num_str[:-1]) * 1000
    elif num_str.endswith('M'):
        num = float(num_str[:-1]) * 1000000
    elif num_str.endswith('B'):
        num = float(num_str[:-1]) * 1000000000
    else:
        num = float(num_str)
    return num


def format_y_ticks(num: float) -> str:
    '''
    [FORMAT_Y_TICKS] Shortens a float into a string with an appropriate
    suffix if necessary. Whole numbers are returned in integer format.
    '''
    if num >= 1000000000:
        tick = float(num / 1000000000)
        suffix = 'B'
    elif num >= 1000000:
        tick = float(num / 1000000)
        suffix = 'M'
    elif num >= 1000:
        tick = float(num / 1000)
        suffix = 'k'
    else:
        tick = float(num)
        suffix = ''
    if tick.is_integer():
        return str(int(tick)) + suffix
    else:
        return str(tick) + suffix


def plot_graph(year: int, gdp_data: pd.Series, le_data: pd.Series) -> None:
    '''
    [PLOT_GRAPH] creates a scatter plot of GDP versus life expectancy for a
    specified year. X-axis is adjusted to a logarithmic scale. Axis labels
    are configured and custom tick marks are used.

    '''
    plt.gcf().canvas.manager.set_window_title("ex03: draw my year")
    plt.title(f"{year}")

    plt.scatter(gdp_data, le_data)
    plt.xscale("log")

    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")

    if year <= 1900:
        plt.ylim(18, 55.2)
        plt.xlim(300, 11000)
        x_ticks = [300, 1000, 10000]
    else:
        x_ticks = [1000, 50000, 200000]
    y_labels = []
    for value in x_ticks:
        y_labels.append(format_y_ticks(value))

    plt.xticks(x_ticks, y_labels)

    plt.show()
    plt.close("all")


def main():
    '''
    [MAIN] Loads GDP and life expectancy datasets, processes numerical data
    for a specified year, and then plots this information. Includes error
    handling for issues related to data loading and processing.
    '''
    try:
        gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        le = load("life_expectancy_years.csv")

        if gdp is None or le is None:
            raise ValueError("Datasets are not loaded properly.")

        year = str(1900)

        if year in gdp.columns:
            gdp[year] = gdp[year].apply(convert_numbers)
        else:
            raise KeyError(f"{year} not found in the GDP dataset.")

        if year in le.columns:
            le[year] = le[year].apply(convert_numbers)
        else:
            raise KeyError(f"{year} not found in the LE dataset.")

        gdp_data = gdp[year]
        le_data = le[year]

        plot_graph(int(year), gdp_data, le_data)

    except ValueError as e:
        print(f"ValueError: {e}")
        sys.exit(1)
    except KeyError as e:
        print(f"KeyError: {e}")
        sys.exit(1)
    except IndexError as e:
        print(f"IndexError: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
