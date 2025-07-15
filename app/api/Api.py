import requests

from .entities.UserEntity import UserEntity
from .entities.Department import Department


class METHODS:
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"


class ENDPOINTS:
    USERS = "users"
    DEPARTMENTS = "departments"


class Api:
    def __init__(self, api_url: str, token: str):
        """
        Initialize the API client with the base URL and token.
        :param api_url: The base URL of the API.
        :param token: The API token for authentication. (not  implemented on server yet)
        """

        self.api_url = api_url
        self.token = token

    def get_user(self, user_id: str) -> UserEntity:
        """
        Fetch a user by ID from the API.
        :param user_id: The unique identifier of the user.
        :return: UserEntity object containing user details.
        """
        # Here you would implement the logic to make an HTTP request to the API
        # and return a UserEntity object. This is a placeholder implementation.

        return UserEntity(
            user_id=user_id,
            first_name="John",
            last_name="Doe",
            surname="Smith",
            telegram_id="123456789",
            created_at="2023-01-01T00:00:00Z",
            updated_at="2023-01-02T00:00:00Z",
        )

    def get_department(self, department_id: str) -> Department:
        """
        Fetch a department by ID from the API.
        :param department_id: The unique identifier of the department.
        :return: Department object containing department details.
        """

        resp = self._send_http_request(
            METHODS.GET, f"{ENDPOINTS.DEPARTMENTS}/{department_id}"
        )
        if resp:
            return Department(
                entity_id=resp.get("id"),
                name=resp.get("name"),
                description=resp.get("description"),
                created_at=resp.get("createdAt"),
                updated_at=resp.get("updatedAt"),
            )

        raise ValueError(f"Department with ID {department_id} not found")

    def get_all_departments(self) -> list[Department]:
        """
        Fetch all departments from the API.
        :return: List of Department objects.
        """
        resp = self._send_http_request(METHODS.GET, ENDPOINTS.DEPARTMENTS)
        if resp:
            return [
                Department(
                    entity_id=dept.get("id"),
                    name=dept.get("name"),
                    description=dept.get("description"),
                    created_at=dept.get("createdAt"),
                    updated_at=dept.get("updatedAt"),
                )
                for dept in resp
            ]

        return []

    def post_user(self, user: UserEntity) -> bool:
        """
        Post a new user to the API.
        :param user: UserEntity object containing user details to be posted.
        :return: True if the operation was successful, False otherwise.
        """
        # Here you would implement the logic to make an HTTP POST request to the API
        # with the user data. This is a placeholder implementation.

        return True

    def _send_http_request(self, method: str, endpoint: str, data: dict = None) -> dict:
        """
        Internal method to send HTTP requests to the API.
        :param method: HTTP method (GET, POST, etc.)
        :param endpoint: API endpoint to hit.
        :param data: Data to send in the request body (for POST requests).
        :return: Response from the API as a dictionary.
        """

        url = f"{self.api_url}/{endpoint}"
        headers = {
            "api_token": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

        try:
            response = requests.request(method, url, headers=headers, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            # Handle exceptions as needed
            # For now, we just return an empty dictionary
        return {}
