# Install

```bash
git clone https://github.com/mvexel/closest.git
cd closest
pip install -r requirements.txt
```

# Run

```bash
python app.py
```

# Use

```bash
curl "http://localhost:5000/closest?lat=40.7500&lon=-111.8833&radius=1000"
```

Should get you:

```json
[{"details": {"city": "Salt Lake City", "wikipedia": "Salt_Lake_City"}, "distance": 0.025257331757996413}, {"details": {"city": "Las Vegas", "wikipedia": "Las_Vegas,_Nevada"}, "distance": 582.4596227040414}, {"details": {"city": "Denver", "wikipedia": "Denver"}, "distance": 596.0062234147682}, {"details": {"city": "Albuquerque", "wikipedia": "Albuquerque,_New_Mexico"}, "distance": 779.8919659216617}, {"details": {"city": "Phoenix", "wikipedia": "Phoenix,_Arizona"}, "distance": 813.3287513033781}, {"details": {"city": "Sacramento", "wikipedia": "Sacramento,_California"}, "distance": 855.2101604288163}, {"details": {"city": "Riverside", "wikipedia": "Riverside,_California"}, "distance": 899.5830676895046}, {"details": {"city": "Los Angeles", "wikipedia": "Los_Angeles"}, "distance": 932.3412435593556}, {"details": {"city": "Mexicali", "wikipedia": "Mexicali"}, "distance": 953.1080966994609}, {"details": {"city": "Tucson", "wikipedia": "Tucson,_Arizona"}, "distance": 954.0909110501495}, {"details": {"city": "San Francisco", "wikipedia": "San_Francisco"}, "distance": 964.3836292852318}]
```
