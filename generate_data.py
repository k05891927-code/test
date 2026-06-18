import json

# Generate numbers 1 to 10
data = {"numbers": list(range(1, 11))}

# Save to a JSON file
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

print("JSON file generated successfully!")