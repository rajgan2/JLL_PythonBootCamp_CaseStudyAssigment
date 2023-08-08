"""task.py"""
import dataclasses
import typing as t
from datetime import datetime


@dataclasses.dataclass
class Task:
    """Task"""

    idx: str
    title: str
    description: str
    is_done: bool = False
    due_date: t.Optional[datetime] = None
