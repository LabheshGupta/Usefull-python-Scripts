import os
import shutil

IMAGE_EXTENSIONS = {
    '.png', '.jpg', '.jpeg', '.gif', '.bmp',
    '.webp', '.tiff', '.ico', '.svg'
}

def move_images_to_folder(root_dir):
    images_dir = os.path.join(root_dir, 'images')
    os.makedirs(images_dir, exist_ok=True)

    moved_count = 0
    for dirpath, _, filenames in os.walk(root_dir):
        # Skip the images folder itself to avoid recursion
        if os.path.abspath(dirpath) == os.path.abspath(images_dir):
            continue

        for file in filenames:
            _, ext = os.path.splitext(file)
            if ext.lower() in IMAGE_EXTENSIONS:
                src_path = os.path.join(dirpath, file)
                dest_path = os.path.join(images_dir, file)

                # Prevent overwriting if file already exist
                if os.path.exists(dest_path):
                    base, ext = os.path.splitext(file)
                    counter = 1
                    while os.path.exists(dest_path):
                        dest_path = os.path.join(images_dir, f"{base}_{counter}{ext}")
                        counter += 1

                shutil.move(src_path, dest_path)
                moved_count += 1
                print(f"Moved: {src_path} -> {dest_path}")

    print(f"\n✅ Done! Moved {moved_count} image(s) to '{images_dir}'.")


if __name__ == "__main__":
    current_dir = os.getcwd()
    move_images_to_folder(current_dir)

