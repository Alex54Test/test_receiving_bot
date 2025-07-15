class Entity:
    """Base class for all entities in the application."""
    
    def __init__(self, entity_id: int):
        """
        Initialize the entity with an ID.
        :param entity_id: Unique identifier for the entity.
        """
        self.entity_id = entity_id

    def get_entity_id(self) -> int:
        """Return the unique identifier of the entity."""
        return self.entity_id

    def to_json(self) -> dict:
        """Convert the entity to a JSON-serializable dictionary."""
        return {
            'entity_id': self.entity_id
        }

    def __repr__(self):
        return f"Entity(entity_id={self.entity_id})"