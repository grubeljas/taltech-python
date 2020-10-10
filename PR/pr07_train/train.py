"""Train."""


class Train:
    """Train class."""

    def __init__(self, passengers: list, carriages: int, seats_in_carriage: int):
        """
        Train constructor.

        :param passengers:
        :param carriages:
        :param seats_in_carriage:
        """
        self.passengers = passengers
        self.carriages = carriages
        self.seats_in_carriage = seats_in_carriage

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

    def get_number_of_passengers(self, passengers) -> int:
        """
        Count number of passengers.

        :param passengers:
        :return:
        """
        a = 0
        for i in range(len(passengers)):
            a += 1
        return a

    def get_passengers_in_carriages(self) -> dict:
        """
        Check passengers be carriage.

        :return:
        """
        dict = {}
        if self.carriages == 0:
            return dict
        for i in range(self._carriages):
            dict[f"{i + 1}"] = []
        for person in self.passengers:
            nums = person.seat.split("-")
            if int(nums[0]) <= self.carriages and int(nums[1]) <= self.seats_in_carriage:
                info = {'id': person.id, 'seat': nums[1]}
                dict[nums[0]].append(info)
        return dict

    @passengers.setter
    def passengers(self, value_list: list):
        """
        Set passengers.

        :param value_list:
        :return:
        """
        self._passengers = value_list

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


class Passenger:
    """Passenger class."""

    def __init__(self, passenger_id: str, seat: str):
        """
        Passenger constructor.

        :param passenger_id:
        :param seat:
        """
        self.id = passenger_id
        self.seat = seat

    def __dict__(self):
        """
        Return dictionary with passenger data.

        :return:
        """
        return {'id': self.id, 'seat': self.seat}


if __name__ == '__main__':
    p_1 = Passenger('123', '1-9')
    p_2 = Passenger('321', '2-11')
    p_3 = Passenger('456', '4-5')
    t = Train([p_1, p_2, p_3], 3, 10)
    print(t)
    print(p_1.__dict__())
    print(t.get_passengers_in_carriages())
