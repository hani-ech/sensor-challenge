import argparse
import os
import time
from sensor_processor.processor import process_sensor_data

# Set up argument parser
parser = argparse.ArgumentParser(description="Process sensor data from a file or stdin.")
parser.add_argument("--file", type=str, help="Path to the sensor data file (optional)")
args = parser.parse_args()

# Select data source
DATA_FILE = args.file if args.file else "data.txt"

def main():
    # Measure start time
    start_time = time.time()

    # Check if file exists
    if os.path.exists(DATA_FILE):
        print(f"📂 Loading data from {DATA_FILE}...")
        process_sensor_data(DATA_FILE)
    else:
        print("⚠️ No data file found. Please provide data via stdin.")

    # Measure execution time
    end_time = time.time()
    print(f"\n⏳ Execution time: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()
