"""
pillow - обработать изображение, например, изменить его размер, применить эффекты и сохранить в другой формат.
https://pillow.readthedocs.io/en/stable/

pip install pillow
"""

from PIL import Image, ImageDraw, ImageFont

def squize(name, scale=1):
    with Image.open(name) as _image:
        print(f"\nImage <{name}>: format {_image.format}; size: {_image.size}; mode: {_image.mode}")
        _image_width, _image_height = _image.size
        return _image.copy().resize({_image_width//scale, _image_height//scale})


n_image = squize('images/foto.jpg', 2)
im_2 = squize('images/starship.jpg')

n_image.paste(im_2, (00, 350))

draw = ImageDraw.Draw(n_image)
font = ImageFont.truetype('BAUHS93.TTF', 30)
draw.text((0, 0), 'Cosmo - 77', 'blue', font=font, spacing=5)


n_image.show('My foto')