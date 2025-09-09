from PIL import Image, ImageDraw
import os


def add_rounded_corners(image, radius=20):
    """
    Resme yuvarlak köşeler ekler

    :param image: PIL Image nesnesi
    :param radius: Köşe yuvarlaklık yarıçapı (piksel cinsinden)
    :return: Yuvarlak köşeli yeni resim
    """
    # Maske oluştur
    mask = Image.new('L', image.size, 0)
    draw = ImageDraw.Draw(mask)

    # Yuvarlak dikdörtgen çiz
    width, height = image.size
    draw.rounded_rectangle([(0, 0), (width, height)], radius, fill=255)

    # Orijinal resmi kopyala ve maskeyi uygula
    result = image.copy()
    result.putalpha(mask)

    return result


def process_images_with_rounded_corners(input_folder, output_folder, radius=20, canvas_size=(1200, 800)):
    """
    Bir klasördeki tüm resimlere yuvarlak köşe uygular

    :param input_folder: Giriş klasörü
    :param output_folder: Çıkış klasörü
    :param radius: Köşe yuvarlaklık yarıçapı
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    supported_formats = ('.png', '.jpg', '.jpeg', '.webp')

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(supported_formats):
            try:
                img_path = os.path.join(input_folder, filename)
                img = Image.open(img_path)

                # PNG formatında kaydetmek için RGBA'ya dönüştür
                if img.mode != 'RGBA':
                    img = img.convert('RGBA')

                # Yuvarlak köşe uygula
                rounded_img = add_rounded_corners(img, radius)

                canvas = Image.new('RGBA', canvas_size)

                img_width, img_height = rounded_img.size
                position = (
                    (canvas_size[0] - img_width) // 2,
                    (canvas_size[1] - img_height) // 2
                )
                canvas.paste(rounded_img, position)

                # Çıktı dosya adını ayarla
                name, ext = os.path.splitext(filename)
                output_path = os.path.join(output_folder, f"{name}.png")

                # PNG olarak kaydet (transparanlık için)
                canvas.save(output_path, 'PNG')
                print(f"{filename} başarıyla işlendi.")

            except Exception as e:
                print(f"{filename} işlenirken hata: {str(e)}")


# Kullanım örneği
input_folder = "images/154"
output_folder = "images/xxxhdpi"
corner_radius = 20  # Köşe yuvarlaklık yarıçapı (piksel)
canvas_size = (192, 192)

process_images_with_rounded_corners(input_folder, output_folder, corner_radius, canvas_size)