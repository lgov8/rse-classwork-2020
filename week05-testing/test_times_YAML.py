# testing times.py with a paremtrised test, reading in the data from a YAML file

from times import time_range, compute_overlap_time
import pytest
import yaml

with open('fixtures.yaml', 'r') as yaml_file:
    data = yaml.safe_load(yaml_file)
    print(data)

@pytest.mark.parametrize("test_name", data)

def test_times(test_name):
    tests = list(data.values())[0] # list of the names of the tests from fixtures
    range1 = time_range(*tests['range1']) # pull first time range from fixtures
    range2 = time_range(*tests['range2']) # pull second time range 
    expected = [(begin,end) for begin, end in tests['expected']] # pull expected overlaps into a list
    assert compute_overlap_time(range1,range2) == expected

def test_starttime_before_endtime():
    with pytest.raises(ValueError):
        time_range("2010-01-12 11:00:00","2010-01-12 10:00:00")   