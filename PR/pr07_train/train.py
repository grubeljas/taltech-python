"""Train."""


class Train:
    def __init__(self, passengers: list, carriages: int, seats_in_carriage: int):
        self.passengers = passengers
        self.carriages = carriages
        self.seats_in_carriage = seats_in_carriage

    @property
    def passengers(self) -> list:
        return self._passengers

    @property
    def carriages(self) -> int:
        return self._carriages

    @property
    def seats_in_carriage(self) -> int:
        return self._seats_in_carriage

    def get_seats_in_train(self) -> int:
        return self.carriages * self.seats_in_carriage

    def get_number_of_passengers(self, passengers) -> int:
        a = 0
        for i in range(len(passengers)):
            a += 1
        return a

    def get_passengers_in_carriages(self) -> dict:
        dict = {}
        if self.carriages == 0:
            return dict
        for i in range(self._carriages):
            dict[f"{i + 1}"] = []
        for person in self.passengers:
            nums = person.seat.split("-")
            if int(nums[0]) <= self.carriages and int(nums[1]) <= self.seats_in_carriage:
                info = {'id': person.passenger_id, 'seat': nums[1]}
                dict[nums[0]].append(info)
        return dict

    @passengers.setter
    def passengers(self, value_list: list):
        self._passengers = value_list

    @carriages.setter
    def carriages(self, value: int):
        self._carriages = value

    @seats_in_carriage.setter
    def seats_in_carriage(self, value: int):
        self._seats_in_carriage = value


class Passenger:
    def __init__(self, passenger_id: str, seat: str):
        self.passenger_id = passenger_id
        self.seat = seat

    def __dict__(self):
        return {'id': self.passenger_id, 'seat': self.seat}


if __name__ == '__main__':
    p_1 = Passenger('123', '1-9')
    p_2 = Passenger('321', '2-11')
    p_3 = Passenger('456', '4-5')
    t = Train([p_1, p_2, p_3], 3, 10)
    print(t)
    print(p_1.__dict__())
    print(t.get_passengers_in_carriages())
