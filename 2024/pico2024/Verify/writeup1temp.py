import zipfile
import hashlib

def calculate_checksum(file_path):
    """Calculate checksum (SHA256) for a file."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            hasher.update(chunk)
    return hasher.hexdigest()

def add_checksum_to_zip(zip_file_path):
    """Add checksum to files within a ZIP archive."""
    with zipfile.ZipFile(zip_file_path, 'a') as zip_file:
        for file_info in zip_file.infolist():
            with zip_file.open(file_info.filename) as file:
                checksum = calculate_checksum(file)
                file_info.filename = f"{file_info.filename}_{checksum[:32]}"  # Append checksum to filename

# Example usage
zip_file_path = 'challenge.zip'
add_checksum_to_zip(zip_file_path)
