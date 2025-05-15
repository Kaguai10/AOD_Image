<div align=center>
<img src="https://readme-typing-svg.herokuapp.com?size=30&color=1830ba&center=true&vCenter=true&width=600&lines=Art+Of+Data+Image+Format">
</div>

# 🖼 AOD - *Art Of Data* Image Format

**AOD** is an experimental image format based on a chunked file structure, designed to store image data in either raw or compressed form, with optional metadata support. It is inspired by PNG but simplified and modified for educational and forensic research purposes.

---

## 📦 AOD File Structure

| Offset | Size    | Field                | Description                                   |
|--------|---------|----------------------|-----------------------------------------------|
| 0      | 4 bytes | `AOD1`               | Magic number + format version                 |
| 4      | 4 bytes | `HDRC`               | Header chunk ID                               |
| 8      | 4 bytes | Width (big-endian)   | Image width                                   |
| 12     | 4 bytes | Height (big-endian)  | Image height                                  |
| 16     | 1 byte  | Color depth          | 3 = RGB, 4 = RGBA                              |
| 17     | 1 byte  | Compression flag     | 0 = None, 1 = zlib compression                 |
| 18     | n bytes | `META` chunks (opt)  | Optional metadata (author, description, etc.) |
| ??     | 4 bytes | `PXDT`               | Chunk ID for pixel data                       |
| ??     | 4 bytes | Data length          | Length of pixel data (compressed or raw)      |
| ??     | n bytes | Image data           | Actual image bytes                            |
| ??     | 4 bytes | `FOOT`               | Footer chunk ID                               |
| ??     | 4 bytes | CRC32                | CRC checksum of image data                    |

---

## 🛠 Encoder

The `encode_aod.py` script is used to convert a `.png` file into an `.aod` file.

### 🔧 Usage

```bash
python encode_aod.py
```

### ✅ Features:
- Optional zlib compression for pixel data
- Embeds metadata such as `Author`
- Supports RGB and RGBA images
- Automatically generates CRC32 checksum

---

## 🔎 Decoder

The `decode_aod.py` script is used to read and extract `.aod` files back into `.png`.

### 🔧 Usage

```bash
python decode_aod.py
```

### ✅ Features:
- Validates magic number and chunk structure
- Automatically decompresses pixel data if compressed
- Extracts embedded metadata
- Verifies CRC to detect corrupted files

---

## 📋 Supported Metadata Format

Metadata is stored in `META` chunks with a simple format:

| Type (2 bytes) | Length (2 bytes) | Value (n bytes) |
|----------------|------------------|------------------|
| `0x01`         | length            | Author           |
| `0x02`         | length            | Description      |
| …              | …                 | …                |

You can define your own tags as long as they follow the same structure.

---

## 💡 Why AOD?

AOD is more than just an image format — it’s an *educational and analytical format*. It was created to:
- Teach how chunk-based file formats work
- Be used in Capture The Flag (CTF) challenges for encoding or steganography
- Provide a lightweight and fully controlled alternative to PNG

---

## 🔐 Security Note

- Not intended for production use
- Does not support advanced features like transparency or animation
- Ideal for research, training, and security challenges
