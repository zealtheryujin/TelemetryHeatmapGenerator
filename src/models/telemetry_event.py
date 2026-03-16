from dataclasses import dataclass
from typing import ClassVar


@dataclass
class TelemetryEvent:
    """Tek bir oyun olayını temsil eden DTO."""
    x: float
    y: float
    timestamp: float
    event_type: str

    VALID_TYPES: ClassVar[set] = {"Death", "Damage", "Kill"}

    @classmethod
    def from_dict(cls, data: dict) -> "TelemetryEvent":
        """Dictionary'den TelemetryEvent oluşturur."""
        return cls(
            x=float(data["x"]),
            y=float(data["y"]),
            timestamp=float(data["timestamp"]),
            event_type=str(data["event_type"]),
        )

    def __repr__(self) -> str:
        return (f"TelemetryEvent(type={self.event_type!r}, "
                f"x={self.x:.1f}, y={self.y:.1f}, t={self.timestamp:.1f})")
