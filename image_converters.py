from PIL import Image
import pillow_avif

def convert_avig_to_png(img_path):
    img = Image.open('/Users/dorraz/Documents/autodidact/miniprojects/chat_service/party.avif')
    img.save('output.png')