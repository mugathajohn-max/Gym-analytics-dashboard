# File: README.md

# Gym-analytics dashboard

multi-endpoint Gym-analytics dashboard that fetches from three data sources. 
Processes each source independently. 
Displays a structured command-centre report and exports data as json output.

## What It Does

- Fetches member data, weekly-run data and session data from.  
- Displays goal hiters, average run score, workout done and specific protocol observed. 
- Shows best day ran and the average run.
- displays sessions and their preference.
- Exports a report as JSON.


## Setup

```bash
pip install -r requirements.txt
```

## Usage

Run the dashboard:
```bash
python Gym-analytics.py
```

## Sample Output

```
 Hit 12 km run goal:          3/6
  Average run:                 12 Km
  workouts today:              5/6
  Goal hitters: Jimmy Juma, Jeff Mbeta, Kevin Kuria

Best day: Sat (80 total runs)
Week avg: 69 run/day

Most popular: muay_thai (14 enrolled)
```

## Stack

Python, Json
