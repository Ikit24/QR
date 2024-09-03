# animated_qrcode.py

import segno
from urllib.request import urlopen

slts_qrcode = segno.make_qr("https://www.youtube.com/watch?v=kpnW68Q8ltc")
nirvana_url = urlopen("https://media.giphy.com/media/zB6tTWcZOSQyA/giphy.gif?cid=ecf05e479e4ihk9ym2sx1yv7ejdrs8jzysqhaz4pqnki9id9&ep=v1_gifs_related&rid=giphy.gif&ct=g")
slts_qrcode.to_artistic(
    background=nirvana_url,
    target="animated_qrcode.gif",
    scale=5,
)
