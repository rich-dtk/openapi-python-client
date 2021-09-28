from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.helm_chart_instantiation import HelmChartInstantiation
from ..models.helm_chart_values_file import HelmChartValuesFile
from ..types import UNSET, Unset

T = TypeVar("T", bound="HelmChart")


@attr.s(auto_attribs=True)
class HelmChart:
    """ """

    values_files: Union[Unset, List[HelmChartValuesFile]] = UNSET
    instantiations: Union[Unset, List[HelmChartInstantiation]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        values_files: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.values_files, Unset):
            values_files = []
            for values_files_item_data in self.values_files:
                values_files_item = values_files_item_data.to_dict()

                values_files.append(values_files_item)

        instantiations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.instantiations, Unset):
            instantiations = []
            for instantiations_item_data in self.instantiations:
                instantiations_item = instantiations_item_data.to_dict()

                instantiations.append(instantiations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if values_files is not UNSET:
            field_dict["values_files"] = values_files
        if instantiations is not UNSET:
            field_dict["instantiations"] = instantiations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        values_files = []
        _values_files = d.pop("values_files", UNSET)
        for values_files_item_data in _values_files or []:
            values_files_item = HelmChartValuesFile.from_dict(values_files_item_data)

            values_files.append(values_files_item)

        instantiations = []
        _instantiations = d.pop("instantiations", UNSET)
        for instantiations_item_data in _instantiations or []:
            instantiations_item = HelmChartInstantiation.from_dict(instantiations_item_data)

            instantiations.append(instantiations_item)

        helm_chart = cls(
            values_files=values_files,
            instantiations=instantiations,
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
