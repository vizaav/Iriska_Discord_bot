import json
import typing
from datetime import datetime
from pathlib import Path

import aiofiles


class PointsManager:
    def __init__(self, store_path: Path = Path("points.json")):
        self.store_path = store_path
        self.points: typing.Dict[str, int] = {}
        self.last_sync: datetime | None = None

    async def sync(self):
        if self.last_sync is None:
            try:
                async with aiofiles.open(self.store_path, 'r') as f:
                    self.points = json.loads(await f.read())
            except FileNotFoundError:
                self.points = {}
                self.last_sync = datetime.now()
                await self.sync()
        else:
            if (datetime.now() - self.last_sync).total_seconds() < 10:
                return

            async with aiofiles.open(self.store_path, 'w') as f:
                await f.write(json.dumps(self.points))

        self.last_sync = datetime.now()

    async def update_points(self, user_id: str, points: int) -> int:
        user_points = self.get_points(user_id)
        user_points += points

        await self.set_points(user_id, user_points)

        return user_points

    def get_points(self, user_id: str) -> int:
        return self.points.get(user_id, 0)

    async def set_points(self, user_id: str, points: int) -> None:
        self.points |= {user_id: points}
        await self.sync()
