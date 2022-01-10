import sys
sys.path.append('c:\\users\\kyle\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.7_qbz5n2kfra8p0\\localcache\\local-packages\\python37\\site-packages')

import pyrealsense2 as rs
from statistics import median

try:
    # Create a context object. This object owns the handles to all connected realsense devices
    pipeline = rs.pipeline()

    # Configure streams
    config = rs.config()
    config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

    # Start streaming
    pipeline.start(config)

    while True:

        frames = pipeline.wait_for_frames()
        depth = frames.get_depth_frame()
        if not depth: continue
        
        for x in range(640):
            points = {}
            for y in range(480):
                dist = depth.get_distance(x, y)
                if 0 < dist and dist < 1: #edit to accept points within cartesian distance
                   points[y] = dist

            if len(points) != 0:
                if max(points) > 75: # any point is more than 8 in from ground
                    if (median(points) - min(points))/(points[median(points)]-points[min(points)]+.01) > 200 or (max(points) - median(points))/(points[max(points)]-points[median(points)]+.01) > 200: #if slope > 200 pixels per meter
                        print("Obstacle detected in column "+str(x))

        exit(0)


except Exception as e:
    print(e)
    pass
