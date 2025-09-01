# 🧭 Natalia – Astrological Natal Chart Generator

**Natalia** is a simple and reliable Python library and API for calculating and visualizing natal (birth) charts by date, time, and place of birth.

---

## ✨ Features

- ✅ Calculates planetary positions (Sun, Moon, Mercury, etc.) using Swiss Ephemeris
- 🌐 Determines astrological houses (Placidus)
- 📐 Calculates aspects between planets
- 🖼️ Generates beautiful natal chart images (PNG)
- 🚀 REST API with FastAPI
- 🧪 Unit tests included

---

## 🚀 Quick Start

### Requirements

- Python ≥ 3.8
- Dependencies: `swisseph`, `matplotlib`, `numpy`, `geopy`, `fastapi`, `uvicorn`

### Installation

Clone the repository and install dependencies:

```bash
pip install -r requirements.txt
```

### Usage as a Library

```python
from main import calculate_chart, draw_chart

# Calculate chart data
chart, err = calculate_chart('1990-05-17', '14:30', 'Riga', 3)
if err:
    print(err)
else:
    # Draw chart image
    img_bytes = draw_chart(chart['planet_degrees'], chart['houses'], chart['aspects'], chart['retrograde_planets'])
    with open('chart.png', 'wb') as f:
        f.write(img_bytes)
```

### Usage as an API

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Once running, open the interactive **Swagger UI** at
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to explore and try the API endpoints.
You can also view the alternative ReDoc documentation at
[http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).

#### Available endpoints and example calls

All endpoints accept either a human‑readable `place` or explicit `latitude` and `longitude` coordinates.

- **Natal chart** – snapshot of the heavens at birth showing the core personality blueprint  
  `GET /natal_chart/calc`  
  `GET /natal_chart/image`
  ```bash
  curl "http://127.0.0.1:8000/natal_chart/image?date=1994-01-15&time=17:45&place=Millerovo,%20Rostov%20Oblast,%20Russia&tz_offset=3" --output chart.png
  ```

- **Synastry** – compares two natal charts to evaluate relationship dynamics  
  `GET /synastry`  
  `GET /synastry/analytics`  
  `GET /synastry/image`
  ```bash
  curl "http://127.0.0.1:8000/synastry?date1=1990-05-17&time1=14:30&place1=Riga&tz_offset1=3&date2=1992-08-05&time2=09:15&place2=Berlin&tz_offset2=1"
  ```

- **Transits** – shows current planetary movements against the natal chart for forecasting  
  `GET /transits`
  ```bash
  curl "http://127.0.0.1:8000/transits?natal_date=1994-01-15&natal_time=17:45&natal_place=Millerovo&natal_tz_offset=3&transit_date=2024-06-01"
  ```

- **Horary chart** – casts a chart for the moment a question is asked to glean guidance  
  `GET /horary_chart`
  ```bash
  curl "http://127.0.0.1:8000/horary_chart?date=2024-05-01&time=12:00&place=Riga&tz_offset=3"
  ```

- **Weekly forecast** – seven‑day personal outlook derived from natal data and daily transits  
  `GET /weekly_forecast`
  ```bash
  curl "http://127.0.0.1:8000/weekly_forecast?date=1994-01-15&time=17:45&place=Millerovo&tz_offset=3&start_date=2024-06-01"
  ```


---

## 🧪 Running Unit Tests

Before running the tests make sure all dependencies are installed:

```bash
pip install -r requirements.txt
```

To run all unit tests locally:

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
```

Or using Docker (from the project root):

```bash
# Map the current folder as a volume to access generated files (e.g., test_chart.png):
docker build -t natalia-tests -f tests/Dockerfile .
docker run --rm -v ${PWD}:/app natalia-tests
```

> **Note:** Mapping the volume with `-v ${PWD}:/app` allows you to access files created by tests (like `test_chart.png`) on your host machine.

---

## 📦 Project Structure

- `main.py` — Main logic, FastAPI app, chart calculation and drawing
- `tests/` — Unit tests
- `requirements.txt` — Python dependencies
- `Dockerfile`, `docker-compose.yml` — For containerized usage

---

## License
MIT
