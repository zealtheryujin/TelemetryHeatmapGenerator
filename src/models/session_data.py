from typing import List, Tuple
from .telemetry_event import TelemetryEvent


class SessionData:
    """Bir oyun oturumundaki tüm telemetri olaylarını yönetir."""

    def __init__(self) -> None:
        self._events: List[TelemetryEvent] = []

    def add_event(self, event: TelemetryEvent) -> None:
        """Yeni bir olay ekler."""
        self._events.append(event)

    def get_events_by_type(self, event_type: str) -> List[TelemetryEvent]:
        """Belirli türdeki olayları filtreler."""
        return [e for e in self._events if e.event_type == event_type]

    def get_all_coordinates(self) -> List[Tuple[float, float]]:
        """Tüm (x, y) koordinatlarını döndürür."""
        return [(e.x, e.y) for e in self._events]

    def get_coordinates_by_type(self, event_type: str) -> List[Tuple[float, float]]:
        """Belirli türdeki olayların koordinatlarını döndürür."""
        return [(e.x, e.y) for e in self.get_events_by_type(event_type)]

    def __len__(self) -> int:
        return len(self._events)

    def __repr__(self) -> str:
        return f"SessionData(events={len(self._events)})"
