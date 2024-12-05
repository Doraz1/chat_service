import base64
from PIL import Image
import io
import matplotlib.pyplot as plt

def encode_image_to_base64(image_path):
    """
    Read an image file and convert it to Base64 string
    
    Args:
        image_path (str): Path to the image file
        
    Returns:
        str: Base64 encoded string of the image
    """
    with open(image_path, "rb") as image_file:
        # Read the binary data
        binary_data = image_file.read()
        # Encode to base64
        base64_encoded = base64.b64encode(binary_data)
        # Convert bytes to string
        base64_string = base64_encoded.decode('utf-8')
        return base64_string

def decode_base64_to_image(base64_string):
    """
    Convert a Base64 string back to an image and display it
    
    Args:
        base64_string (str): Base64 encoded image data
        
    Returns:
        PIL.Image: Decoded image object
    """
    # Decode base64 string to bytes
    image_data = base64.b64decode(base64_string)
    # Create image object from bytes
    image = Image.open(io.BytesIO(image_data))
    return image

def display_image(image):
    """
    Display an image using matplotlib
    
    Args:
        image (PIL.Image): Image object to display
    """
    plt.figure(figsize=(10, 8))
    plt.imshow(image)
    plt.axis('off')
    plt.show()

# Example usage
if __name__ == "__main__":
    # Replace with your image path
    image_path = "example_image.jpg"
    
    try:
        # Encode image to Base64
        print("Encoding image to Base64...")
        base64_string = encode_image_to_base64(image_path)
        print("Base64 string (first 100 characters):")
        print(base64_string[:100])
        print("...")
        
        # Decode Base64 back to image
        print("\nDecoding Base64 back to image...")
        decoded_image = decode_base64_to_image(base64_string)
        
        # Display the decoded image
        print("Displaying decoded image...")
        display_image(decoded_image)
        
        # Optionally save the decoded image
        # decoded_image.save("decoded_image.jpg")
        
    except FileNotFoundError:
        print(f"Error: Could not find image file at {image_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")