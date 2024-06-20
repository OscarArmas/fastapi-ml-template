from abc import ABC, abstractmethod


class DataBase(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def fetch_single_db_record(self, unique_id: str):
        raise NotImplementedError()

