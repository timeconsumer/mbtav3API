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

from swagger_client.models.alert_resource_attributes import AlertResourceAttributes  # noqa: F401,E501
from swagger_client.models.alert_resource_relationships import AlertResourceRelationships  # noqa: F401,E501


class AlertResource(object):
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
        'relationships': 'AlertResourceRelationships',
        'links': 'object',
        'id': 'str',
        'attributes': 'AlertResourceAttributes'
    }

    attribute_map = {
        'type': 'type',
        'relationships': 'relationships',
        'links': 'links',
        'id': 'id',
        'attributes': 'attributes'
    }

    def __init__(self, type=None, relationships=None, links=None, id=None, attributes=None):  # noqa: E501
        """AlertResource - a model defined in Swagger"""  # noqa: E501

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
        """Gets the type of this AlertResource.  # noqa: E501

        The JSON-API resource type  # noqa: E501

        :return: The type of this AlertResource.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AlertResource.

        The JSON-API resource type  # noqa: E501

        :param type: The type of this AlertResource.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def relationships(self):
        """Gets the relationships of this AlertResource.  # noqa: E501


        :return: The relationships of this AlertResource.  # noqa: E501
        :rtype: AlertResourceRelationships
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """Sets the relationships of this AlertResource.


        :param relationships: The relationships of this AlertResource.  # noqa: E501
        :type: AlertResourceRelationships
        """

        self._relationships = relationships

    @property
    def links(self):
        """Gets the links of this AlertResource.  # noqa: E501


        :return: The links of this AlertResource.  # noqa: E501
        :rtype: object
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AlertResource.


        :param links: The links of this AlertResource.  # noqa: E501
        :type: object
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this AlertResource.  # noqa: E501

        The JSON-API resource ID  # noqa: E501

        :return: The id of this AlertResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AlertResource.

        The JSON-API resource ID  # noqa: E501

        :param id: The id of this AlertResource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def attributes(self):
        """Gets the attributes of this AlertResource.  # noqa: E501


        :return: The attributes of this AlertResource.  # noqa: E501
        :rtype: AlertResourceAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this AlertResource.


        :param attributes: The attributes of this AlertResource.  # noqa: E501
        :type: AlertResourceAttributes
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
        if not isinstance(other, AlertResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
