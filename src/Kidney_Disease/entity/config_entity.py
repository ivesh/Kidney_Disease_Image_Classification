from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    """Configuration for data ingestion."""
    root_dir: Path
    data_source_url: str
    local_data_file: Path
    unzip_dir: Path

