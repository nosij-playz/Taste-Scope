# Example usage
from tastescope import FoodClassifier, FoodInfo

info = FoodInfo()
TEST_IMAGE_PATH = "Keema-Samosa-05.jpg"
classifier = FoodClassifier()
prediction = classifier.predict(TEST_IMAGE_PATH)
print(f"Predicted class: {prediction}")
info.set(prediction)

# Retrieve information
print("Description:", info.get_description())
print("Calories:", info.get_calories())
print("Ingredients:", info.get_ingredients())
print("Portion Size:", info.get_portion_size())
print("Origin:", info.get_origin())