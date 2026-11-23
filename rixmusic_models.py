from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional, Union
import time

@dataclass
class Track:
    title: str
    url: str
    requested_by: Optional[Union[str, int]] = None
    duration: Optional[float] = None
    file_path: Optional[Path] = None
    metadata: dict[str, Any] = field(default_factory=dict)
    added_at: float = field(default_factory=time.time)

    def __post_init__(self):
        self.title = str(self.title).strip() or "Unknown"
        self.url = str(self.url).strip()
        if not self.url:
            raise ValueError("Track.url cannot be empty")
        if self.file_path is not None:
            self.file_path = Path(self.file_path)

    @property
    def downloaded(self) -> bool:
        return bool(self.file_path and self.file_path.is_file())

@dataclass
class SearchResult:
    title: str
    url: str
    source: str = "unknown"
    duration: Optional[float] = None
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass
class PlaybackState:
    chat_id: str
    current: Optional[Track] = None
    paused: bool = False
    started_at: Optional[float] = None
