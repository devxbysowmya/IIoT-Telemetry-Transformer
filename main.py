import json
from datetime import datetime

# Helper function to convert ISO timestamp to Unix milliseconds
def iso_to_unix_ms(iso_str):
    dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
    return int(dt.timestamp() * 1000)

# Transform data from data-1.json format to unified format
def transform_data1(data):
    return {
        "device_id": data["id"],
        "temperature_c": data["temp"],
        "pressure_psi": data["pressure"],
        "timestamp": iso_to_unix_ms(data["time"])
    }

# Transform data from data-2.json format to unified format
def transform_data2(data):
    return {
        "device_id": data["device"],
        "temperature_c": data["metrics"]["temperature"],
        "pressure_psi": data["metrics"]["pressure"],
        "timestamp": data["timestamp"]  # already in Unix ms
    }

if __name__ == "__main__":
    # Load data from data-1.json
    with open("data-1.json", "r") as f1:
        data1 = json.load(f1)

    # Load data from data-2.json
    with open("data-2.json", "r") as f2:
        data2 = json.load(f2)

    # Transform the data
    result1 = transform_data1(data1)
    result2 = transform_data2(data2)

    # Print the transformed results (you can adjust this to your needs)
    print("Transformed data-1.json:")
    print(json.dumps(result1, indent=2))

    print("\nTransformed data-2.json:")
    print(json.dumps(result2, indent=2))
