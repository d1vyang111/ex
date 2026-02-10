# scripts/mpops_commit.py
import json, time

with open("current_perf.json") as f:
    data = json.load(f)

data["timestamp"] = time.time()

with open("baseline_perf.json", "w") as f:
    json.dump(data, f, indent=2)

print("MPOps commit created")
