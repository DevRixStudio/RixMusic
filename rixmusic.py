"""RixMusic public API. All project files are flat in the project root."""
from rixmusic_core import RixMusic
from rixmusic_models import Track, SearchResult, PlaybackState
from rixmusic_queue import MusicQueue
from rixmusic_permissions import PermissionManager
from rixmusic_downloader import MusicDownloader
from rixmusic_rubpy import RubpyAdapter
from rixmusic_voice import VoiceChatManager
from rixmusic_media import MediaManager
from rixmusic_errors import (
    RixMusicError, ConfigurationError, UnsupportedFeature,
    DownloadError, PermissionDenied, VoiceChatUnavailable
)

__version__ = "0.3.0"
__all__ = [
    "RixMusic", "Track", "SearchResult", "PlaybackState", "MusicQueue",
    "PermissionManager", "MusicDownloader", "RubpyAdapter",
    "VoiceChatManager", "MediaManager", "RixMusicError",
    "ConfigurationError", "UnsupportedFeature", "DownloadError",
    "PermissionDenied", "VoiceChatUnavailable", "__version__",
]
