import datetime

today = datetime.datetime.now()
epoch_time = datetime.datetime(1970, 1, 1)
delta = today - epoch_time
delta_seconds = delta.total_seconds()

print(f"Seconds since January 1, 1970: {delta_seconds:,.4f} or \
{delta_seconds:.2e} in scientific notation")

print(today.strftime("%b %d %Y"))
