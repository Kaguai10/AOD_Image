cat ayyy.py 
import struct
import zlib
from PIL import Image

def decode_aod(input_path, output_path):
    with open(input_path, "rb") as f:
        data = f.read()

    # Pastikan magic number benar
    if data[:4] != b"AOD1":
        raise ValueError("File bukan AOD yang valid")

    offset = 4  # Lewati magic number

    # HDRC
    if data[offset:offset+4] != b"HDRC":
        raise ValueError("Header chunk (HDRC) tidak ditemukan")
    offset += 4

    width = struct.unpack(">I", data[offset:offset+4])[0]
    offset += 4
    height = struct.unpack(">I", data[offset:offset+4])[0]
    offset += 4
    color_depth = data[offset]
    offset += 1
    compression_flag = data[offset]
    offset += 1

    # META (opsional)
    if data[offset:offset+4] == b"META":
        offset += 4
        meta_type, meta_length = struct.unpack(">HH", data[offset:offset+4])
        offset += 4
        meta_value = data[offset:offset+meta_length]
        print(f"[i] Metadata ({hex(meta_type)}): {meta_value.decode(errors='ignore')}")
        offset += meta_length

    # PXDT (pixel data)
    if data[offset:offset+4] != b"PXDT":
        raise ValueError("Chunk PXDT tidak ditemukan")
    offset += 4
    pxdt_length = struct.unpack(">I", data[offset:offset+4])[0]
    offset += 4
    pixel_data = data[offset:offset+pxdt_length]
    offset += pxdt_length

    # FOOT + CRC (opsional untuk validasi CRC, bisa diabaikan)
    if data[offset:offset+4] == b"FOOT":
        offset += 4
        crc32 = struct.unpack(">I", data[offset:offset+4])[0]
        print(f"[i] CRC32 (deklarasi): {hex(crc32)}")

    # Dekompresi jika perlu
    if compression_flag == 1:
        raw_data = zlib.decompress(pixel_data)
    else:
        raw_data = pixel_data

    # Mode warna
    if color_depth == 3:
        mode = "RGB"
    elif color_depth == 4:
        mode = "RGBA"
    else:
        raise ValueError("Color depth tidak dikenal")

    # Buat gambar dan simpan
    img = Image.frombytes(mode, (width, height), raw_data)
    img.save(output_path)
    print(f"[+] Gambar berhasil disimpan di: {output_path}")

fileAod = input("masukan nama file AOD: ")
# Contoh penggunaan:
decode_aod("fileAod", "output.png")
