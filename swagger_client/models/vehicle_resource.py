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

from swagger_client.models.vehicle_resource_attributes import VehicleResourceAttributes  # noqa: F401,E501
from swagger_client.models.vehicle_resource_relationships import VehicleResourceRelationships  # noqa: F401,E501


class VehicleResource(object):
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
        'type': 'str',
        'relationships': 'VehicleResourceRelationships',
        'links': 'object',
        'id': 'str',
        'attributes': 'VehicleResourceAttributes'
    }

    attribute_map = {
        'type': 'type',
        'relationships': 'relationships',
        'links': 'links',
        'id': 'id',
        'attributes': 'attributes'
    }

    def __init__(self, type=None, relationships=None, links=None, id=None, attributes=None):  # noqa: E501
        """VehicleResource - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._relationships = None
        self._links = None
        self._id = None
        self._attributes = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if relationships is not None:
            self.relationships = relationships
        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if attributes is not None:
            self.attributes = attributes

    @property
    def type(self):
        """Gets the type of this VehicleResource.  # noqa: E501

        The JSON-API resource type  # noqa: E501

        :return: The type of this VehicleResource.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VehicleResource.

        The JSON-API resource type  # noqa: E501

        :param type: The type of this VehicleResource.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def relationships(self):
        """Gets the relationships of this VehicleResource.  # noqa: E501


        :return: The relationships of this VehicleResource.  # noqa: E501
        :rtype: VehicleResourceRelationships
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """Sets the relationships of this VehicleResource.


        :param relationships: The relationships of this VehicleResource.  # noqa: E501
        :type: VehicleResourceRelationships
        """

        self._relationships = relationships

    @property
    def links(self):
        """Gets the links of this VehicleResource.  # noqa: E501


        :return: The links of this VehicleResource.  # noqa: E501
        :rtype: object
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this VehicleResource.


        :param links: The links of this VehicleResource.  # noqa: E501
        :type: object
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this VehicleResource.  # noqa: E501

        The JSON-API resource ID  # noqa: E501

        :return: The id of this VehicleResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VehicleResource.

        The JSON-API resource ID  # noqa: E501

        :param id: The id of this VehicleResource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def attributes(self):
        """Gets the attributes of this VehicleResource.  # noqa: E501


        :return: The attributes of this VehicleResource.  # noqa: E501
        :rtype: VehicleResourceAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this VehicleResource.


        :param attributes: The attributes of this VehicleResource.  # noqa: E501
        :type: VehicleResourceAttributes
        """

        self._attributes = attributes

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
        if not isinstance(other, VehicleResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
