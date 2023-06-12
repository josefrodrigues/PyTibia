from src.utils.coordinate import getDirectionBetweenCoordinates


def test_should_return_right_when_next_x_coordinate_is_greather_than_current_x_coordinate():
    coordinate = (0, 0, 0)
    nextCoordinate = (1, 0, 0)
    assert getDirectionBetweenCoordinates(coordinate, nextCoordinate) == 'right'

def test_should_return_left_when_current_x_coordinate_is_greather_than_next_x_coordinate():
    coordinate = (1, 0, 0)
    nextCoordinate = (0, 0, 0)
    assert getDirectionBetweenCoordinates(coordinate, nextCoordinate) == 'left'

def test_should_return_down_when_next_y_coordinate_is_greather_than_current_y_coordinate():
    coordinate = (0, 0, 0)
    nextCoordinate = (0, 1, 0)
    assert getDirectionBetweenCoordinates(coordinate, nextCoordinate) == 'down'

def test_should_return_up_when_currnet_y_coordinate_is_greather_than_next_y_coordinate():
    coordinate = (0, 1, 0)
    nextCoordinate = (0, 0, 0)
    assert getDirectionBetweenCoordinates(coordinate, nextCoordinate) == 'up'

def test_should_return_None_when_x_or_y_are_equals():
    coordinate = (0, 0, 0)
    nextCoordinate = (0, 0, 0)
    assert getDirectionBetweenCoordinates(coordinate, nextCoordinate) is None
