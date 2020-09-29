"""
EX05 - OEE
"""
import csv


def read_production_data(filename: str) -> dict:
    """
    Open the file in the provided path, read in values and return them as a dictionary,
    where the key is the machine name and value is a list of integers for the production data for each shift.

    {
    'Machine Name': [Run Time (minutes), Ideal Run Rate (pcs/min), Total Count (pcs), Good Count (pcs)]
    }

    :param filename: string file path for the CSV file to be read
    :return: dictionary with the production data per machine
    """
    son = {}
    try:
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                son[row[0]] = [int(row[1]), int(row[2]), int(row[3]), int(row[4])]
            return son
    except FileNotFoundError:
        return son


def calculate_quality(production_data: dict) -> dict:
    """
    Go through the input dictionary and for each machine, calculate the Quality percentage (as a float, e.g. 98.1).
    Save each value in a new dictionary, where the key is the machine name and value is the calculated Quality.
    Return the newly created dictionary.

    :param production_data: dictionary with production data
    :return: dictionary with OEE Quality value per machine
    """
    quality_dict = {}
    for machine, values in production_data.items():
        good_count = values[3]
        total_count = values[2]
        if total_count == 0:
            quality_dict[machine] = 0.0
            continue
        quality = (good_count/total_count) * 100
        quality_dict[machine] = round(quality, 1)
    return quality_dict


def calculate_availability(production_data: dict) -> dict:
    """
    Go through the input dictionary and for each machine, calculate the Availability percentage (as a float, e.g. 98.1).
    Save each value in a new dictionary, where the key is the machine name and value is the calculated Availability.
    Return the newly created dictionary.

    :param production_data: dictionary with production data
    :return: dictionary with OEE Availability value per machine
    """
    availability_dict = {}
    for machine, values in production_data.items():
        run_time = values[0]
        planned_time = 420
        availability = run_time / planned_time * 100
        availability_dict[machine] = round(availability, 1)
    return availability_dict


def calculate_performance(production_data: dict) -> dict:
    """
    Go through the input dictionary and for each machine, calculate the Performance percentage (as a float, e.g. 98.1).
    Save each value in a new dictionary, where the key is the machine name and value is the calculated Performance.
    Return the newly created dictionary.

    :param production_data: dictionary with production data
    :return: dictionary with OEE Performance value per machine
    """
    performance_dict = {}
    for machine, values in production_data.items():
        run_time = values[0]
        total_count = values[2]
        ideal_run_time = values[1]
        if run_time == 0:
            performance_dict[machine] = 0.0
            continue
        performance = (total_count / run_time) / ideal_run_time * 100
        performance_dict[machine] = round(performance, 1)
    return performance_dict


def calculate_oee(production_data: dict) -> dict:
    """
    Using the previously defined functions, calculate the final OEE percentage for each machine.
    Save each value in a new dictionary, where the key is the machine name and value is the calculated Performance.
    Return the newly created dictionary.

    :return: dictionary with OEE percentage value per machine
    """
    oee_dict = {}
    performance_dict = calculate_performance(production_data)
    availability_dict = calculate_availability(production_data)
    quality_dict = calculate_quality(production_data)
    for machine in production_data:
        performance = performance_dict[machine]
        availability = availability_dict[machine]
        quality = quality_dict[machine]
        oee = (performance * availability * quality) / 10000
        oee_dict[machine] = round(oee, 1)
    return oee_dict


def write_results_to_file(production_data: dict, filename: str):
    """
    Write the calculation results to a CSV formatted file.

    :param filename: string file path for the CSV file to be written to
    :param production_data: dictionary with production data
    """
    quality = calculate_quality(production_data)
    performance = calculate_performance(production_data)
    availability = calculate_availability(production_data)
    oee = calculate_oee(production_data)
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(["Liin", "Saadavus", "Tootlus", "Kvaliteet", "OEE"])
        for machine, numbers in production_data.items():
            writer.writerow([machine, availability[machine], performance[machine], quality[machine], oee[machine]])
