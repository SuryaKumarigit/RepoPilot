import ast
from pathlib import Path


def parse_python_file(file_path: str) -> dict:
    """
    Parse a Python file and extract its structural information.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"File does not exist: {file_path}"
        )

    if path.suffix.lower() != ".py":
        raise ValueError(
            f"Only Python files are supported currently: {file_path}"
        )

    source_code = path.read_text(encoding="utf-8")

    tree = ast.parse(source_code)

    functions = []
    classes = []
    imports = []

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):
            functions.append(
                {
                    "name": node.name,
                    "type": "function",
                    "start_line": node.lineno,
                    "end_line": node.end_lineno,
                }
            )

        elif isinstance(node, ast.AsyncFunctionDef):
            functions.append(
                {
                    "name": node.name,
                    "type": "async_function",
                    "start_line": node.lineno,
                    "end_line": node.end_lineno,
                }
            )

        elif isinstance(node, ast.ClassDef):
            classes.append(
                {
                    "name": node.name,
                    "type": "class",
                    "start_line": node.lineno,
                    "end_line": node.end_lineno,
                }
            )

        elif isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)

        elif isinstance(node, ast.ImportFrom):
            module = node.module or ""

            for alias in node.names:
                imports.append(
                    f"{module}.{alias.name}"
                )

    return {
        "file_path": str(path),
        "functions": functions,
        "classes": classes,
        "imports": imports,
    }