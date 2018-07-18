# coding: utf-8

"""
    MBTA

    MBTA service API. https://www.mbta.com  # noqa: E501

    OpenAPI spec version: 3.0
    Contact: developer@mbta.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.stop_resource_relationships_parent_station import StopResourceRelationshipsParentStation  # noqa: F401,E501


class StopResourceRelationships(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'parent_station': 'StopResourceRelationshipsParentStation'
    }

    attribute_map = {
        'parent_station': 'parent_station'
    }

    def __init__(self, parent_station=None):  # noqa: E501
        """StopResourceRelationships - a model defined in Swagger"""  # noqa: E501

        self._parent_station = None
        self.discriminator = None

        if parent_station is not None:
            self.parent_station = parent_station

    @property
    def parent_station(self):
        """Gets the parent_station of this StopResourceRelationships.  # noqa: E501


        :return: The parent_station of this StopResourceRelationships.  # noqa: E501
        :rtype: StopResourceRelationshipsParentStation
        """
        return self._parent_station

    @parent_station.setter
    def parent_station(self, parent_station):
        """Sets the parent_station of this StopResourceRelationships.


        :param parent_station: The parent_station of this StopResourceRelationships.  # noqa: E501
        :type: StopResourceRelationshipsParentStation
        """

        self._parent_station = parent_station

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StopResourceRelationships):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other