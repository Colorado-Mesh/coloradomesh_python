from typing import Optional, Any

from pydantic import field_validator, model_validator

from coloradomesh.emojis import EmojiTools
from coloradomesh.internal import BaseModel
from coloradomesh.meshcore.models.general.companion_type import CompanionType
from coloradomesh.meshcore.services.emojis import blacklisted_emojis
from coloradomesh.meshcore.standards import COMPANION_NAMING_SCHEMA_ROLE, COMPANION_NAMING_SCHEMA_COUNTER, \
    COMPANION_NAMING_SCHEMA_PKID


class CompanionName(BaseModel):
    """
    Contains elements of a MeshCore companion on the ColoradoMesh network.
    """
    handle: str  # The handle of the companion device owner (should not be a real name)
    emoji: Optional[str] = None
    role_type: Optional[CompanionType] = None
    role_counter: Optional[int] = None
    public_key_id: Optional[str] = None

    @field_validator('role_counter', mode='before')
    @classmethod
    def validate_role_counter(cls, value: Any) -> Any:
        if isinstance(value, str) and not value:  # Replace string with None if it's an empty string
            return None

        return value

    @model_validator(mode="after")
    def validate_model(self):
        # With (optional) 4-char emoji and <=4-char suffix, plus spaces, handle must be <=10 chars for 23 char limit
        if len(self.handle) > 10:
            raise ValueError("Handle must be up to 10 characters long")

        if self.emoji:
            emoji_tools = EmojiTools()
            if not emoji_tools.validate_emoji_unicode(self.emoji):
                raise ValueError("Emoji must be a valid Unicode emoji")
            if self.emoji in blacklisted_emojis():
                raise ValueError("Emoji is not allowed")

        if self.role_counter:
            if not 1 <= self.role_counter <= 99:
                raise ValueError("Role counter must be between 1 and 99")

        return self

    @property
    def formatted(self) -> str:
        """
        Get the formatted companion name based on the provided details.
        :return: A formatted companion name based on the provided details.
        :rtype: str
        """
        emoji = self.emoji or ""  # Use empty string if emoji is None

        # Order of preference: role_type -> role_counter -> public_key_id
        if self.role_type:
            return COMPANION_NAMING_SCHEMA_ROLE.format(
                emoji=emoji,
                handle=self.handle,
                role=CompanionType.to_acronym(node_type=self.role_type)
            )
        elif self.role_counter:
            return COMPANION_NAMING_SCHEMA_COUNTER.format(
                emoji=emoji,
                handle=self.handle,
                counter=str(self.role_counter).zfill(2)  # Pad the counter with zeros to ensure it's always 2 digits
            )
        else:
            return COMPANION_NAMING_SCHEMA_PKID.format(
                emoji=emoji,
                handle=self.handle,
                public_key_id=self.public_key_id.upper()
            )
