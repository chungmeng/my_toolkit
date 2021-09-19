from general_utils.time_utils import delta_days
from datetime import datetime

def inform_target_date(step=14):
    today = str(datetime.today().date())
    target = delta_days(today, step)
    print(f"Today's Date is {today}")
    print(f"With Delta {step} days ...")
    print(f"Target Date is {target}")

if __name__=='__main__':
    inform_target_date()

