class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return (days + 6) // 7

    @classmethod
    def from_dict(cls, course_dict: dict) -> any:
        name = course_dict.get("name")
        description = course_dict.get("description")
        days = course_dict.get("days")
        weeks = cls.days_to_weeks(days)
        return cls(name, description, weeks)
