import pandas as pd
from ..models.telemetry_event import TelemetryEvent
from ..models.session_data import SessionData


class CSVParser:
    """CSV dosyasını SessionData objesine dönüştürür."""

    def parse(self, file_path: str) -> SessionData:
        """CSV dosyasını okuyup SessionData döndürür."""
        df = pd.read_csv(file_path)
        session = SessionData()
        for _, row in df.iterrows():
            event = TelemetryEvent.from_dict(row.to_dict())
            session.add_event(event)
        return session

    def __repr__(self) -> str:
        return "CSVParser()"
