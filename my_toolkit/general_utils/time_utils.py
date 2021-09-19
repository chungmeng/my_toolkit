from datetime import datetime, timedelta

def delta_days(date, days, dt_format='%Y-%m-%d'):
    """
    Given a Date String, returns Date String with Delta Days
    ie. Given '2020-10-05' with days=-3, Returns '2020-10-02'
    Args:
        date: Date (str)
        days: Delta Days (int)
    Returns:
        date: Date (str)
    """
    new_date=datetime.strptime(date, dt_format)+timedelta(days=days)
    return datetime.strftime(new_date, dt_format)