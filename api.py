import json

# Step 1: Load your original API JSON
with open("models_api.json", "r") as file:
    data = json.load(file)

models = data.get("models", [])

# Step 2: Define a helper function to prettify model names
def format_model_name(raw_name):
    name_parts = raw_name.replace("_", " ").split()
    # Capitalize words and fix YOLOx case
    formatted = " ".join([word.capitalize() for word in name_parts])
    if "Yolox" in formatted:
        formatted = formatted.replace("Yolox", "YOLOx")
    return formatted

# Step 3: Transform the models
transformed = []
for model in models:
    name = format_model_name(model["model_name"])
    model_url = model["url"]

    # Determine type automatically
    if "yolo" in model["model_name"].lower():
        model_type = "yolox"
        labels_url = "https://github.com/SyedFarhan110/Object-detection-/raw/refs/heads/main/app/src/main/assets/yoloLabels.txt"
    elif "ssd" in model["model_name"].lower():
        model_type = "ssd"
        labels_url = "https://raw.githubusercontent.com/SyedFarhan110/Object-detection-/refs/heads/main/app/src/main/assets/labels.txt"

    transformed.append({
        "name": name,
        "model_url": model_url,
        "labels_url": labels_url,
        "type": model_type
    })

# Step 4: Save or print transformed JSON
with open("transformed_models.json", "w") as outfile:
    json.dump(transformed, outfile, indent=2)

print(json.dumps(transformed, indent=2))
