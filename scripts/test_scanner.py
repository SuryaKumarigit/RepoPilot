from app.ingestion.scanner import scan_repository


repository_path = "data"

files = scan_repository(repository_path)

print(f"\nFound {len(files)} source files:\n")

for file in files:
    print(file)