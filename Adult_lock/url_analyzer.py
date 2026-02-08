import re
import validators
from urllib.parse import urlparse

SHORTENERS = ["bit.ly", "tinyurl", "t.co", "goo.gl"]

def analyze_urls(text):
    risk = 0
    reasons = []

    try:
        urls = re.findall(r'(https?://\S+)', text)

    except Exception as e:
        print(f"Invalid or Unknown content")

    for url in urls:
        parsed = urlparse(url)

        # Shortened URL
        if any(short in parsed.netloc for short in SHORTENERS):
            risk += 40
            reasons.append("Uses a shortened URL (+40)")

        # IP-based URL
        if re.match(r"\d+\.\d+\.\d+\.\d+", parsed.netloc):
            risk += 40
            reasons.append("Uses IP-based URL (+40)")

        # Too many parameters
        if parsed.query.count("&") >= 2:
            risk += 20
            reasons.append("URL has excessive parameters (+20)")

        # Invalid domain
        if not validators.domain(parsed.netloc):
            risk += 20
            reasons.append("Suspicious or invalid domain (+20)")

    return risk, reasons
