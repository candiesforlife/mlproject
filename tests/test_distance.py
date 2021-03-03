from mlproject.distance import haversine

def test_dist():
    assert haversine(2.380009, 48.865070, 2.3514616, 48.8566969) == 2.2864989955090875
    assert type(haversine(2.380009, 48.865070, 2.3514616, 48.8566969))==float
