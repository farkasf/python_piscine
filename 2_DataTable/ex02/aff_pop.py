import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from load_csv import load


def convert_numbers(num_str: str | int | float) -> float:
    '''
    [CONVERT_NUMBERS] Converts str, int, or float number into a float.
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


def calculate_step(max_population: float) -> int:
    '''
    [CALCULATE_STEP] Determines the appropriate step size for y-axis
    tick marks based on the maximum population value.
    '''
    if max_population >= convert_numbers("1B"):
        return 200000000
    elif max_population >= convert_numbers("50M"):
        return 20000000
    elif max_population >= convert_numbers("10M"):
        return 3000000
    else:
        return 200000


def plot_graph(years: pd.Index, population: dict, countries: list) -> None:
    '''
    [PLOT_GRAPH] generates a line plot comparing population projections
    across multiple countries over time. Axis labels are configured and
    custom tick marks are used.
    '''
    plt.gcf().canvas.manager.set_window_title("ex02: compare my country")
    plt.title('Population Projections')

    for country in countries:
        plt.plot(years, population[country], label=country)

    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend()

    x_ticks = range(1800, 2050, 40)
    plt.xticks(x_ticks)

    max_population = (max(max(population[country]) for country in countries))
    step = calculate_step(max_population)

    y_ticks = np.arange(step, max_population, step)
    y_labels = []
    for tick in y_ticks:
        y_labels.append(format_y_ticks(tick))
    plt.yticks(ticks=y_ticks, labels=y_labels)

    plt.show()
    plt.close('all')


def main():
    '''
    [MAIN] Loads a dataset, processes numerical columns, filters the data
    for specified countries, and extracts population figures over a range
    of years and then plots this data. Includes error handling for issues
    related to data loading and processing.
    '''
    try:
        dataset = load("population_total.csv")
        if dataset is None:
            raise ValueError("Dataset is not loaded properly.")

        for column in dataset.columns[1:]:
            dataset[column] = dataset[column].apply(convert_numbers)

        countries = ["Czech Republic", "France"]
        countries_data = {}

        for country in countries:
            if country in dataset["country"].values:
                mask = dataset["country"] == country
                countries_data[country] = dataset[mask]
            else:
                raise ValueError(f"{country} not found in the dataset.")

        years = dataset.columns[1:].astype(int)
        population = {}
        for country in countries:
            population[country] = countries_data[country].values[0][1:]

        year_mask = []
        for year in years:
            if year >= 1800 and year <= 2050:
                year_mask.append(True)
            else:
                year_mask.append(False)

        years = years[year_mask]
        for country in countries:
            population[country] = population[country][year_mask]

        plot_graph(years, population, countries)

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
