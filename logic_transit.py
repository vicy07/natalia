# logic_transit.py
from astro_core import calculate_chart
from typing import Optional

def transits(
    natal_date,
    natal_time,
    natal_place: Optional[str],
    natal_tz_offset,
    transit_date,
    transit_time="00:00",
    latitude: Optional[float] = None,
    longitude: Optional[float] = None,
):
    natal, err = calculate_chart(natal_date, natal_time, natal_place, natal_tz_offset, latitude, longitude)
    if err:
        return err
    trans, err2 = calculate_chart(transit_date, transit_time, natal_place, natal_tz_offset, latitude, longitude)
    if err2:
        return err2
    orb_luminaries = 8
    orb_planets = 6
    aspect_defs = [
        (0, "Conjunction", "☌"),
        (60, "Sextile", "✶"),
        (90, "Square", "□"),
        (120, "Trine", "△"),
        (180, "Opposition", "☍")
    ]
    personal_planets = ["Sun", "Moon", "Mercury", "Venus", "Mars"]
    transit_aspects = []
    for tn, td in trans["planet_degrees"].items():
        for nn, nd in natal["planet_degrees"].items():
            diff = abs((td - nd + 180) % 360 - 180)
            orb = orb_luminaries if tn in ["Sun", "Moon"] or nn in ["Sun", "Moon"] else orb_planets
            for ang, name, sym in aspect_defs:
                if abs(diff - ang) <= orb:
                    transit_aspects.append({
                        "transit": tn,
                        "natal": nn,
                        "type": name,
                        "symbol": sym,
                        "angle": round(diff, 2),
                        "personal": tn in personal_planets or nn in personal_planets
                    })
    return {
        "natal": {
            "date": natal_date,
            "time": natal_time,
            "place": natal_place,
            "planet_degrees": natal["planet_degrees"]
        },
        "transit": {
            "date": transit_date,
            "time": transit_time,
            "planet_degrees": trans["planet_degrees"]
        },
        "aspects": transit_aspects
    }
