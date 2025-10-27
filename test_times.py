import pytest
from times import time_range, compute_overlap_time

def test_time_range_single_interval():
    result = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    expected = [("2010-01-12 10:00:00", "2010-01-12 12:00:00")]
    assert result == expected

def test_time_range_two_intervals():
    result = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", number_of_intervals=2)
    expected = [
        ("2010-01-12 10:00:00", "2010-01-12 11:00:00"),
        ("2010-01-12 11:00:00", "2010-01-12 12:00:00")
    ]
    assert result == expected

def test_compute_overlap_time():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", number_of_intervals=2, gap_between_intervals_s=60)
    result = compute_overlap_time(large, short)
    expected = [
        ("2010-01-12 10:30:00", "2010-01-12 10:37:30"),
        ("2010-01-12 10:38:30", "2010-01-12 10:45:00")
    ]
    assert result == expected
