import numpy as np

def process_sensor_data(file_path=None):
    """
    Reads sensor data from a file or stdin, processes it, and prints the results.
    """
    if file_path:
        with open(file_path, "r") as f:
            input_data = f.read().strip().split("\n")
    else:
        import sys
        input_data = sys.stdin.read().strip().split("\n")

    # Parse first line (number of sensors, number of measurements per sensor)
    n, m = map(int, input_data[0].split())
    
    # Parse thresholds
    thresholds = list(map(int, input_data[1].split()))
    
    results = []
    
    # Process each sensor
    for i, line in enumerate(input_data[2:2 + n]):  # Skip first two lines
        measurements = np.array(list(map(int, line.strip().split(","))))  # Convert to NumPy array
        sensor_name = f"S{i+1}"  # Generate sensor names (S1, S2, ...)
        
        # Count values exceeding each threshold using NumPy
        counts = [np.sum(measurements > threshold) for threshold in thresholds]
        
        # Store result
        results.append(f"{sensor_name} {' '.join(map(str, counts))}")
    
    # Print results
    for result in results:
        print(result)
