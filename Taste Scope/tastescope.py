import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import json
import os


class FoodClassifier:
    def __init__(self, model_path="best_food101_resnet50.pth", class_names_path="class_names.json", num_classes=101):
        self.model_path = model_path
        self.class_names_path = class_names_path
        self.num_classes = num_classes
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.transform = self._build_transform()
        self.model = self._load_model()
        self.class_names = self._load_class_names()

    def _build_transform(self):
        return transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225]),
        ])

    def _load_model(self):
        model = models.resnet50(pretrained=False)
        num_ftrs = model.fc.in_features
        model.fc = nn.Linear(num_ftrs, self.num_classes)
        model.load_state_dict(torch.load(self.model_path, map_location=self.device))
        model.to(self.device)
        model.eval()
        return model

    def _load_class_names(self):
        with open(self.class_names_path, "r") as f:
            return json.load(f)

    def predict(self, image_path):
        image = Image.open(image_path).convert("RGB")
        image_tensor = self.transform(image).unsqueeze(0).to(self.device)

        with torch.no_grad():
            outputs = self.model(image_tensor)
            _, predicted = torch.max(outputs, 1)
            return self.class_names[predicted.item()]

class FoodInfo:
    def __init__(self, info_json_path="food_info.json"):
        self.info_json_path = info_json_path
        self.data = self._load_json()
        self.current_class = None

    def _load_json(self):
        with open(self.info_json_path, 'r') as f:
            return json.load(f)

    def set(self, class_name):
        if class_name in self.data:
            self.current_class = class_name
        else:
            raise ValueError(f"'{class_name}' not found in the JSON data.")

    def get_description(self):
        return self._get_info("description")

    def get_calories(self):
        return self._get_info("calories_per_serving")

    def get_ingredients(self):
        return self._get_info("ingredients")

    def get_portion_size(self):
        return self._get_info("portion_size")

    def get_origin(self):
        return self._get_info("origin")

    def _get_info(self, key):
        if not self.current_class:
            raise RuntimeError("No class has been set. Use the set() method first.")
        return self.data[self.current_class].get(key, f"{key} not available")