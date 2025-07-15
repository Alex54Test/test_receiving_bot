from .Entity import Entity


class Department(Entity):
    """
    Class representing a department entity in the application.
    Department contains:
    - id: Unique identifier for the department
    - name: Name of the department
    - description: Optional description of the department
    - createdAt: Timestamp when the department was created
    - updatedAt: Timestamp when the department was last updated
    """

    def __init__(
        self,
        entity_id: str,
        name: str,
        description: str,
        created_at: str,
        updated_at: str,
    ):
        super().__init__(entity_id=entity_id)
        self.name = name
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at

    def to_json(self) -> dict:
        """Convert the Department to a JSON-serializable dictionary."""
        return {
            "id": self.entity_id,
            "name": self.name,
            "description": self.description,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
        }
