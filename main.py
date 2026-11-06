"""
Developermerv File Organizer v2
by @developermerv
İndirilenler klasörünü otomatik düzenleyen hafif otomasyon
"""

import os
import shutil
from pathlib import Path
from datetime import datetime

# developermerv config
DOWNLOADS = Path.home() / "Downloads"

FILE_MAP = {
    "Resimler": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Belgeler": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videolar": [".mp4", ".mov", ".avi", ".mkv"],
    "Kodlar": [".py", ".js", ".html", ".css", ".json"],
    "Kurulumlar": [".exe", ".msi", ".zip", ".rar", ".7z"]
}

def organize():
    print(f"🚀 developermerv organizer çalışıyor... {datetime.now().strftime('%H:%M')}")
    count = 0
    for file in DOWNLOADS.iterdir():
        if file.is_file():
            ext = file.suffix.lower()
            for folder, exts in FILE_MAP.items():
                if ext in exts:
                    target = DOWNLOADS / folder
                    target.mkdir(exist_ok=True)
                    try:
                        shutil.move(str(file), str(target / file.name))
                        print(f"  -> {file.name} -> {folder}/")
                        count += 1
                    except Exception as e:
                        print(f"  !! {file.name} taşınamadı: {e}")
                    break
    print(f"✅ Bitti! {count} dosya düzenlendi - by developermerv")

if __name__ == "__main__":
    organize()
