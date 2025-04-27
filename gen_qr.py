#! python
"""Generate QR codes for sub-sites."""

import qrcode

mapping = {
    "static/career-at-nowan.dev.png": "mailto://career@nowan.dev",
    "static/career.nowan.dev.png": "https://career.nowan.dev",
}
for path, val in mapping.items():
    img = qrcode.make(val)
    img.save(path)
