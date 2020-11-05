# import the functions made in times
from times import compute_overlap_time
from times import time_range
from pytest import raises

# function to test
def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = (compute_overlap_time(large, short))
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    
    assert result == expected

def test_no_overlap():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 13:30:00", "2010-01-12 13:45:00", 2, 60)
    expected = []
    
    assert (compute_overlap_time(large, short)) == expected

def test_both_intervals():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2,60)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2,60)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    
    assert (compute_overlap_time(large, short)) == expected

def test_times_touching():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00",2,0)
    short = time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00", 2, 0)
    expected = []
    
    assert (compute_overlap_time(large, short)) == expected

def test_starttime_before_endtime():
    with raises(ValueError):
        time_range("2010-01-12 11:00:00","2010-01-12 10:00:00")

def test_starttime_equal_endtime():
    with raises(ValueError):
        time_range("2010-01-12 11:00:00","2010-01-12 11:00:00")