import os
from pathlib import Path
import urllib.request
import zipfile


base_dir = Path("../datasets/coco")
images_dir = base_dir / "images"
labels_dir = base_dir / "labels"
train_txt = base_dir / "train2017.txt"
val_txt = base_dir / "val2017.txt"
test_txt = base_dir / "test-dev2017.txt"


def create_directories():
    print("Creating directories...")
    images_dir.mkdir(parents=True, exist_ok=True)
    labels_dir.mkdir(parents=True, exist_ok=True)
    print(f"Directories created: {images_dir}, {labels_dir}")


def download_and_extract(url, extract_to):
    print(f"Downloading from {url}...")
    zip_path, _ = urllib.request.urlretrieve(url)
    print(f"Extracting to {extract_to}...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Download and extraction complete.")


def download_coco_data():
    create_directories()

    download_and_extract('http://images.cocodataset.org/zips/train2017.zip', images_dir)
    download_and_extract('http://images.cocodataset.org/zips/val2017.zip', images_dir)
    download_and_extract('http://images.cocodataset.org/zips/test2017.zip', images_dir)

    download_and_extract('https://github.com/ultralytics/assets/releases/download/v0.0.0/coco2017labels.zip', labels_dir)


def create_image_path_txt(img_dir, txt_file):
    print(f"Creating {txt_file}...")
    with open(txt_file, 'w') as f:
        for img_path in sorted(img_dir.glob('*.jpg')):
            f.write(f"{img_path.relative_to(base_dir)}\n")
    print(f"{txt_file} created.")


if __name__ == "__main__":
    download_coco_data()

    create_image_path_txt(images_dir / "train2017", train_txt)
    create_image_path_txt(images_dir / "val2017", val_txt)
    create_image_path_txt(images_dir / "test2017", test_txt)

    print("COCO dataset is ready.")
