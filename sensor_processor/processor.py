import numpy as np

class Sensor:
    """Represents a single sensor and its measurements."""

    def __init__(self, name, measurements):
        self.name = name
        self.measurements = np.array(measurements)  # Store as NumPy array for efficiency

    def count_exceedances(self, thresholds):
        """Returns a list of counts for how many measurements exceed each threshold."""
        
        exceedances = [np.sum(self.measurements > t) for t in thresholds]
        
        return exceedances


class SensorProcessor:
    """Handles input parsing, processing, and result formatting."""
    
    def __init__(self, input_data):
        self.sensors = []
        self.thresholds = []
        self._parse_input(input_data)
        
    def _parse_input(self, input_data):
        """Parses the input data to extract sensor measurements and thresholds."""
        lines = input_data.strip().split("\n")

        # Validate input length
        if len(lines) < 2:
            raise ValueError("❌ Invalid input: Expected at least two lines (metadata & thresholds).")

        try:
            n, m = map(int, lines[0].split())  # Number of sensors & number of thresholds
            self.thresholds = list(map(int, lines[1].split()))  # Threshold values
        except ValueError:
            raise ValueError("❌ Invalid input: First two lines must contain numbers.")

        # Validate sensor data
        if len(lines) < 2 + n:
            raise ValueError(f"❌ Invalid input: Expected {n} sensor lines but found {len(lines) - 2}.")

        self.sensors = []

        for i, line in enumerate(lines[2:]):  # Skip first 2 lines (metadata + thresholds)

            if "," in line:  #  File input case (comma-separated)
                sensor_name = f"S{i+1}"
                measurements = list(map(int, line.split(",")))  # Convert CSV to integer list
            else:  #  Stdin input case (space-separated)
                parts = line.split()
                sensor_name = parts[0]
                measurements = list(map(int, parts[1:]))  # Convert remaining parts to integers

            
            self.sensors.append(Sensor(sensor_name, measurements))

    
    def process(self):
        """Processes all sensors and returns formatted results."""
        results = []
        for sensor in self.sensors:
            counts = sensor.count_exceedances(self.thresholds)
            results.append(f"{sensor.name} {' '.join(map(str, counts))}")  # Ensure clean formatting
        return results
