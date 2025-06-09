

from locust import HttpUser, task, between, LoadTestShape


class LoadTest(HttpUser):
    wait_time = between(1, 2)
    headers = {
        "Authorization": "pk_200410700_O80BZL6YIMK4KL5U5GUBP4AGWPVZ4HSQ",  # заміни на свій ClickUp токен
        "Content-Type": "application/json"
    }
    @task
    def get_authorized_user(self):
        self.client.get("/folder", headers=self.headers)


class CustomLoadShape(LoadTestShape):

    # Навантаження:
    # - 0-20 сек: 10 користувачів/сек
    # - 20-25 сек: 100 користувачів/сек (пік)
    # - 25-45 сек: 10 користувачів/сек

    def tick(self):
        run_time = self.get_run_time()

        if run_time < 20:
            return (10, 10)
        elif run_time < 25:
            return (100, 100)
        elif run_time < 45:
            return (10, 10)
        else:
            return None


