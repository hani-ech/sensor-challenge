import numpy as np

class Sensor:
    """Represents a single sensor and its measurements."""

    def __init__(self, name, measurements):
        self.name = name
        self.measurements = np.array(measurements, dtype=int)  # Store as NumPy array

    def count_exceedances(self, thresholds):
        """Returns a NumPy array of counts for how many measurements exceed each threshold."""
        thresholds = np.array(thresholds, dtype=int)  # Convert thresholds to NumPy array
        return np.sum(self.measurements[:, None] > thresholds, axis=0)  # Vectorized exceedance count


class SensorProcessor:
    """Handles input parsing, processing, and result formatting."""

    def __init__(self, input_data):
        self.sensors = []
        self.thresholds = []
        self._parse_input(input_data)

    def _parse_input(self, input_data):
        """Parses the input data to extract sensor measurements and thresholds."""
        lines = input_data.strip().split("\n")

        if len(lines) < 2:
            raise ValueError("❌ Invalid input: Expected at least two lines (metadata & thresholds).")

        try:
            n, _ = map(int, lines[0].split())  # Number of sensors (n) & number of thresholds (ignored)
            self.thresholds = np.array(list(map(int, lines[1].split())), dtype=int)  # Store thresholds as NumPy array
        except ValueError:
            raise ValueError("❌ Invalid input: First two lines must contain numbers.")

        if len(lines) < 2 + n:
            raise ValueError(f"❌ Invalid input: Expected {n} sensor lines but found {len(lines) - 2}.")

        # Efficient batch processing: Collect all measurements first
        sensor_names = []
        sensor_data = []

        for i, line in enumerate(lines[2:]):  # Skip metadata & thresholds
            if "," in line:  # File input case (comma-separated)
                sensor_name = f"S{i+1}"
                measurements = list(map(int, line.split(",")))
            else:  # Stdin input case (space-separated)
                parts = line.split()
                sensor_name = parts[0]
                measurements = list(map(int, parts[1:]))

            sensor_names.append(sensor_name)
            sensor_data.append(measurements)

        # Convert to a single NumPy array for fast computation
        self.sensor_names = sensor_names
        self.sensor_data = np.array(sensor_data, dtype=int)

    def process(self):
        """Processes all sensors using vectorized operations and returns formatted results."""
        exceedances = np.sum(self.sensor_data[:, :, None] > self.thresholds, axis=1)  # Fully vectorized count
        results = [f"{name} {' '.join(map(str, counts))}" for name, counts in zip(self.sensor_names, exceedances)]
        return results
