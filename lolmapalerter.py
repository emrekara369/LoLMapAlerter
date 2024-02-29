import mss
from PIL import Image

# İki noktanın koordinatlarını belirle
x1, y1 = 1652, 807  # Başlangıç noktası
x2, y2 = 1900, 1062  # Bitiş noktası

# Koordinatları sırala
left = min(x1, x2)
top = min(y1, y2)
width = abs(x2 - x1)
height = abs(y2 - y1)

while True:
    with mss.mss() as sct:
        region = {"left": left, "top": top, "width": width, "height": height}
        screenshot = sct.grab(region)
        
    image = Image.frombytes('RGB', screenshot.size, screenshot.rgb)