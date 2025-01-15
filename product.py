from PIL import Image, ImageDraw, ImageFont
import os

# Ensure the fonts directory exists and contains appropriate fonts
FONTS_DIR = "fonts"
IMAGES_DIR = "images"
OUTPUT_DIR = "output"

# Function to load fonts
def load_font(font_name, size):
    font_path = os.path.join(FONTS_DIR, font_name)
    if os.path.exists(font_path):
        return ImageFont.truetype(font_path, size)
    else:
        raise FileNotFoundError(f"Font {font_name} not found in {FONTS_DIR}")

# Function to create a graphic
def create_graphic(base_image, output_name, title, subtitle, author, font_title, font_subtitle, font_author):
    try:
        # Open base image
        image_path = os.path.join(IMAGES_DIR, base_image)
        with Image.open(image_path) as img:
            draw = ImageDraw.Draw(img)
            
            # Define text positions
            width, height = img.size
            title_position = (50, height // 5)
            subtitle_position = (50, height // 3)
            author_position = (50, height - 100)

            # Add text to the image
            draw.text(title_position, title, font=font_title, fill="white")
            draw.text(subtitle_position, subtitle, font=font_subtitle, fill="lightgray")
            draw.text(author_position, f"By {author}", font=font_author, fill="gray")

            # Save the output image
            if not os.path.exists(OUTPUT_DIR):
                os.makedirs(OUTPUT_DIR)

            output_path = os.path.join(OUTPUT_DIR, output_name)
            img.save(output_path)
            print(f"Graphic saved at {output_path}")
    except Exception as e:
        print(f"Error creating graphic: {e}")

# Function to display available images
def list_images():
    if os.path.exists(IMAGES_DIR):
        images = [img for img in os.listdir(IMAGES_DIR) if img.endswith(('.png', '.jpg', '.jpeg'))]
        return images
    else:
        raise FileNotFoundError(f"Images directory '{IMAGES_DIR}' not found")

# Function to display available fonts
def list_fonts():
    if os.path.exists(FONTS_DIR):
        fonts = [font for font in os.listdir(FONTS_DIR) if font.endswith('.ttf')]
        return fonts
    else:
        raise FileNotFoundError(f"Fonts directory '{FONTS_DIR}' not found")

# Main function
def main():
    print("Welcome to the Blog Graphics Generator!")

    # Display available images
    try:
        images = list_images()
        print("Available images:")
        for i, image in enumerate(images):
            print(f"{i + 1}. {image}")
    except FileNotFoundError as e:
        print(e)
        return

    # Select an image
    image_choice = int(input("Select an image by number: ")) - 1
    if 0 <= image_choice < len(images):
        base_image = images[image_choice]
    else:
        print("Invalid choice. Exiting.")
        return

    # Get user input for text
    title = input("Enter the title text: ")
    subtitle = input("Enter the subtitle text: ")
    author = input("Enter the author name: ")

    # Display available fonts
    try:
        fonts = list_fonts()
        print("Available fonts:")
        for i, font in enumerate(fonts):
            print(f"{i + 1}. {font}")
    except FileNotFoundError as e:
        print(e)
        return

    # Select fonts for title, subtitle, and author
    try:
        font_title = load_font(fonts[int(input("Select a font for the title by number: ")) - 1], 50)
        font_subtitle = load_font(fonts[int(input("Select a font for the subtitle by number: ")) - 1], 30)
        font_author = load_font(fonts[int(input("Select a font for the author by number: ")) - 1], 20)
    except (IndexError, ValueError, FileNotFoundError):
        print("Invalid font selection. Exiting.")
        return

    # Generate output name
    output_name = input("Enter the output file name (with extension, e.g., graphic.png): ")

    # Create the graphic
    create_graphic(base_image, output_name, title, subtitle, author, font_title, font_subtitle, font_author)

if __name__ == "__main__":
    main()
