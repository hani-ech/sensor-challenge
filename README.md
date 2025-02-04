# 📡 Sensor Data Processor

A Python package that reads sensor measurements from either **standard input (stdin)** or a **file**, then calculates how many values exceed given thresholds.

---

## ⚡ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/hani-ech/sensor-challenge.git
```

### 2️⃣ Set Up a Virtual Environment
```bash
python3 -m venv sensor-env
source sensor-env/bin/activate  # On Linux/macOS
```
or
```bash
sensor-env\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

## 🚀 Usage

### 🔹 Option 1: Manual Input (stdin)

Run the script without arguments, then enter data manually:
```bash
python run.py
```

### 🔹 Option 2: File input

If sensor data is stored in a file, specify it using `--file`:
#### 📁 Default File (`data.txt`)
```bash
python run.py --file
```
If no filename is provided, data.txt is used by default.
#### 📁 Custom File
```bash
python run.py --file myFile.txt
```

## 🔧 Code Structure

```bash
sensor-challenge/
├── README.md               # Documentation
├── requirements.txt        # Dependencies
├── run.py                  # Main execution script
├── data.txt                # Default data
├── sensor_processor/
│   ├── __init__.py         # Package initialization
│   ├── processor.py        # Sensor data processing logic
└── tests/                  # Test cases
```


