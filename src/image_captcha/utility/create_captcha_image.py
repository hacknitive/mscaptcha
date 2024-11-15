from base64 import b64encode
from io import BytesIO

from captcha.image import ImageCaptcha


def create_captcha_image(code: str) -> str:
    image_captcha = ImageCaptcha()
    image = image_captcha.generate_image(code)
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_bytes = buffered.getvalue()
    img_base64 = b64encode(img_bytes).decode('utf-8')

    return img_base64