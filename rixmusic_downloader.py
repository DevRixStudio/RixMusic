import asyncio
import mimetypes
import re
import time
import urllib.request
from pathlib import Path
from urllib.parse import urlparse
from rixmusic_errors import DownloadError

class MusicDownloader:
    """Direct HTTP(S) downloader; does not scrape music platforms."""
    def __init__(self, directory="RixMusicDownloads", timeout=35,
                 max_bytes=150 * 1024 * 1024):
        self.directory = Path(directory)
        self.directory.mkdir(parents=True, exist_ok=True)
        self.timeout = timeout
        self.max_bytes = max_bytes

    def _download(self, url, filename=None):
        if urlparse(url).scheme not in ("http", "https"):
            raise DownloadError("Only direct HTTP/HTTPS media URLs are supported.")
        req = urllib.request.Request(url, headers={"User-Agent": "RixMusic/0.3.0"})
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as response:
                name = filename or Path(urlparse(response.geturl()).path).name or "audio"
                name = re.sub(r"[^\\w. -]", "_", name).strip(" .")[:100] or "audio"
                if not Path(name).suffix:
                    name += mimetypes.guess_extension(
                        response.headers.get_content_type()
                    ) or ".bin"
                target = self.directory / name
                if target.exists():
                    target = target.with_name(f"{target.stem}_{int(time.time())}{target.suffix}")
                total = 0
                with target.open("wb") as out:
                    while True:
                        chunk = response.read(65536)
                        if not chunk:
                            break
                        total += len(chunk)
                        if self.max_bytes and total > self.max_bytes:
                            raise DownloadError("Download exceeded max_bytes limit.")
                        out.write(chunk)
            return target
        except DownloadError:
            if 'target' in locals():
                target.unlink(missing_ok=True)
            raise
        except Exception as exc:
            raise DownloadError(f"Download failed: {exc}") from exc

    async def download(self, url, filename=None):
        return await asyncio.to_thread(self._download, url, filename)
