from locust import HttpLocust, TaskSet, task, seq_task


class UserRunaBehavior(TaskSet):

    def __init__(self, parent):
        super().__init__(parent)
        self.token = None

    def on_start(self):
        response = self.client.post("/sessions", json={
            "password":"runahr",
            "email":"producto+automation@runahr.com",
            "subdomain":"automation",
            "ownerType":"company"
        }, headers={
            "Accept": "application/json",
            "content-type": "application/json;charset=UTF-8"
        })
        self.token = response.json()['access_token']
        assert 200 == response.status_code

    @seq_task(1)
    @task(2)
    def payrolls(self):
        response = self.client.get("/payrolls?status=finished&per_page=2", headers={
            "authorization": self.token,
            "content-type": "application/json"
        })
        assert 200 == response.status_code

    @seq_task(2)
    @task(3)
    def employees(self):
        response = self.client.get("/employees?per_page=2&column=family_name%2Cemployee_identifier&direction=asc%2Casc&status=active", headers={
            "authorization": self.token,
            "content-type": "application/json"
        })
        r = response.json()
        assert 200 == response.status_code
        assert 'Angela Acosta Ruiz' in r['results'][0]['name']
        assert len(r) == 2


class WebsiteUser(HttpLocust):
    task_set = UserRunaBehavior
    host = 'https://api-automation.runademos.info'
    min_wait = 5000
    max_wait = 9000