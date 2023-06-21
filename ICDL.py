import torch
import torchvision.transforms as transforms
from PIL import Image

# Load the pre-trained image classification model
model = torch.hub.load('pytorch/vision:v0.11.0', 'resnet18', pretrained=True)
model.eval()

def classify_image(image_path):
    # Load and preprocess the image
    image = Image.open(image_path).convert('RGB')
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    image = preprocess(image)
    image = image.unsqueeze(0)

    # Perform image classification
    with torch.no_grad():
        outputs = model(image)
        _, predicted_class = torch.max(outputs, 1)

    # Map predicted class to a pathology category
    pathology_category = "Example Pathology"

    return pathology_category

# User interface loop
while True:
    user_input = input("Enter image file path (or 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    pathology_category = classify_image(user_input)
    print("Pathology Category:", pathology_category)
    print()
