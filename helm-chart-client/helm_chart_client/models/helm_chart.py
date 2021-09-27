from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.helm_chart_values_file import HelmChartValuesFile
from ..types import UNSET, Unset

T = TypeVar("T", bound="HelmChart")


@attr.s(auto_attribs=True)
class HelmChart:
    """ """

    values_files: Union[Unset, HelmChartValuesFile] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        values_files: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.values_files, Unset):
            values_files = self.values_files.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if values_files is not UNSET:
            field_dict["values_files"] = values_files

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _values_files = d.pop("values_files", UNSET)
        values_files: Union[Unset, HelmChartValuesFile]
        if isinstance(_values_files, Unset):
            values_files = UNSET
        else:
            values_files = HelmChartValuesFile.from_dict(_values_files)

        helm_chart = cls(
            values_files=values_files,
        )

        helm_chart.additional_properties = d
        return helm_chart

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
