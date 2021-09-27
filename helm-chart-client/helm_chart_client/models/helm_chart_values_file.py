from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="HelmChartValuesFile")


@attr.s(auto_attribs=True)
class HelmChartValuesFile:
    """ """

    relative_path: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        relative_path = self.relative_path

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "relative_path": relative_path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        relative_path = d.pop("relative_path")

        helm_chart_values_file = cls(
            relative_path=relative_path,
        )

        helm_chart_values_file.additional_properties = d
        return helm_chart_values_file

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
