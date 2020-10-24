"""Formula One."""
import re
import csv
import copy


class Driver:
    """Driver class."""

    def __init__(self, name: str, team: str):
        """
        Driver constructor.

        Here you should save driver's results as dictionary,
        where key is race number and value is points from that race.
        You must also save driver's points into a variable "points".

        :param name: Driver name
        :param team: Driver team
        """
        self.name = name
        self.team = team
        self.results = {}
        self.points = 0

    def get_results(self) -> dict:
        """
        Get all driver's results.

        :return: Results as dictionary
        """
        return self.results

    def get_points(self) -> int:
        """
        Return calculated driver points.

        :return: Calculated points
        """
        return self.points

    def set_points(self, value):
        """Set points for driver."""
        self.points += int(value)

    def add_result(self, race_number: int, points: int):
        """
        Add new result to dictionary of results.

        Dictionary is located in the constructor.

        :param race_number: Race number
        :param points: Number of points from the race
        """
        self.results[race_number] = points


class Race:
    """Race class."""

    def __init__(self, file):
        """
        Race constructor.

        Here you should keep data collected from file.
        You must read file rows to list.

        :param file: File with race data
        """
        self.file = file
        self.info = self.read_file_to_list()[1:]
        self.number = self.read_file_to_list()[0]

    def read_file_to_list(self):
        """
        Read file data to list in constructor.

        First line shows number of races in data file.
        Rest of the data follows same rules. Each line consists of 'Driver Team Time Race'.
        There are 2 or more spaces between each 'category'.
        E.g. "Mika Häkkinen  McLaren-Mercedes      42069   3"

        If file does NOT exist, throw FileNotFoundError with message "No file found!".
        """
        lines = []
        try:
            with open(self.file, encoding='utf-8') as file:
                for line in file:
                    if len(line) > 5:
                        lines.append(Race.extract_info(line))
                    else:
                        lines.append(line)
        except FileNotFoundError:
            return "No file found!"
        return lines

    @staticmethod
    def extract_info(line: str) -> dict:
        """
        Helper method for read_file_to_list.

        Here you should convert one data line to dictionary.
        Dictionary must contain following key-value pairs:
            'Name': driver's name as string
            'Team': driver's team as string
            'Time': driver's time as integer (time is always in milliseconds)
            'Diff': empty string
            'Race': race number as integer

        :param line: Data string
        :return: Converted dictionary
        """
        pattern = r"\s\s+"
        a = re.split(pattern, line)
        return {
            'Name': a[0],
            'Team': a[1],
            'Time': a[2],
            'Diff': "",
            'Race': a[3],
        }

    def filter_data_by_race(self, race_number: int) -> list:
        """
        Filter data by race number.

        :param race_number: Race number
        :return: Filtered race data
        """
        data = self.info
        filtered = []
        for racer in data:
            if int(racer["Race"]) == race_number:
                filtered.append(racer)
        return filtered

    @staticmethod
    def format_time(time: str) -> str:
        """
        Format time from milliseconds to M:SS.SSS

        format_time('12') -> 0:00.012
        format_time('1234') -> 0:01.234
        format_time('123456') -> 2:03.456

        :param time: Time in milliseconds
        :return: Time as M:SS.SSS string
        """
        milliseconds = time
        milliseconds = int(milliseconds)
        minutes = milliseconds // 60000
        milliseconds = milliseconds % 60000
        milliseconds = str(milliseconds)
        while len(milliseconds) < 5:
            milliseconds = "0" + milliseconds
        time = f'{minutes}:{milliseconds[:2]}.{milliseconds[2:]}'
        return time

    @staticmethod
    def calculate_time_difference(first_time: int, second_time: int) -> str:
        """
        Calculate difference between two times.

        First time is always smaller than second time. Both times are in milliseconds.
        You have to return difference in format +M:SS.SSS

        calculate_time_difference(4201, 57411) -> +0:53.210

        :param first_time: First time in milliseconds
        :param second_time: Second time in milliseconds
        :return: Time difference as +M:SS.SSS string
        """
        diff = second_time - first_time
        return "+" + Race.format_time(str(diff))

    @staticmethod
    def sort_data_by_time(results: list) -> list:
        """
        Sort results data list of dictionaries by 'Time'.

        :param results: List of dictionaries
        :return: Sorted list of dictionaries
        """
        data = copy.deepcopy(results)
        data.sort(key=lambda x: x["Time"])
        return data

    def get_results_by_race(self, race_number: int) -> list:
        """
        Final results by race number.

        This method combines the rest of the methods.
        You have to filter data by race number and sort them by time.
        You must also fill 'Diff' as time difference with first position.
        You must add 'Place' and 'Points' key-value pairs for each dictionary.

        :param race_number: Race number for filtering
        :return: Final dictionary with complete data
        """
        data = self.filter_data_by_race(race_number)
        data = Race.sort_data_by_time(data)
        place = 1
        points = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
        for race in data:
            if place <= 10:
                race["Points"] = str(points[place - 1])
            else:
                race["Points"] = "0"
            race["Place"] = str(place)
            if place > 1:
                second_time = int(race["Time"])
                race["Diff"] = Race.calculate_time_difference(first_time, second_time)
            first_time = int(race["Time"])
            place += 1
            race["Time"] = Race.format_time(race["Time"])
        return data


class FormulaOne:
    """FormulaOne class."""

    def __init__(self, file):
        """
        FormulaOne constructor.

        It is reasonable to create Race instance here to collect all data from file.

        :param file: File with race data
        """
        self.file = file
        self.race = Race(self.file)
        self.number = int(self.race.number)

    def write_race_results_to_file(self, race_number: int):
        """
        Write one race results to a file.

        File name is 'results_for_race_{race_number}.txt'.
        Exact specifications are described in the text.

        :param race_number: Race to write to file
        """
        with open(f'results_for_race_{race_number}.txt', 'w', newline='') as file:
            file.write('PLACE     NAME                     TEAM                     TIME           DIFF           POINTS\n')
            file.write('-' * 96 + '\n')
            for line in self.race.get_results_by_race(race_number):
                while len(line['Place']) < 10:
                    line['Place'] += ' '
                while len(line['Name']) < 25:
                    line['Name'] += ' '
                while len(line['Team']) < 25:
                    line['Team'] += ' '
                while len(line['Time']) < 15:
                    line['Time'] += ' '
                while len(line['Diff']) < 15:
                    line['Diff'] += ' '
                while len(line['Points']) < 6:
                    line['Points'] += ' '
                file.write(f"{line['Place']}{line['Name']}{line['Team']}{line['Time']}{line['Diff']}{line['Points']}\n")

    def write_race_results_to_csv(self, race_number: int):
        """
        Write one race results to a csv file.

        File name is 'race_{race_number}_results.csv'.
        Exact specifications are described in the text.

        :param race_number: Race to write to file
        """
        data = self.race.get_results_by_race(race_number)
        with open(f'race_{race_number}_results.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(['Place', 'Name', 'Team', 'Time', 'Diff', 'Points', 'Race'])
            for line in data:
                writer.writerow([line['Place'], line['Name'], line['Team'], line['Time'], line['Diff'], line['Points'], line['Race']])

    def write_championship_to_file(self):
        """
        Write championship results to file.

        It is reasonable to create Driver class instance for each unique driver name and collect their points
        using methods from Driver class.
        Exact specifications are described in the text.
        """
        list_of_racers = []
        for i in range(self.number):
            data = self.race.get_results_by_race(i+1)
            for racer in data:
                dude = Driver(racer['Name'], racer['Team'])
                if dude not in list_of_racers:
                    list_of_racers.append(dude)
                dude.add_result(i, racer['Points'])
                dude.set_points(racer['Points'])
        list_of_racers.sort(key=lambda x: x.points, reverse=True)
        with open(f'championship_results.txt', 'w', newline='') as file:
            file.write('PLACE     NAME                     TEAM                     POINTS\n')
            file.write('-' * 66 + '\n')
            counter = 1
            for dude in list_of_racers:
                place = str(counter)
                dude.points = str(dude.points)
                while len(place) < 10:
                    place += ' '
                while len(dude.name) < 25:
                    dude.name += ' '
                while len(dude.team) < 25:
                    dude.team += ' '
                while len(dude.points) < 6:
                    dude.points += ' '
                file.write(f"{place}{dude.name}{dude.team}{dude.points}\n")
                counter += 1


if __name__ == '__main__':
    f1 = FormulaOne("ex08_example_data.txt")
    r = Race("ex08_example_data.txt")
    f1.write_race_results_to_file(1)
    f1.write_race_results_to_csv(2)
    print(f1.write_championship_to_file())
