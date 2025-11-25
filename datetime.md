## Python Date & Time Notes (datetime module)

This cheat‑sheet covers Python's built‑in `datetime` facilities: `date`, `time`, `datetime`, `timedelta`, `timezone` handling, parsing & formatting, arithmetic, best practices, and common pitfalls.

---
### 1. Core Classes

Import once:
```py
from datetime import date, time, datetime, timedelta, timezone
import calendar
```

Class | Purpose | Key attributes
----- | ------- | --------------
`date` | Calendar date (year, month, day) | `year`, `month`, `day`
`time` | Time of day (no date) | `hour`, `minute`, `second`, `microsecond`, `tzinfo`
`datetime` | Combines date + time | All of above
`timedelta` | Duration difference | `days`, `seconds`, `microseconds`
`timezone` | Fixed UTC offset | `utcoffset()`

Naive vs Aware:
- Naive objects: no timezone info (`tzinfo is None`).
- Aware objects: have `tzinfo` (offset from UTC) enabling reliable conversion & arithmetic.

### 2. Getting Current Date/Time
```py
today = date.today()              # Local date (naive)
now_local = datetime.now()        # Local datetime (naive)
now_utc = datetime.utcnow()       # UTC naive (avoid; prefer aware below)
now_aware_utc = datetime.now(timezone.utc)  # Aware UTC
```

Why prefer `datetime.now(timezone.utc)`: returns an aware UTC datetime; easier to convert safely.

### 3. Creating Instances
```py
some_date = date(2025, 11, 24)
some_time = time(14, 30, 5, 123456)              # 14:30:05.123456
dt = datetime(2025, 11, 24, 14, 30, 5, 0)        # naive
dt_aware = datetime(2025, 11, 24, 14, 30, tzinfo=timezone.utc)
```
Note: Validate ranges (month 1–12, hour 0–23). Invalid values raise `ValueError`.

### 4. Timedelta (Durations)
```py
delta = timedelta(days=2, hours=5)   # hours converted into seconds internally
future = dt + delta
past = dt - timedelta(days=1)
diff = future - past                 # returns timedelta
delta_days = diff.days
total_seconds = diff.total_seconds()
```
Negative timedeltas are allowed.

### 5. Formatting (to String)
Use `strftime` on date/datetime/time:
```py
formatted = dt.strftime('%Y-%m-%d %H:%M:%S')
iso = dt.isoformat()  # '2025-11-24T14:30:05'
date_str = today.strftime('%d/%m/%Y')
```
Common `strftime` directives:
- `%Y` year (4-digit) | `%y` year (2-digit)
- `%m` month (01–12) | `%d` day (01–31)
- `%H` hour (00–23) | `%I` hour (01–12) | `%p` AM/PM
- `%M` minute | `%S` second | `%f` microsecond
- `%z` UTC offset | `%Z` timezone name
- `%a` abbreviated weekday | `%A` full weekday | `%w` weekday number (0=Sun)
- `%j` day of year (001–366)
- `%U/%W` week number (Sunday/Monday as first day)

### 6. Parsing Strings
```py
dt_parsed = datetime.strptime('2025-11-24 14:30:05', '%Y-%m-%d %H:%M:%S')
date_parsed = datetime.strptime('24/11/2025', '%d/%m/%Y').date()
```
For ISO 8601:
```py
iso_dt = datetime.fromisoformat('2025-11-24T14:30:05')          # Python 3.7+
iso_dt_utc = datetime.fromisoformat('2025-11-24T14:30:05+00:00')
```
Robust parsing (varied human inputs): consider `dateutil.parser.parse` (external library) or `pendulum`.

### 7. Weekday & Calendar Info
```py
w = some_date.weekday()   # Monday=0 ... Sunday=6
isoweekday = some_date.isoweekday()  # Monday=1 ... Sunday=7
week_number = some_date.isocalendar().week
year, week, iso_weekday = some_date.isocalendar()
```
Calendar utilities:
```py
calendar.monthrange(2025, 11)  # (weekday_of_first_day, number_of_days) -> (5,30)
list(calendar.Calendar().itermonthdates(2025, 11))  # iterate over month grid dates
```

### 8. Timezones & Conversion
Built‑in `timezone.utc` gives a fixed UTC offset. For real-world zones (DST) use `zoneinfo` (Python 3.9+) or `pytz` (legacy).
```py
from zoneinfo import ZoneInfo
dt_ny = datetime(2025, 11, 24, 9, 30, tzinfo=ZoneInfo('America/New_York'))
dt_utc = dt_ny.astimezone(timezone.utc)
dt_tokyo = dt_ny.astimezone(ZoneInfo('Asia/Tokyo'))
```
Creating aware local now:
```py
now_ny = datetime.now(ZoneInfo('America/New_York'))
```
Never attach a timezone by simply assigning `.tzinfo` to a naive datetime for regions with DST. Instead, construct with `tzinfo` directly OR convert from naive UTC using `replace(tzinfo=timezone.utc)` only if you are certain the naive value represents UTC.

### 9. Making Naive → Aware Safely
Scenario: You received a naive timestamp that is actually UTC.
```py
naive = datetime.utcnow()  # naive UTC
aware = naive.replace(tzinfo=timezone.utc)
```
If naive is local time, convert using `ZoneInfo`:
```py
local_naive = datetime(2025,11,24,11,0,0)  # local wall time
local_aware = local_naive.replace(tzinfo=ZoneInfo('Asia/Kolkata'))  # OK only if you KNOW it's that zone
```

### 10. Arithmetic & Comparisons
You can add/subtract timedeltas and compare datetimes (must both be aware of same or convertible tz, or both naive).
```py
remaining = dt_aware - datetime.now(timezone.utc)
if remaining.total_seconds() <= 0:
    print('Expired')
```
Comparing naive with aware raises `TypeError` in modern Python versions.

### 11. Rounding / Truncation
```py
truncated = dt.replace(microsecond=0)       # remove microseconds
dt_minute = dt.replace(second=0, microsecond=0)
```
Floor to day:
```py
day_start = dt.replace(hour=0, minute=0, second=0, microsecond=0)
```
Custom rounding (`timedelta` arithmetic):
```py
def round_minutes(d: datetime, minutes=5):
    discard = timedelta(minutes=d.minute % minutes,
                        seconds=d.second,
                        microseconds=d.microsecond)
    return d - discard
```

### 12. Measuring Elapsed Time
Use `time.perf_counter()` for precise intervals, not `datetime.now()` (clock adjustments may skew).
```py
import time
start = time.perf_counter()
do_work()
elapsed = time.perf_counter() - start
```
For wall-clock stamps, `datetime.now(timezone.utc)`. For durations, `perf_counter` or `monotonic`.

### 13. Serialization
```py
json_ready = dt_aware.isoformat()  # '2025-11-24T14:30:05+00:00'
parsed_back = datetime.fromisoformat(json_ready)
```
Store in UTC ISO string or UNIX epoch (`dt.timestamp()`). Convert epoch to datetime:
```py
ts = dt_aware.timestamp()              # float seconds since epoch
from_ts = datetime.fromtimestamp(ts, timezone.utc)
```

### 14. Common Pitfalls
- Mixing naive and aware datetimes → `TypeError` or silent logic errors.
- Using `datetime.utcnow()` widely then later needing timezone handling — start with aware UTC.
- Relying on `strftime('%Z')` for timezone name portability; names differ and may be empty.
- Using `replace(tzinfo=ZoneInfo(...))` on naive datetimes that were not UTC or not guaranteed to be in that zone (DST mistakes).
- Week numbers (`%W`, `%U`) vary by definition; for ISO weeks use `isocalendar()`.
- Parsing ambiguous human times (12-hour clock without AM/PM) — validate inputs.

### 15. Best Practices Summary
- Store datetimes in UTC (aware) internally.
- Convert to local timezone only at I/O boundaries (display, logs).
- Use `zoneinfo` (standard) over `pytz` for new code (Python ≥3.9).
- Always annotate timezone expectations in code comments.
- Avoid mutable global timezone objects; pass explicit `ZoneInfo` or `tzinfo`.
- Prefer `timedelta` arithmetic over manual seconds math.
- Use monotonic clock (`time.perf_counter`) for measuring durations.

### 16. Useful Snippets
Days until end of month:
```py
def days_remaining_in_month(d: date) -> int:
    _, last = calendar.monthrange(d.year, d.month)
    return last - d.day
```
Generate hourly range:
```py
def hours_range(start: datetime, hours: int):
    for i in range(hours):
        yield start + timedelta(hours=i)
```
Next occurrence of weekday (0=Mon):
```py
def next_weekday(d: date, weekday: int) -> date:
    w = d.weekday()
    delta = (weekday - w) % 7 or 7
    return d + timedelta(days=delta)
```

### 17. External Libraries (When needed)
- `zoneinfo` — IANA time zones (standard library in 3.9+).
- `dateutil` — flexible parsing, relative deltas (`relativedelta`).
- `pendulum` — rich timezone, formatting, and intervals.
- `arrow` — user-friendly wrapper (simplifies conversions & formatting).

---
If you want, I can add a `datetime_examples.py` file with runnable demonstrations or a small test suite—just ask.
