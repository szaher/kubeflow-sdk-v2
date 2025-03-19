# coding: utf-8

"""
    Kubeflow Trainer OpenAPI Spec

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: unversioned
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from kubeflow.trainer.models.io_k8s_api_core_v1_local_object_reference import IoK8sApiCoreV1LocalObjectReference
from typing import Optional, Set
from typing_extensions import Self

class IoK8sApiCoreV1CinderVolumeSource(BaseModel):
    """
    Represents a cinder volume resource in Openstack. A Cinder volume must exist before mounting to a container. The volume must also be in the same region as the kubelet. Cinder volumes support ownership management and SELinux relabeling.
    """ # noqa: E501
    fs_type: Optional[StrictStr] = Field(default=None, description="fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified. More info: https://examples.k8s.io/mysql-cinder-pd/README.md", alias="fsType")
    read_only: Optional[StrictBool] = Field(default=None, description="readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/mysql-cinder-pd/README.md", alias="readOnly")
    secret_ref: Optional[IoK8sApiCoreV1LocalObjectReference] = Field(default=None, description="secretRef is optional: points to a secret object containing parameters used to connect to OpenStack.", alias="secretRef")
    volume_id: StrictStr = Field(description="volumeID used to identify the volume in cinder. More info: https://examples.k8s.io/mysql-cinder-pd/README.md", alias="volumeID")
    __properties: ClassVar[List[str]] = ["fsType", "readOnly", "secretRef", "volumeID"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of IoK8sApiCoreV1CinderVolumeSource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of secret_ref
        if self.secret_ref:
            _dict['secretRef'] = self.secret_ref.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoK8sApiCoreV1CinderVolumeSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fsType": obj.get("fsType"),
            "readOnly": obj.get("readOnly"),
            "secretRef": IoK8sApiCoreV1LocalObjectReference.from_dict(obj["secretRef"]) if obj.get("secretRef") is not None else None,
            "volumeID": obj.get("volumeID") if obj.get("volumeID") is not None else ''
        })
        return _obj


