import os
import time
import shutil
from pathlib import Path


NUM_FILES = 500
FILE_SIZE_KB = 1
SOURCE_DIR = Path("./")
NAS_TARGET_DIR = Path("/mnt/storage")


def create_test_files():
    print("Creating test files...")
    SOURCE_DIR.mkdir(exist_ok=True)
    data = os.urandom(FILE_SIZE_KB * 1024)

    for i in range(NUM_FILES):
        with open(SOURCE_DIR / f"file_{i:04}.dat", "wb") as f:
            f.write(data)


def transfer_files():
    print(f"Transferring {NUM_FILES} files to NAS at: {NAS_TARGET_DIR}")
    if not NAS_TARGET_DIR.exists():
        print(f"Error: NAS target path {NAS_TARGET_DIR} does not exist.")
        return

    #fair warning, there's nothing here to prevent this process overwriting your existing files, be careful
    start_time = time.time()
    for file_path in SOURCE_DIR.iterdir():
        shutil.copy2(file_path, NAS_TARGET_DIR)
    end_time = time.time()

    elapsed = end_time - start_time
    print(f"\nTransfer complete.")
    print(f"Total time: {elapsed:.2f} seconds")
    print(f"Average per file: {elapsed / NUM_FILES:.4f} seconds")


def cleanup():
    print("Cleaning up local test files...")
    shutil.rmtree(SOURCE_DIR)


if __name__ == "__main__":
    create_test_files()
    transfer_files()
    # cleanup()  # Uncomment if you want to delete local test files after transfer
