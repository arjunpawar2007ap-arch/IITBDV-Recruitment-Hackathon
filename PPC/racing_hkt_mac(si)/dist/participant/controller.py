'''
PPC Hackathon — Participant Boilerplate
You must implement two functions: plan() and control()
'''

# ─── TYPES (for reference) ────────────────────────────────────────────────────

# Path: list of waypoints [{"x": float, "y": float}, ...]
# State: {"x", "y", "yaw", "vx", "vy", "yaw_rate"} 
# CmdFeedback: {"throttle", "steer"}         

# ─── CONTROLLER ───────────────────────────────────────────────────────────────
import numpy as np

def steering(path: list[dict], state: dict) -> float:
 
    if not path:
        return 0.0

    pos_x, pos_y, yaw = state["x"], state["y"], state["yaw"]
    vx = state["vx"]

    
    closest_idx = min(range(len(path)),
                      key=lambda i: (path[i]["x"]-pos_x)**2 + (path[i]["y"]-pos_y)**2)

    lookahead_steps = int(5 + vx * 1.0)
    lookahead_steps = max(5, min(lookahead_steps, 15))
    lookahead_idx = min(closest_idx + lookahead_steps, len(path) - 1)

    target = path[lookahead_idx]

   
    dx = target["x"] - pos_x
    dy = target["y"] - pos_y
    angle_to_target = np.arctan2(dy, dx)
    heading_error = angle_to_target - yaw
    heading_error = (heading_error + np.pi) % (2 * np.pi) - np.pi

    steer = 0.6 * heading_error
    return float(np.clip(steer, -0.5, 0.5))


def throttle_algorithm(target_speed, current_speed, dt):
   
    error = target_speed - current_speed
    if error > 0:
        throttle = float(np.clip(error * 0.5, 0.0, 1.0))
        brake = 0.0
    else:
        throttle = 0.0
        brake = float(np.clip(-error * 0.3, 0.0, 1.0))
    return throttle, brake


def control(
    path: list[dict],
    state: dict,
    cmd_feedback: dict,
    step: int,
) -> tuple[float, float, float]:
  
    steer = steering(path, state)

   
    if abs(steer) > 0.2:
        target_speed = 3.5
    else:
        target_speed = 5.0

    throttle, brake = throttle_algorithm(target_speed, state["vx"], 0.05)

    return throttle, steer, brake        
    

