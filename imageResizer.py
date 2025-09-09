from PIL import Image
import os


def resize_images_in_folder(input_folder, output_folder, new_size=(800, 600)):
    """
    Bir klasördeki tüm resimleri belirtilen boyuta dönüştürür.

    :param input_folder: İşlenecek resimlerin bulunduğu klasör yolu
    :param output_folder: Dönüştürülmüş resimlerin kaydedileceği klasör yolu
    :param new_size: Yeni boyut (genişlik, yükseklik). Varsayılan: (800, 600)
    """

    # Eğer çıktı klasörü yoksa oluştur
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Klasördeki tüm dosyaları listele
    for filename in os.listdir(input_folder):
        # Sadece resim dosyalarını işle
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            try:
                # Resmi aç
                img_path = os.path.join(input_folder, filename)
                img = Image.open(img_path)

                # Boyutlandır
                img_resized = img.resize(new_size, Image.LANCZOS)

                # Yeni dosya yolunu oluştur ve kaydet
                output_path = os.path.join(output_folder, filename)
                img_resized.save(output_path)

                print(f"{filename} başarıyla boyutlandırıldı ve kaydedildi.")

            except Exception as e:
                print(f"{filename} işlenirken hata oluştu: {str(e)}")


# Kullanım örneği



input_folder = "images/xxxhdpi"  # Orijinal resimlerin bulunduğu klasör

#resize_images_in_folder("images/512", "images/154", (154, 154))

# resize_images_in_folder(input_folder, "images/xxhdpi", (144, 144))
# resize_images_in_folder(input_folder, "images/xhdpi", (96, 96))
# resize_images_in_folder(input_folder, "images/hdpi", (72, 72))
# resize_images_in_folder(input_folder, "images/mdpi", (48, 48))