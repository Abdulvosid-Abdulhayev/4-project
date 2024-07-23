from PIL import Image, ImageFilter, ImageOps
import os

class ImageChanger:
    def __init__(self, filename):
        if not os.path.exists(filename):
            raise FileNotFoundError(f"No such file: '{filename}'")
        self.filename = filename
        self.image = Image.open(filename)

    def resize(self, output_filename, size):
        resized_image = self.image.resize(size)
        resized_image.save(output_filename)
        return resized_image

    def crop(self, output_filename, size):
        width, height = self.image.size
        left = (width - size[0]) / 2
        top = (height - size[1]) / 2
        right = (width + size[0]) / 2
        bottom = (height + size[1]) / 2
        cropped_image = self.image.crop((left, top, right, bottom))
        cropped_image.save(output_filename)
        return cropped_image

    def blur(self, output_filename, radius):
        blurred_image = self.image.filter(ImageFilter.GaussianBlur(radius))
        blurred_image.save(output_filename)
        return blurred_image

    def passport_formatter(self, output_filename):
        passport_size = (354, 472) 
        return self.crop(output_filename, passport_size)

    def black(self, output_filename):
        black_white_image = ImageOps.grayscale(self.image)
        black_white_image.save(output_filename)
        return black_white_image

    def merge(self, output_filename, second_filename):
        if not os.path.exists(second_filename):
            raise FileNotFoundError(f"No such file: '{second_filename}'")
        second_image = Image.open(second_filename)
        width1, height1 = self.image.size
        width2, height2 = second_image.size
        new_width = max(width1, width2)
        new_height = height1 + height2
        new_image = Image.new('RGB', (new_width, new_height))
        new_image.paste(self.image, (0, 0))
        new_image.paste(second_image, (0, height1))
        new_image.save(output_filename)
        return new_image

# Usage example:
changer = ImageChanger('gray_image.jpg')
# changer.resize('resized_rasm.jpg', (800, 600))
# changer.crop('cropped_rasm.jpg', (400, 300))
# changer.blur('blurred_rasm.jpg', 5)
# changer.passport_formatter('passport_rasm.jpg')
# changer.black('black_white_rasm.jpg')
# changer.merge('merged_rasm.jpg', 'another_rasm.jpg')
