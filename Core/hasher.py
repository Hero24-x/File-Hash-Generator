import hashlib

def calculate_hash(file_path, algorithm):
    hash_func = hashlib.new(algorithm)

    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            hash_func.update(chunk)

    return hash_func.hexdigest()


def generate_hashes(file_path):
    algorithms = ["md5", "sha1", "sha256"]
    results = {}

    for algo in algorithms:
        results[algo.upper()] = calculate_hash(file_path, algo)

    return results
