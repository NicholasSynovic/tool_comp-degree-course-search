from typing import Any


class CourseListing:
    def __init__(
        self,
        name: str = "",
        source: str = "",
        number: int = 0,
        subject: str = "",
        extra: dict[str, Any] = {},
    ) -> None:
        self.name: str = name
        self.source: str = source
        self.number: int = number
        self.subject: str = subject
        self.extra: dict[str, Any] = extra

    def toJSON(self) -> dict[str, Any]:
        return {
            "source": self.source,
            "subject": self.subject,
            "number": self.number,
            "name": self.name,
            "fqn": f"{self.subject} {self.number} - {self.name}",
        }
