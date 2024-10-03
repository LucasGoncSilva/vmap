"""
locust --headless -f loadtests/load_test.py -H http://localhost:8000 \
    --processes -1 --csv report/csv/load/load --html report/html/load.html
"""

from typing import Callable, Type

from locust import FastHttpUser, LoadTestShape, TaskSet, constant, stats, task
from utils import handle_stages


stats.PERCENTILES_TO_STATISTICS = [0.5, 0.75, 0.90, 0.95, 0.99]
stats.PERCENTILES_TO_CHART = [0.5, 0.75, 0.90, 0.95, 0.99]


class UserTasks(TaskSet):
    @task
    def get_root(self) -> None:
        self.client.get('/')


class WebsiteUser(FastHttpUser):
    wait_time: Callable = constant(0.5)
    tasks: list[Type[UserTasks]] = [UserTasks]


class LoadTest(LoadTestShape):
    stages: list[dict[str, str | int | float]] = [
        {'duration': '5m', 'users': 250, 'spawn_rate': 5 / 6},
        {'duration': '10m', 'users': 250, 'spawn_rate': 5 / 6},
        {'duration': '5m', 'users': 0, 'spawn_rate': 5 / 6},
    ]

    def tick(self) -> tuple | None:
        run_time: float = self.get_run_time()

        stages: list[dict[str, int | float]] = handle_stages(self.stages.copy())

        for stage in stages:
            if run_time < stage['duration']:
                tick_data: tuple[int | float, int | float] = (
                    stage['users'],
                    stage['spawn_rate'],
                )
                return tick_data

        return None
