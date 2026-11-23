from rixmusic_queue import MusicQueue
from rixmusic_permissions import PermissionManager
from rixmusic_downloader import MusicDownloader
from rixmusic_rubpy import RubpyAdapter
from rixmusic_voice import VoiceChatManager
from rixmusic_media import MediaManager
from rixmusic_errors import ConfigurationError

class RixMusic:
    """Main facade for the RixMusic toolkit."""
    def __init__(self, client=None, owner_ids=None, download_dir="RixMusicDownloads"):
        self.client = client
        self.adapter = RubpyAdapter(client) if client is not None else None
        self.permissions = PermissionManager(owner_ids)
        self.downloader = MusicDownloader(download_dir)
        self.queues = {}
        self.voice = VoiceChatManager(self.adapter) if self.adapter else None
        self.media = MediaManager(self.adapter) if self.adapter else None

    def queue(self, chat_guid):
        key = str(chat_guid)
        if key not in self.queues:
            self.queues[key] = MusicQueue()
        return self.queues[key]

    async def add(self, chat_guid, track):
        return await self.queue(chat_guid).add(track)

    async def next(self, chat_guid):
        return await self.queue(chat_guid).next()

    async def skip(self, chat_guid):
        return await self.next(chat_guid)

    async def clear(self, chat_guid):
        await self.queue(chat_guid).clear()

    async def shuffle(self, chat_guid):
        return await self.queue(chat_guid).shuffle()

    async def download(self, url, filename=None):
        return await self.downloader.download(url, filename)

    def _require_client(self):
        if self.adapter is None:
            raise ConfigurationError("Pass an authenticated Rubpy Client to RixMusic.")

    async def send_music(self, chat_guid, path, caption=None):
        self._require_client()
        return await self.media.music(chat_guid, path, caption)

    async def send_video(self, chat_guid, path, caption=None):
        self._require_client()
        return await self.media.video(chat_guid, path, caption)

    async def create_voice_chat(self, group_guid):
        self._require_client()
        return await self.voice.create(group_guid)

    async def play_in_voice_chat(self, chat_guid, audio_path):
        self._require_client()
        return await self.voice.play(chat_guid, audio_path)

    async def stop_voice_chat_player(self, chat_guid):
        self._require_client()
        return await self.voice.stop(chat_guid)

    async def call_account(self, user_guid):
        self._require_client()
        return await self.adapter.account_voice_call(user_guid)

    async def video_call_account(self, user_guid):
        self._require_client()
        return await self.adapter.account_video_call(user_guid)
