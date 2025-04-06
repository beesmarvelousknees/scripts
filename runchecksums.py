import hashlib
import os
import datetime

# Returns the SHA-256 hash of a file.
def calculate_sha256(file_path):
    hash_object = hashlib.sha256()
    # Read bytes for compatibility with images, etc.
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            # Update the hash object in chunks so large files
            # don't need to be in memory all at once.
            hash_object.update(chunk)
    # Convert from binary value to a hexidecimal output.
    return hash_object.hexdigest()

# Load existing checksums into a dictionary
def load_existing_checksums(checksum_path):
    existing_checksums = {}
    try:
        with open(checksum_path, 'r') as f:
            for line in f:
                filename, file_hash = line.strip().split(',')
                existing_checksums[filename] = file_hash
    except FileNotFoundError:
        pass  # It's ok if the file doesn't exist
    return existing_checksums

# Get script directory and checksums files.
directory = os.getcwd()
checksum_file_path = os.path.join(directory, '.checksums.txt')
checksum_diff_file_path = os.path.join(directory, '.checksums_diff.txt')

existing_checksums = load_existing_checksums(checksum_file_path)
checksum_diffs = []

num_new_checksums = 0
num_new_conflicting_checksums = 0

current_datetime = datetime.datetime.now()

with open(checksum_file_path, 'w') as checksum_file:
    # Loop through each file in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Skip the checksum file itself and directories
        if filename in ['.runchecksums.py', '.checksums.txt', '.checksums_diff.txt'] or os.path.isdir(file_path):
            continue
        
        # Calculate the SHA-256 hash of the file
        file_hash = calculate_sha256(file_path)

        # Check if the file's checksum has changed
        if filename in existing_checksums and existing_checksums[filename] != file_hash:
            checksum_diffs.append((filename, existing_checksums[filename], file_hash))
            num_new_checksums += 1
            num_new_conflicting_checksums += 1

        if not (filename in existing_checksums):
            num_new_checksums += 1  

        checksum_file.write(f"{filename},{file_hash}\n")

# Write differences to checksum_diff file
if checksum_diffs:
    with open(checksum_diff_file_path, 'a') as diff_file:
        for filename, old_hash, new_hash in checksum_diffs:
            datetime_str = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            diff_file.write(f"{filename},{old_hash},{new_hash},{datetime_str}\n")

print(f"Added {num_new_checksums} new checksums to {checksum_file_path}")
if checksum_diffs:
    print(f"DIFFERENCES FOUND! Added {num_new_conflicting_checksums} new conflicting checksum pairs to {checksum_diff_file_path}")
