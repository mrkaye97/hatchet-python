# coding: utf-8

"""
    Hatchet API

    The Hatchet API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, Field, StrictStr
from typing_extensions import Annotated, Self

from hatchet_sdk.clients.rest.models.api_resource_meta import APIResourceMeta
from hatchet_sdk.clients.rest.models.workflow_run_status import WorkflowRunStatus
from hatchet_sdk.clients.rest.models.workflow_run_triggered_by import (
    WorkflowRunTriggeredBy,
)


class WorkflowRun(BaseModel):
    """
    WorkflowRun
    """  # noqa: E501

    metadata: APIResourceMeta
    tenant_id: StrictStr = Field(alias="tenantId")
    workflow_version_id: StrictStr = Field(alias="workflowVersionId")
    workflow_version: Optional[WorkflowVersion] = Field(
        default=None, alias="workflowVersion"
    )
    status: WorkflowRunStatus
    display_name: Optional[StrictStr] = Field(default=None, alias="displayName")
    job_runs: Optional[List[JobRun]] = Field(default=None, alias="jobRuns")
    triggered_by: WorkflowRunTriggeredBy = Field(alias="triggeredBy")
    input: Optional[Dict[str, Any]] = None
    error: Optional[StrictStr] = None
    started_at: Optional[datetime] = Field(default=None, alias="startedAt")
    finished_at: Optional[datetime] = Field(default=None, alias="finishedAt")
    parent_id: Optional[
        Annotated[str, Field(min_length=36, strict=True, max_length=36)]
    ] = Field(default=None, alias="parentId")
    parent_step_run_id: Optional[
        Annotated[str, Field(min_length=36, strict=True, max_length=36)]
    ] = Field(default=None, alias="parentStepRunId")
    __properties: ClassVar[List[str]] = [
        "metadata",
        "tenantId",
        "workflowVersionId",
        "workflowVersion",
        "status",
        "displayName",
        "jobRuns",
        "triggeredBy",
        "input",
        "error",
        "startedAt",
        "finishedAt",
        "parentId",
        "parentStepRunId",
    ]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of WorkflowRun from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict["metadata"] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of workflow_version
        if self.workflow_version:
            _dict["workflowVersion"] = self.workflow_version.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in job_runs (list)
        _items = []
        if self.job_runs:
            for _item in self.job_runs:
                if _item:
                    _items.append(_item.to_dict())
            _dict["jobRuns"] = _items
        # override the default output from pydantic by calling `to_dict()` of triggered_by
        if self.triggered_by:
            _dict["triggeredBy"] = self.triggered_by.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WorkflowRun from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "metadata": (
                    APIResourceMeta.from_dict(obj["metadata"])
                    if obj.get("metadata") is not None
                    else None
                ),
                "tenantId": obj.get("tenantId"),
                "workflowVersionId": obj.get("workflowVersionId"),
                "workflowVersion": (
                    WorkflowVersion.from_dict(obj["workflowVersion"])
                    if obj.get("workflowVersion") is not None
                    else None
                ),
                "status": obj.get("status"),
                "displayName": obj.get("displayName"),
                "jobRuns": (
                    [JobRun.from_dict(_item) for _item in obj["jobRuns"]]
                    if obj.get("jobRuns") is not None
                    else None
                ),
                "triggeredBy": (
                    WorkflowRunTriggeredBy.from_dict(obj["triggeredBy"])
                    if obj.get("triggeredBy") is not None
                    else None
                ),
                "input": obj.get("input"),
                "error": obj.get("error"),
                "startedAt": obj.get("startedAt"),
                "finishedAt": obj.get("finishedAt"),
                "parentId": obj.get("parentId"),
                "parentStepRunId": obj.get("parentStepRunId"),
            }
        )
        return _obj


from hatchet_sdk.clients.rest.models.job_run import JobRun
from hatchet_sdk.clients.rest.models.workflow_version import WorkflowVersion

# TODO: Rewrite to not use raise_errors
WorkflowRun.model_rebuild(raise_errors=False)
