import struct
import zlib
from PIL import Image

def encode_aod(input_path, output_path, author="Anonymous", compress=True):
    img = Image.open(input_path).convert("RGBA" if img_has_alpha(img := Image.open(input_path)) else "RGB")
    width, height = img.size
    mode = img.mode
    color_depth = 4 if mode == "RGBA" else 3

    raw_data = img.tobytes()
    compression_flag = 1 if compress else 0
    pixel_data = zlib.compress(raw_data) if compress else raw_data

    # Mulai menyusun file AOD
    with open(output_path, "wb") as f:
        # Magic
        f.write(b"AOD1")

        # Header
        f.write(b"HDRC")
        f.write(struct.pack(">I", width))
        f.write(struct.pack(">I", height))
        f.write(struct.pack("B", color_depth))
        f.write(struct.pack("B", compression_flag))

        # META chunk (optional metadata)
        meta_value = author.encode()
        f.write(b"META")
        f.write(struct.pack(">HH", 0x01, len(meta_value)))
        f.write(meta_value)

        # PXDT chunk (pixel data)
        f.write(b"PXDT")
        f.write(struct.pack(">I", len(pixel_data)))
        f.write(pixel_data)

        # FOOT chunk (footer + CRC32)
        f.write(b"FOOT")
        crc32 = zlib.crc32(pixel_data)
        f.write(struct.pack(">I", crc32))

    print(f"[+] AOD berhasil dibuat di: {output_path}")

def img_has_alpha(img):
    return img.mode in ("RGBA", "LA") or (img.mode == "P" and 'transparency' in img.info)

gambar = input("Nama File Gambar: ")
# Contoh penggunaan:
encode_aod(gambar, "output.aod", author="anonymous", compress=True)
