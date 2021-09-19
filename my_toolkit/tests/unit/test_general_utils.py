from my_toolkit.general_utils.time_utils import delta_days

def test_delta_days():
    assert delta_days('2020-10-05', -2)=='2020-10-03'
    assert delta_days('2020-10-05', 2)=='2020-10-07'

