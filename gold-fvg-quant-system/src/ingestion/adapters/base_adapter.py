from abc import ABC, abstractmethod
from typing import Dict, Any
import pandas as pd


class BaseAdapter(ABC):
    """
    Institutional-grade base adapter contract.

    Every market data adapter must inherit from this class.
    """

    def __init__(self, source_name: str):
        self.source_name = source_name
        self.connected = False

    @abstractmethod
    def connect(self) -> None:
        """
        Initialize API session / authentication.
        """
        pass

    @abstractmethod
    def fetch_historical_data(
        self,
        symbol: str,
        timeframe: str,
        start_date: str,
        end_date: str
    ) -> pd.DataFrame:
        """
        Fetch historical OHLCV data.
        """
        pass

    @abstractmethod
    def fetch_latest_data(
        self,
        symbol: str,
        timeframe: str
    ) -> Dict[str, Any]:
        """
        Fetch latest candle / tick data.
        """
        pass

    @abstractmethod
    def validate_response(
        self,
        data: Any
    ) -> bool:
        """
        Validate API response integrity.
        """
        pass

    @abstractmethod
    def normalize_data(
        self,
        data: Any
    ) -> pd.DataFrame:
        """
        Normalize raw provider data into
        institutional standard schema.
        """
        pass

    @abstractmethod
    def health_check(self) -> bool:
        """
        Check provider/API health.
        """
        pass

    @abstractmethod
    def close(self) -> None:
        """
        Cleanup sessions/resources.
        """
        pass
