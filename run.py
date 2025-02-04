import argparse
import sys
import time
from sensor_processor.processor import SensorProcessor

def main():
    # Argument parser for file input
    parser = argparse.ArgumentParser(description="Process sensor data from a file or stdin.")
    parser.add_argument("--file", nargs="?", const="data.txt", type=str, help="Path to the sensor data file (default: data.txt if no file specified)")
    args = parser.parse_args()


    # Read input from file or stdin
    if args.file:
        with open(args.file, "r") as f:
            input_data = f.read().strip()  # Read from file and remove extra spaces
    else:
        print("\nEnter sensor data (press Ctrl+D when done):")
        input_data = sys.stdin.read().strip()  # Read **full multiline input** from stdin
        

    print("\n⏳ Processing started...")

    # Tic: Start timing
    tic = time.time()

    # Process the data
    processor = SensorProcessor(input_data)
    results = processor.process()

    # Toc: End timing
    toc = time.time()

    # Print results
    for result in results:
        print(result)

    # Print execution time
    print(f"\n✅ Processing completed in {toc - tic:.4f} seconds")

if __name__ == "__main__":
    main()
