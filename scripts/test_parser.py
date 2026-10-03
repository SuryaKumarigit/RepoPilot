from app.ingestion.parser import parse_python_file


file_path = "data/app/auth.py"

result = parse_python_file(file_path)

print("\nFILE:")
print(result["file_path"])

print("\nFUNCTIONS:")

for function in result["functions"]:
    print(
        f"  {function['name']} "
        f"({function['start_line']}-{function['end_line']})"
    )

print("\nCLASSES:")

for class_info in result["classes"]:
    print(
        f"  {class_info['name']} "
        f"({class_info['start_line']}-{class_info['end_line']})"
    )

print("\nIMPORTS:")

for imported in result["imports"]:
    print(f"  {imported}")