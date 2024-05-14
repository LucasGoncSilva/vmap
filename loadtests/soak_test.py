"""
locust --headless -f loadtests/soak_test.py -H http://localhost:8000 --processes -1 --csv report/csv/soak/soak --html report/html/soak.html
"""

from locust import FastHttpUser, LoadTestShape, TaskSet, constant, task, stats

from utils import handle_stages


stats.PERCENTILES_TO_STATISTICS = [0.5, 0.75, 0.80, 0.90, 0.95, 0.99]
stats.MODERN_UI_PERCENTILES_TO_CHART = [0.5, 0.75, 0.80, 0.90, 0.95, 0.99]


class UserTasks(TaskSet):
    @task
    def get_root(self) -> None:
        self.client.get('/')


class WebsiteUser(FastHttpUser):
    wait_time = constant(0.5)
    tasks = [UserTasks]


class SoakTest(LoadTestShape):
    stages = [
        {'duration': '2m', 'users': 250, 'spawn_rate': 25 / 12},
        {'duration': '5h40', 'users': 250, 'spawn_rate': 25 / 12},
        {'duration': '2m', 'users': 0, 'spawn_rate': 25 / 12},
    ]

    def tick(self) -> tuple | None:
        run_time = self.get_run_time()

        stages = handle_stages(self.stages.copy())

        for stage in stages:
            if run_time < stage['duration']:
                tick_data = (stage['users'], stage['spawn_rate'])
                return tick_data

        return None
