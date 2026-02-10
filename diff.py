
import json
import sys

with open("baseline_perf.json") as f:
    base = json.load(f)

with open("current_perf.json") as f:
    curr = json.load(f)

delta = curr["accuracy"] - base["accuracy"]

print("Accuracy delta:", delta)

if delta < -0.02:
    print("❌ MPOps regression detected")
    sys.exit(1)

print("✅ MPOps check passed")
