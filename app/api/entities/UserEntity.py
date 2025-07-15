from .Entity import Entity


class UserEntity(Entity):
    """
    Class representing a user entity in the application.
    UserEntity contains:
    - id: Unique identifier for the user
    - firstName: User's first name
    - lastName: User's last name
    - surname: User's surname
    - telegramId: Unique Telegram ID for the user
    - createdAt: Timestamp when the user was created
    - updatedAt: Timestamp when the user was last updated
    """

    def __init__(
        self,
        user_id: str,
        first_name: str,
        last_name: str,
        surname: str,
        telegram_id: str,
        created_at: str,
        updated_at: str,
    ):
        """
        Initialize the UserEntity with user details.
        :param user_id: Unique identifier for the user
        :param first_name: User's first name
        :param last_name: User's last name
        :param surname: User's surname
        :param telegram_id: Unique Telegram ID for the user
        :param created_at: Timestamp when the user was created
        :param updated_at: Timestamp when the user was last updated
        """
        super().__init__(entity_id=user_id)
        self.first_name = first_name
        self.last_name = last_name
        self.surname = surname
        self.telegram_id = telegram_id
        self.created_at = created_at
        self.updated_at = updated_at

    def to_json(self) -> dict:
        """Convert the UserEntity to a JSON-serializable dictionary."""
        return {
            "id": self.entity_id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "surname": self.surname,
            "telegramId": self.telegram_id,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
        }
