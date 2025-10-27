import pytest
from times import time_range, compute_overlap_time


def test_compute_overlap_time():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", number_of_intervals=2, gap_between_intervals_s=60)
    result = compute_overlap_time(large, short)
    expected = [
        ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
        ("2010-01-12 10:38:00", "2010-01-12 10:45:00")
    ]
    assert result == expected

def test_no_overlap(): 
    range1 = [("2010-01-12 10:00:00", "2010-01-12 11:00:00")]
    range2 = [("2010-01-12 11:30:00", "2010-01-12 12:00:00")]
    result = compute_overlap_time(range1, range2)
    expected = [("2010-01-12 11:30:00", "2010-01-12 11:00:00")]
    assert result == expected

def test_multiple_overlaps():
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 13:00:00", number_of_intervals=3)
    range2 = time_range("2010-01-12 11:00:00", "2010-01-12 14:00:00", number_of_intervals=3)
    result = compute_overlap_time(range1, range2)
    expected = [
        ("2010-01-12 11:00:00", "2010-01-12 12:00:00"),
        ("2010-01-12 12:00:00", "2010-01-12 13:00:00"),
    ]
        
    assert result == expected   

def test_touching_intervals():
    range1 = [("2010-01-12 10:00:00", "2010-01-12 11:00:00")]
    range2 = [("2010-01-12 11:00:00", "2010-01-12 12:00:00")]
    result = compute_overlap_time(range1, range2)
    expected = [("2010-01-12 11:00:00", "2010-01-12 11:00:00")]
    assert result == expected