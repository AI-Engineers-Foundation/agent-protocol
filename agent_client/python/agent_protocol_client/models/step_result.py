# coding: utf-8

"""
    Agent Communication Protocol

    Specification of the API protocol for communication with an agent.  # noqa: E501

    The version of the OpenAPI document: v0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictBool, conlist
from agent_protocol_client.models.artifact import Artifact


class StepResult(BaseModel):
    """
    Result of the task step.
    """

    output: Optional[Any] = Field(
        None,
        description="Output that the task step has produced. Any value is allowed.",
    )
    artifacts: Optional[conlist(Artifact)] = Field(
        None, description="A list of artifacts that the step has produced."
    )
    is_last: Optional[StrictBool] = Field(
        False, description="Whether this is the last step in the task."
    )
    __properties = ["output", "artifacts", "is_last"]

    class Config:
        """Pydantic configuration"""

        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> StepResult:
        """Create an instance of StepResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in artifacts (list)
        _items = []
        if self.artifacts:
            for _item in self.artifacts:
                if _item:
                    _items.append(_item.to_dict())
            _dict["artifacts"] = _items
        # set to None if output (nullable) is None
        # and __fields_set__ contains the field
        if self.output is None and "output" in self.__fields_set__:
            _dict["output"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StepResult:
        """Create an instance of StepResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StepResult.parse_obj(obj)

        _obj = StepResult.parse_obj(
            {
                "output": obj.get("output"),
                "artifacts": [
                    Artifact.from_dict(_item) for _item in obj.get("artifacts")
                ]
                if obj.get("artifacts") is not None
                else None,
                "is_last": obj.get("is_last")
                if obj.get("is_last") is not None
                else False,
            }
        )
        return _obj
