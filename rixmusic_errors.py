class RixMusicError(Exception):
    """Base exception for RixMusic."""

class ConfigurationError(RixMusicError):
    pass

class UnsupportedFeature(RixMusicError):
    """Raised when the connected Rubika/Rubpy API has no confirmed support."""

class DownloadError(RixMusicError):
    pass

class PermissionDenied(RixMusicError):
    pass

class VoiceChatUnavailable(RixMusicError):
    pass
