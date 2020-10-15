"""Train Station."""


class Passenger:
    """Passenger class."""

    def __init__(self, passenger_id: str, seat):
        """
        Passenger constructor.

        :param passenger_id:
        :param seat:
        """
        self.passenger_id = passenger_id
        self.seat = seat
        listing = seat.split("-")
        self.trainid = listing[0]
        self.carriage = listing[1]
        self.place = listing[2]

    @property
    def passenger_id(self) -> str:
        """
        Get id.

        :return:
        """
        return self._passenger_id

    @property
    def seat(self) -> str:
        """
        Get seat.

        :return:
        """
        return self._seat

    @seat.setter
    def seat(self, value):
        """
        Set seat.

        :param value:
        :return:
        """
        self._seat = value

    @passenger_id.setter
    def passenger_id(self, value):
        """
        Set id.

        :param value:
        :return:
        """
        self._passenger_id = value


class Train:
    """Train class."""

    def __init__(self, train_id: str, carriages: int, seats_in_carriage: int):
        """
        Train constructor.

        :param train_id:
        :param carriages:
        :param seats_in_carriage:
        """
        self.train_id = train_id
        self.carriages = carriages
        self.seats_in_carriage = seats_in_carriage
        self.passengers = []

    @property
    def passengers(self) -> list:
        """
        Return list of passengers.

        :return:
        """
        return self._passengers

    @property
    def carriages(self) -> int:
        """
        Return number of carriages.

        :return:
        """
        return self._carriages

    @property
    def train_id(self) -> str:
        """
        Return train id.

        :return:
        """
        return self._train_id

    @property
    def seats_in_carriage(self) -> int:
        """
        Return number of seats in carriage.

        :return:
        """
        return self._seats_in_carriage

    def get_seats_in_train(self) -> int:
        """
        Return number of seats in train.

        :return:
        """
        return self.carriages * self.seats_in_carriage

    def get_number_of_passengers(self) -> int:
        """
        Get number of passengers.

        :return:
        """
        self.get_passengers_in_carriages()
        return len(self._passengers)

    def get_passengers_in_carriages(self) -> dict:
        """
        Rerurn dictionary of passengers.

        :return:
        """
        dict = {}
        real_passengers = []
        for i in range(self.carriages):
            dict[f"{i + 1}"] = []
        for person in self.passengers:
            if self._train_id == person.trainid:
                if int(person.carriage) in range(1, self.carriages + 1) and int(person.place) in range(1, self.seats_in_carriage + 1):
                    dict[person.carriage].append(person)
                    real_passengers.append(person)
        self._passengers = real_passengers
        return dict

    @passengers.setter
    def passengers(self, value_list: list):
        """
        Set passengers.

        :param value_list:
        :return:
        """
        self._passengers = value_list

    @train_id.setter
    def train_id(self, value: str):
        """
        Set train id.

        :param value:
        :return:
        """
        self._train_id = value

    @carriages.setter
    def carriages(self, value: int):
        """
        Set carriages.

        :param value:
        :return:
        """
        self._carriages = value

    @seats_in_carriage.setter
    def seats_in_carriage(self, value: int):
        """
        Set seats.

        :param value:
        :return:
        """
        self._seats_in_carriage = value

    def add_passenger(self, passenger: Passenger) -> Passenger:
        """
        Add passenger to the list.

        :param passenger:
        :return:
        """
        self.passengers.append(passenger)


class TrainStation:
    """Train station class."""

    def __init__(self, trains: list, passengers: list):
        """
        Train station constructor.

        :param trains:
        :param passengers:
        """
        self.trains = trains
        self.passengers = passengers
        self.old_passengers = passengers[:]
        self.get_station_overview()

    def get_station_overview(self) -> list:
        """
        Get dict of all trains and their amount of passengers.

        :return:
        """
        train_info = []
        for train in self._trains:
            for passenger in self.old_passengers[:]:
                if passenger.trainid == train.train_id:
                    if int(passenger.carriage) in range(1, train.carriages + 1) and int(passenger.place) in range(1, train.seats_in_carriage + 1):
                        try:
                            for p in train.passengers:
                                if passenger.seat == p.seat and passenger.passenger_id != p.passenger_id:
                                    1 / 0
                        except ZeroDivisionError:
                            continue
                        else:
                            train.add_passenger(passenger)
                            self.old_passengers.remove(passenger)
            seats = f"{train.get_number_of_passengers()}/{train.get_seats_in_train()}"
            info = {"train_id": train.train_id, "carriages": train.carriages, "seats": seats}
            train_info.append(info)
        return train_info

    def get_number_of_passengers(self):
        """
        Get number of passengers on the station.

        :return:
        """
        return len(self.old_passengers)

    @property
    def passengers(self):
        """
        Get passengers.

        :return:
        """
        return self._passengers

    @passengers.setter
    def passengers(self, value_list: list):
        """
        Set passengers.

        :param value_list:
        :return:
        """
        self._passengers = value_list

    @property
    def trains(self):
        """
        Get trains.

        :return:
        """
        return self._trains

    @trains.setter
    def trains(self, value_list: list):
        """
        Set trains.

        :param value_list:
        :return:
        """
        self._trains = value_list


if __name__ == "__main__":
    # passengers
    p1 = Passenger("10", "AA-1-0")
    p2 = Passenger("11", "AA-1-1")
    p3 = Passenger("12", "AA-1-1")
    p4 = Passenger("13", "AA-1-2")
    p5 = Passenger("14", "AA-2-5")
    p6 = Passenger("15", "AB-2-4")
    p7 = Passenger("16", "AB-10-4")
    p8 = Passenger("17", "AB-0-0")
    passengers = [p1, p2, p3, p4, p5, p6, p7, p8]
    valid_passengers = [p2, p4, p5, p6]

    # trains
    t1 = Train("AA", 5, 5)
    t2 = Train("AB", 2, 4)
    trains = [t1, t2]

    # stations
    s1 = TrainStation(trains, passengers)
    stations = [s1]

    # TEST FUNCTION
    def basic_test(testname, output, expected):
        """Compare output with expected result."""
        if output == expected:
            print(f"{testname}: PASSED")
        else:
            print(f"{testname}: FAIL\n {output} - your output \n {expected} - expected")

    # TESTS
    basic_test("init_passengers", [p.passenger_id for p in passengers], ['10', '11', '12', '13', '14', '15', '16', '17'])
    basic_test("init_trains", [t.train_id for t in trains], ['AA', 'AB'])
    basic_test("init_station", s1.trains, trains)
    basic_test("get_seats_in_train", [t.get_seats_in_train() for t in trains], [25, 8])
    basic_test("get_number_of_passengers", [t.get_number_of_passengers() for t in trains], [3, 1])
    # basic_test("check_for_valid_passengers", [p.passenger_id for p in s1.passengers], ['11', '13', '14', '15'])
    get_passengers_in_carriages_correct = [{'1': [p2, p4], '2': [p5], '3': [], '4': [], '5': []}, {'1': [], '2': [p6]}]
    basic_test("get_passengers_in_carriages", [t.get_passengers_in_carriages() for t in trains], get_passengers_in_carriages_correct)
    get_station_overview_correct = [{'train_id': 'AA', 'carriages': 5, 'seats': '3/25'}, {'train_id': 'AB', 'carriages': 2, 'seats': '1/8'}]
    basic_test("get_station_overview", s1.get_station_overview(), get_station_overview_correct)
    basic_test("get_number_of_passengers", s1.get_number_of_passengers(), 4)
