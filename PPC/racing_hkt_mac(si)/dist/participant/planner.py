'''
PPC Hackathon — Participant Boilerplate
You must implement two functions: plan() and control()
'''

# ─── TYPES (for reference) ────────────────────────────────────────────────────

# Cone: {"x": float, "y": float, "side": "left" | "right", "index": int}
# State: {"x", "y", "yaw", "vx", "vy", "yaw_rate"}  
# CmdFeedback: {"throttle", "steer"}        

# ─── PLANNER ──────────────────────────────────────────────────────────────────
import numpy as np

def plan(cones: list[dict]) -> list[dict]:
 

    blue   = [c for c in cones if c["side"] == "left"]
    yellow = [c for c in cones if c["side"] == "right"]

    if not blue or not yellow:
        return []

    midpoints = []
    for b in blue:
        nearest = min(yellow, key=lambda y: (y["x"]-b["x"])**2 + (y["y"]-b["y"])**2)
        midpoints.append({"x": (b["x"]+nearest["x"])/2.0,
                          "y": (b["y"]+nearest["y"])/2.0})
    for y in yellow:
        nearest = min(blue, key=lambda b: (b["x"]-y["x"])**2 + (b["y"]-y["y"])**2)
        midpoints.append({"x": (y["x"]+nearest["x"])/2.0,
                          "y": (y["y"]+nearest["y"])/2.0})

    
    ordered = [midpoints[0]]
    remaining = midpoints[1:]
    while remaining:
        last = ordered[-1]
        nearest_idx = min(range(len(remaining)),
                          key=lambda i: (remaining[i]["x"]-last["x"])**2 +
                                        (remaining[i]["y"]-last["y"])**2)
        ordered.append(remaining.pop(nearest_idx))

    
    smoothed = []
    for i in range(len(ordered)):
        i_prev = max(0, i - 2)
        i_next = min(len(ordered) - 1, i + 2)
        neighbors = ordered[i_prev:i_next+1]
        avg_x = sum(p["x"] for p in neighbors) / len(neighbors)
        avg_y = sum(p["y"] for p in neighbors) / len(neighbors)
        smoothed.append({"x": avg_x, "y": avg_y})

  
    dense = []
    for i in range(len(smoothed) - 1):
        p0 = smoothed[i]
        p1 = smoothed[i + 1]
        for t in [0.0, 0.2, 0.4, 0.6, 0.8]:
            dense.append({
                "x": p0["x"] + t * (p1["x"] - p0["x"]),
                "y": p0["y"] + t * (p1["y"] - p0["y"])
            })
    dense.append(smoothed[-1])

    return dense
