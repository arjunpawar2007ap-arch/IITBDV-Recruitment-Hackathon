# IITBDV Recruitment Hackathon

**Name:** Arjun Pawar  
**Roll Number:** 25b2286

## Approach

### Planner
- Separated cones into left (blue) and right (yellow)
- For each cone on both sides, found the nearest partner cone 
  and computed the midpoint between them
- Sorted midpoints into track order using greedy nearest-neighbour
- Smoothed the path by averaging neighboring waypoints to reduce jitter
- Densified the path by interpolating extra points between waypoints 
  so the car always has a nearby point to follow

### Controller
- Found the closest waypoint to the car at each timestep
- Used a speed-based lookahead: at low speed look 5 steps ahead, 
  at high speed look up to 15 steps ahead
- Steered proportionally to the heading error toward the lookahead point
- Slowed to 3.5 m/s when steering hard (cornering), 
  otherwise maintained 5 m/s

## Result
- Lap complete ✅
- Cone hits: 0
- Final score: 31.36s
