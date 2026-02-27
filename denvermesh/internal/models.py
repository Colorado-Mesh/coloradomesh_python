from pydantic import BaseModel, model_validator, Field, field_validator, ValidationInfo


class _Base(BaseModel):
    pass
