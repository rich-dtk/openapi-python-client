from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.helm_value_assignment import HelmValueAssignment

T = TypeVar("T", bound="HelmChartInstantiation")


@attr.s(auto_attribs=True)
class HelmChartInstantiation:
    """ """

    values_file_relative_path: str
    override_values: List[HelmValueAssignment]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        values_file_relative_path = self.values_file_relative_path
        override_values = []
        for override_values_item_data in self.override_values:
            override_values_item = override_values_item_data.to_dict()

            override_values.append(override_values_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "values_file_relative_path": values_file_relative_path,
                "override_values": override_values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        values_file_relative_path = d.pop("values_file_relative_path")

        override_values = []
        _override_values = d.pop("override_values")
        for override_values_item_data in _override_values:
            override_values_item = HelmValueAssignment.from_dict(override_values_item_data)

            override_values.append(override_values_item)

        helm_chart_instantiation = cls(
            values_file_relative_path=values_file_relative_path,
            override_values=override_values,
        )

        helm_chart_instantiation.additional_properties = d
        return helm_chart_instantiation

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
