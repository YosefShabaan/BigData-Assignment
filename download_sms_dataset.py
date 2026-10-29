"""Download the UCI SMS Spam Collection into data/dataset.csv.

Run from the bd-a1 project folder BEFORE building the Docker image:
    python download_sms_dataset.py

Source: https://archive.ics.uci.edu/dataset/228/sms+spam+collection
License: CC BY 4.0 (credit UCI and dataset creators).
"""

from pathlib import Path
import csv
import io
import urllib.request
import zipfile

URL = "https://archive.ics.uci.edu/static/public/228/sms%2Bspam%2Bcollection.zip"
DEST = Path(__file__).resolve().parent / "data" / "dataset.csv"


def main():
    print("Downloading UCI SMS Spam Collection...")
    req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as response:
        archive_bytes = response.read()

    with zipfile.ZipFile(io.BytesIO(archive_bytes)) as archive:
        raw = archive.read("SMSSpamCollection")

    try:
        content = raw.decode("utf-8")
    except UnicodeDecodeError:
        content = raw.decode("latin-1")

    records = []
    for line_num, line in enumerate(content.splitlines(), start=1):
        if not line.strip():
            continue
        if "\t" not in line:
            raise ValueError(f"Line {line_num} has no tab separator")
        label, text = line.split("\t", 1)
        if label not in ("ham", "spam"):
            raise ValueError(f"Unexpected label {label!r} on line {line_num}")
        records.append((label, text))

    DEST.parent.mkdir(parents=True, exist_ok=True)
    with DEST.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["label", "text"])
        writer.writerows(records)

    print(f"Saved {len(records):,} messages to: {DEST}")
    print(f"ham: {sum(label == 'ham' for label, _ in records):,}")
    print(f"spam: {sum(label == 'spam' for label, _ in records):,}")


if __name__ == "__main__":
    main()