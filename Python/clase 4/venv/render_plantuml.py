import sys
import zlib
import urllib.request

ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_"

def encode6bit(b):
    return ALPHABET[b & 0x3f]

def append3bytes(b1, b2, b3):
    c1 = b1 >> 2
    c2 = ((b1 & 0x3) << 4) | (b2 >> 4)
    c3 = ((b2 & 0xF) << 2) | (b3 >> 6)
    c4 = b3 & 0x3F
    return encode6bit(c1) + encode6bit(c2) + encode6bit(c3) + encode6bit(c4)

def plantuml_encode(text):
    data = text.encode('utf-8')
    compressed = zlib.compress(data)
    # strip zlib header and checksum
    compressed = compressed[2:-4]
    res = ''
    i = 0
    while i < len(compressed):
        b1 = compressed[i]
        b2 = compressed[i+1] if i+1 < len(compressed) else 0
        b3 = compressed[i+2] if i+2 < len(compressed) else 0
        res += append3bytes(b1, b2, b3)
        i += 3
    return res


def main(puml_path, out_png):
    with open(puml_path, 'r', encoding='utf-8') as f:
        text = f.read()
    code = plantuml_encode(text)
    url = f"https://www.plantuml.com/plantuml/png/{code}"
    print('Requesting:', url)
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT)'
    })
    resp = urllib.request.urlopen(req)
    data = resp.read()
    with open(out_png, 'wb') as f:
        f.write(data)
    print('Saved PNG to', out_png)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: render_plantuml.py input.puml output.png')
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
