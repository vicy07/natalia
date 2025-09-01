# logic_natal.py
from fastapi import Query, Response
from typing import Optional
from astro_core import calculate_chart
from chart_draw import draw_chart

def natal_chart_calc(
    date: str,
    time: str,
    place: Optional[str],
    tz_offset: int,
    latitude: Optional[float] = None,
    longitude: Optional[float] = None,
):
    data, err = calculate_chart(date, time, place, tz_offset, latitude, longitude)
    return err or data

def natal_chart_image(
    date: str,
    time: str,
    place: Optional[str],
    tz_offset: int,
    latitude: Optional[float] = None,
    longitude: Optional[float] = None,
):
    data, err = calculate_chart(date, time, place, tz_offset, latitude, longitude)
    if err:
        return err
    img = draw_chart(
        data["planet_degrees"],
        data["houses"],
        data["aspects"],
        data["retrograde_planets"],
        data.get("house_rulers")
    )
    return Response(content=img, media_type="image/png")
