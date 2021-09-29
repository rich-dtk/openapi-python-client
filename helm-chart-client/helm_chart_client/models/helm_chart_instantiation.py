from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.helm_chart_instantiation_override_values import HelmChartInstantiationOverrideValues

T = TypeVar("T", bound="HelmChartInstantiation")


@attr.s(auto_attribs=True)
class HelmChartInstantiation:
    """ """

    values_file_relative_path: str
    override_values: HelmChartInstantiationOverrideValues
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        values_file_relative_path = self.values_file_relative_path
        override_values = self.override_values.to_dict()

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

        override_values = HelmChartInstantiationOverrideValues.from_dict(d.pop("override_values"))

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
