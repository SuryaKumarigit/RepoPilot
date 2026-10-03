from pathlib import Path


SUPPORTED_EXTENSIONS = {
    ".py",
    ".js",
    ".ts",
    ".jsx",
    ".tsx",
    ".java",
    ".cpp",
    ".c",
    ".cs",
    ".go",
}


IGNORED_DIRECTORIES = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    "node_modules",
    "dist",
    "build",
    ".pytest_cache",
}


def scan_repository(repository_path: str) -> list[Path]:
    """
    Find supported source files inside a repository.
    """

    root = Path(repository_path)

    if not root.exists():
        raise FileNotFoundError(
            f"Repository path does not exist: {repository_path}"
        )

    if not root.is_dir():
        raise NotADirectoryError(
            f"Expected a directory: {repository_path}"
        )

    source_files = []

    for path in root.rglob("*"):

        if not path.is_file():
            continue

        if any(
            ignored_dir in path.parts
            for ignored_dir in IGNORED_DIRECTORIES
        ):
            continue

        if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue

        source_files.append(path)

    return sorted(source_files)