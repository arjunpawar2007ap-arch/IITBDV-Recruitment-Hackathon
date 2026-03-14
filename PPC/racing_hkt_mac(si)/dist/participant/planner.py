
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
    """
    Generate a path from the cone layout.
    Called ONCE before the simulation starts.

    Args:
        cones: List of cone dicts with keys x, y, side ("left"/"right"), index

    Returns:
        path: List of waypoints [{"x": float, "y": float}, ...]
              Ordered from start to finish.
    
    Tip: Try midline interpolation between matched left/right cones.
         You can also compute a curvature-optimised racing line.
    """
    path = []
    # TODO: implement your path planning here
    blue = np.array([[cone["x"], cone["y"]] for cone in cones if cone["side"] == "left"])
    yellow = np.array([[cone["x"], cone["y"]] for cone in cones if cone["side"] == "right"])

    # implement a planning algorithm to generate a path from the blue and yellow cones

    if len(blue) == 0 or len(yellow) == 0:
        return path
        
    for b_cone in blue 
        distances = np.linalg.norm(yellow - b_cone, axis=1)
        closest_idx = np.argmin(distances)
        nearest_yellow = yellow[closest_idx]
        
        mid_x = (b_cone[0] + nearest_yellow[0]) / 2
        mid_y = (b_cone[1] + nearest_yellow[1]) / 2
        
        path.append({"x": float(mid_x), "y": float(mid_y)})
        path = sorted(path, key=lambda p: p["x"])

    return path

