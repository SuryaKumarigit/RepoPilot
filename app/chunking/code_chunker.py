from dataclasses import dataclass
import hashlib

@dataclass
class CodeChunk:
    """
    Represents one retrievable unit of source code.
    """

    chunk_id: str
    file_path: str
    language: str
    symbol_name: str
    symbol_type: str
    start_line: int
    end_line: int
    code: str

    def to_embedding_text(self) -> str:
        """
        Convert the code chunk into text suitable for embedding.
        """

        return f"""
File: {self.file_path}
Language: {self.language}
Symbol: {self.symbol_name}
Type: {self.symbol_type}
Lines: {self.start_line}-{self.end_line}

Code:
{self.code}
""".strip()
from pathlib import Path

from app.ingestion.parser import parse_python_file


def create_code_chunks(file_path: str) -> list[CodeChunk]:
    """
    Convert a Python source file into structure-aware code chunks.
    """

    parsed_data = parse_python_file(file_path)

    source_code = Path(file_path).read_text(encoding="utf-8")

    source_lines = source_code.splitlines()

    chunks = []

    for function in parsed_data["functions"]:

        start_line = function["start_line"]
        end_line = function["end_line"]

        code = "\n".join(
            source_lines[start_line - 1:end_line]
        )

        raw_id = (
            f"{file_path}:"
            f"{start_line}:"
            f"{end_line}"
        )

        chunk_id = hashlib.md5(
            raw_id.encode("utf-8")
        ).hexdigest()

        chunk = CodeChunk(
            chunk_id=chunk_id,
            file_path=file_path,
            language="python",
            symbol_name=function["name"],
            symbol_type=function["type"],
            start_line=start_line,
            end_line=end_line,
            code=code,
        )

        chunks.append(chunk)

    for class_info in parsed_data["classes"]:

        start_line = class_info["start_line"]
        end_line = class_info["end_line"]

        code = "\n".join(
            source_lines[start_line - 1:end_line]
        )

        raw_id = (
            f"{file_path}:"
            f"{start_line}:"
            f"{end_line}"
        )

        chunk_id = hashlib.md5(
            raw_id.encode("utf-8")
        ).hexdigest()

        chunk = CodeChunk(
            chunk_id=chunk_id,
            file_path=file_path,
            language="python",
            symbol_name=class_info["name"],
            symbol_type=class_info["type"],
            start_line=start_line,
            end_line=end_line,
            code=code,
        )

        chunks.append(chunk)

    return chunks