# Gym-analytics dashboard
import json

# --- Data (simulated API responses) ---
real_members = [
    {"name": "Jimmy Juma",   "run": 15,  "protocol": "OMAD", "glasses": 5.0, "workout": True},
    {"name": "Debie njeri",  "run": 10,  "protocol": "2MAD", "glasses": 8.0, "workout": True},
    {"name": "Jeff Mbeta",   "run": 12,  "protocol": "OMAD", "glasses": 6.0, "workout": False},
    {"name": "Nancy Kawira", "run": 9,   "protocol": "OMAD", "glasses": 7.0, "workout": True},
    {"name": "Peter Kimeu",  "run": 11,  "protocol": "2MAD", "glasses": 9.0, "workout": True},
    {"name": "Kevin Kuria",  "run": 13,  "protocol": "OMAD", "glasses": 7.0, "workout": True},
]
daily_runs = [58, 60, 64, 72, 78, 80, 71]
day_names   = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
session_list = [
    {"name": "boxing",     "enrolled": 9},
    {"name": "karate",     "enrolled": 11},
    {"name": "muay_thai",  "enrolled": 14},
    {"name": "yoga",       "enrolled": 12},
    {"name": "wrestling",  "enrolled": 7},
]

# --- Process ---
RUN_GOAL = 12 
goal_met = [m for m in real_members if m["run"] >= RUN_GOAL]
avg_run = round(sum(m["run"] for m in real_members) / len(real_members))
workouts_done = sum(1 for m in real_members if m["workout"])
best_day  = day_names[daily_runs.index(max(daily_runs))]
top_session = max(session_list, key=lambda s: s["enrolled"])
avg_glasses = round(sum(m["glasses"] for m in real_members) / len(real_members))

# --- Output ---
W = 52
print("=" * W)
print(f"  SMP GYM DASHBOARD  |  Week 2026-W30")
print("=" * W)

print(f"\n  SECTION 1: MEMBER PERFORMANCE")
print(f"  {'Total members:':<28} {len(real_members)}")
print(f"  {'Hit {RUN_GOAL:,} run goal:':}")
print(f"  Hit {RUN_GOAL:,} km run goal:          {len(goal_met)}/{len(real_members)}")
print(f"  {'Average run:':<28} {avg_run:,} Km")
print(f"  {'workouts today:':<28} {workouts_done}/{len(real_members)}")
print(f"  Goal hitters: {', '.join(m['name'] for m in goal_met)}")
print(f"  Average water glasses taken: {avg_glasses} ")
print(f"  OMAD Observers:")
print(f"    {'NAME':<28} {'PROTOCOL'}") 
for i, m in enumerate(real_members, 1):
    if m["protocol"] == "OMAD":
        print(f"{i}   {m['name']:<28} {m['protocol']}")

print(f"\n  SECTION 2: WEEKLY RUNS")
for day, total in zip(day_names, daily_runs):
    bar = "#" * (total // 10)
    print(f"  {day:4} {total:>7,}  {bar}")
print(f"  Best day: {best_day} ({max(daily_runs):,} total runs)")
print(f"  Week avg: {round(sum(daily_runs)/len(daily_runs)):,} run/day")

print(f"\n  SECTION 3: ACTIVE SESSSIONS")
for s in sorted(session_list, key=lambda x: -x["enrolled"]):
    print(f"  {s['name']:15} {s['enrolled']} enrolled")
print(f"  Most popular: {top_session['name']} ({top_session['enrolled']} enrolled)")

print(f"\n{'=' * W}")

# JSON export
export = {
    "week": "2026-W30",
    "members": {"total": len(real_members), "goal_met": len(goal_met), "avg_run": avg_run},
    "weekly": {"best_day": best_day, "total_run": sum(daily_runs)},
    "skills": {"active": len(session_list), "most_popular": top_session["name"]}
}
print("\nJSON export:")
print(json.dumps(export, indent=2))

with open("log.json", "r") as f:
    data = json.load(f)