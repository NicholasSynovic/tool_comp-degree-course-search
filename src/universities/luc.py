from requests import Response, post


class LUC_APIBuilder:
    def __init__(self) -> None:
        pass

    def build(self, subject: str) -> str:
        return f"https://catalog.luc.edu/course-search/api/?page=fose&route=search&subject={subject}"  # noqa: E501


class LUC_APIDirector:
    def __init__(self) -> None:
        self.builder: LUC_APIBuilder = LUC_APIBuilder()

    def query(self, subject: str) -> Response:
        url: str = self.builder.build(subject=subject)
        json: dict = {
            "other": {"srcdb": ""},
            "criteria": [
                {
                    "field": "subject",
                    "value": subject,
                }
            ],
        }
        return post(url=url, json=json, timeout=60)


class LUC:
    def __init__(self) -> None:
        self.director: LUC_APIDirector = LUC_APIDirector()

    def searchForCourses(self, subject: str) -> dict:
        resp: Response = self.director.query(subject=subject)

        if resp.status_code != 200:
            raise ValueError(
                f"`{subject}` returned a non 200 status code: {resp.status_code}"  # noqa: E501
            )

        return resp.json()
