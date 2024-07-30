import csv
from datetime import timedelta
import os
import pandas as pd

from source.constants import PA_ANALYSIS_FOLDER


def format_dates(start_date, end_date):
    start_datetime = pd.to_datetime(start_date, format="%d/%m/%Y %H:%M:%S")
    end_datetime = pd.to_datetime(end_date, format="%d/%m/%Y %H:%M:%S")
    return start_datetime, end_datetime


def make_positive(value):
    if value < 0:
        return value * -1
    return value


def make_negative(value):
    if value > 0:
        return value * -1
    return value


def make_round(value):
    return round(value, 2)


def format_duration(seconds):
    return str(timedelta(seconds=seconds))

    # days = seconds / (3600 * 24)
    # if days >= 1:
    #     return f"{make_round(days)} days"
    # hours = seconds / 3600
    # if hours >= 1:
    #     return f"{make_round(hours)} hours"
    # minutes = seconds / 60
    # return f"{make_round(minutes)} minutes"


def write_dict_to_csv(
    data,
    main_header,
    sub_header=None,
    output_dir=PA_ANALYSIS_FOLDER,
    csv_filename="final_result.csv",
):
    csv_file_path = os.path.join(output_dir, csv_filename)
    os.makedirs(output_dir, exist_ok=True)

    # Write to CSV
    with open(csv_file_path, mode="w", newline="") as file:
        writer = csv.writer(file)

        # Write main and sub headers
        writer.writerow(main_header)
        if sub_header:
            writer.writerow(sub_header)

        # Write the data rows
        for row in data:
            writer.writerow(row.values())


def write_dataframe_to_csv(dataframe, folder_name, file_name):
    path = os.path.join(folder_name, file_name)
    os.makedirs(folder_name, exist_ok=True)
    dataframe.to_csv(path, index=True)


def make_positive_series(series: pd.Series) -> pd.Series:
    """
    Ensure all values in the series are positive.
    If a value is negative, it is converted to positive.
    """
    return series.abs()


def make_round_series(series: pd.Series, decimals: int = 2) -> pd.Series:
    """
    Round all values in the series to the specified number of decimal places.
    """
    return series.round(decimals)
