from intervals import overlapping_intervals

def test_overlapping_intervals():
    assert overlapping_intervals((1, 5), (3, 6)) == True
    assert overlapping_intervals((2, 5), (7, 10)) == False 
    assert overlapping_intervals((0, 4), (4, 0)) == True
    assert overlapping_intervals((1, 2), (2, 3)) == True
    assert overlapping_intervals((1, 2), (3, 4)) == False

