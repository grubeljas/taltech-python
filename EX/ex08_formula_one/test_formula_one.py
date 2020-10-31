import pytest

from formula_one import Driver, Race, FormulaOne
f1 = FormulaOne("ex08_example_data.txt")
r = Race("ex08_example_data.txt")
print(r.info)
d = Driver('Dan', 'GhostDriver')
d.add_result(1, 5)
d.add_result(2, 0)
f1.write_race_results_to_file(1)
f1.write_race_results_to_csv(1)
f1.write_championship_to_file()

def test():

    assert r.file == "ex08_example_data.txt"
    assert Race.format_time(111) == '0:00.111'
    assert int(r.number) == 3
    assert r.info[0] == {'Diff': '',
 'Name': 'Mika Hakkinen',
 'Race': 1,
 'Team': 'Mclaren-Mercedes',
 'Time': 79694}
    assert Race.calculate_time_difference(10000, 50000) == '+0:40.000'
    assert r.read_file_to_list()[0] == '3\n'
    assert r.number == '3\n'
    assert r.calculate_time_difference(9, 69999) == '+1:09.990'
    assert r.get_results_by_race(1)[0] == {'Diff': '', 'Name': 'Jenson Button', 'Place': 1, 'Points': 25, 'Race': 1, 'Team': 'Williams-BMW', 'Time': '1:17.606'}
    assert r.filter_data_by_race(1)[0] == {'Diff': '',
 'Name': 'Mika Hakkinen',
 'Race': 1,
 'Team': 'Mclaren-Mercedes',
 'Time': 79694} != 1
    assert r.sort_data_by_time([{"Time": 10}, {"Time": 1}]) == [{"Time": 1}, {"Time": 10}]
    assert d.get_points() == 5
    assert d.get_results() == {1: 5, 2: 0}

