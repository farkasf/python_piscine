import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from load_csv import load


def plot_data(years: pd.Index, life_exp: np.ndarray, country: str) -> None:
    '''
    [PLOT_DATA] creates a line plot displaying life expectancy projections
    for a specified country over a range of years. Axis labels are configured
    and custom tick marks are used.
    '''
    plt.gcf().canvas.manager.set_window_title("ex01: draw my country")
    plt.title(f"{country} Life expectancy Projections")

    plt.plot(years, life_exp, label=country)

    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")

    x_ticks = list(range(years[0], years[-1], 40))
    plt.xticks(x_ticks)

    y_ticks = range(30, 100, 10)
    plt.yticks(y_ticks)
    plt.ylim(27, 95)

    plt.show()
    plt.close('all')


def main():
    '''
    [MAIN] loads a dataset, filters it for a specified country, extracts year
    and life expectancy data, and then plots this data. Includes error handling
    for issues related to data loading and processing.
    '''
    try:
        dataset = load("life_expectancy_years.csv")
        if dataset is None:
            raise ValueError("dataset is not loaded properly")

        country_name = "Czech Republic"
        if country_name in dataset["country"].values:
            mask = dataset["country"] == country_name
            country_data = dataset[mask]
        else:
            raise ValueError(f"'{country_name}' not found in the dataset")

        years = country_data.columns[1:].astype(int)
        life_expectancy = country_data.values[0][1:]

        plot_data(years, life_expectancy, country_name)

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
