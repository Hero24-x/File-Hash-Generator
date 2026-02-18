from core.hasher import generate_hashes
from utils.file_handler import validate_file
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <file_path>")
        return

    file_path = sys.argv[1]

    if not validate_file(file_path):
        print("Invalid file path!")
        return

    hashes = generate_hashes(file_path)

    print("\nHash Results:\n")
    for name, value in hashes.items():
        print(f"{name}: {value}")

if __name__ == "__main__":
    main()
