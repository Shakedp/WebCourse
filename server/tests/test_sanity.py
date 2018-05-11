from server import calc


def test_display_single():
    print(calc.calculate_next_state(None, 1))