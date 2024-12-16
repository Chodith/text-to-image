from PIL import Image, ImageDraw, ImageFont

def text_to_image(text, font_size=50, text_color="black", bg_color="white", image_size=(500, 300), font_path=None):
    # Create a new blank image with the given background color
    img = Image.new("RGB", image_size, color=bg_color)
    
    # Initialize ImageDraw object
    draw = ImageDraw.Draw(img)
    
    # Load font, either default or custom if provided
    if font_path:
        try:
            font = ImageFont.truetype(font_path, font_size)
        except IOError:
            print(f"Error: Font file not found at {font_path}. Using default font.")
            font = ImageFont.load_default()
    else:
        font = ImageFont.load_default()
    
    # Get the size of the text so we can center it
    text_width, text_height = draw.textsize(text, font=font)
    
    # Calculate position to center the text on the image
    position = ((image_size[0] - text_width) // 2, (image_size[1] - text_height) // 2)
    
    # Draw the text on the image
    draw.text(position, text, font=font, fill=text_color)
    
    # Save the image to a file
    img.save("text_image.png")
    
    # Display the image
    img.show()