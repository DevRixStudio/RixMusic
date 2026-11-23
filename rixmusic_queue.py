import asyncio
import random
from collections import deque
from typing import Iterable, Optional
from rixmusic_models import Track

class MusicQueue:
    """Async FIFO queue with skip, shuffle, remove and snapshot methods."""
    def __init__(self):
        self._items = deque()
        self.current: Optional[Track] = None
        self._lock = asyncio.Lock()

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(tuple(self._items))

    @property
    def items(self):
        return list(self._items)

    async def add(self, track: Track):
        if not isinstance(track, Track):
            raise TypeError("Only Track instances can be queued")
        async with self._lock:
            self._items.append(track)
        return track

    async def extend(self, tracks: Iterable[Track]):
        result = []
        for track in tracks:
            result.append(await self.add(track))
        return result

    async def next(self):
        async with self._lock:
            self.current = self._items.popleft() if self._items else None
            return self.current

    async def peek(self):
        async with self._lock:
            return self._items[0] if self._items else None

    async def remove(self, index: int):
        async with self._lock:
            values = list(self._items)
            if not 0 <= index < len(values):
                raise IndexError("Queue index out of range")
            item = values.pop(index)
            self._items = deque(values)
            return item

    async def clear(self):
        async with self._lock:
            self._items.clear()
            self.current = None

    async def shuffle(self):
        async with self._lock:
            values = list(self._items)
            random.shuffle(values)
            self._items = deque(values)
            return self.items
