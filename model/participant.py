from datetime import time
from operator import concat


class Participant():

    def __init__(
        self,
        ci: int,
        first_last_name: str,
        second_last_name: str,
        first_name: str,
        char_second_name: str,
        gender: str,
        age: int,
        hours: int,
        minutes: int,
        seconds: int,
    ):
        self.ci = ci
        self.first_last_name = first_last_name
        self.second_last_name = second_last_name
        self.first_name = first_name
        self.char_second_name = char_second_name
        self.gender = gender
        self.age = int(age)
        self.hours = int(hours)
        self.minutes = int(minutes)
        self.seconds = int(seconds)
        if self.age <= 25:
            self.etarian_group = "Juniors"
        elif 25 < self.age <= 40:
            self.etarian_group = "Seniors"
        else:
            self.etarian_group = "Masters"
        self.time = time(
            self.hours,
            self.minutes,
            self.seconds)
        self.total_time = self.seconds + (self.minutes * 60) + (self.hours * 3600)

    def __str__(self) -> str:
        return self.first_name + " " + self.first_last_name