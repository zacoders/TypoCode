

from datetime import datetime, timezone


class TimeProvider:

    def get_utc_time(self) -> datetime:
        return datetime.now(timezone.utc)
