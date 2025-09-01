# logic_horary.py
from astro_core import calculate_chart
from typing import Optional

def horary_chart(
    date,
    time,
    place: Optional[str],
    tz_offset,
    latitude: Optional[float] = None,
    longitude: Optional[float] = None,
):
    data, err = calculate_chart(date, time, place, tz_offset, latitude, longitude)
    if err:
        return err
    return {
        "type": "horary",
        "question_time": f"{date} {time}",
        "place": place,
        "chart": data
    }
