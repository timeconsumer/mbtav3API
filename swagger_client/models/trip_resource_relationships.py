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

from swagger_client.models.schedule_resource_relationships_route import ScheduleResourceRelationshipsRoute  # noqa: F401,E501
from swagger_client.models.trip_resource_relationships_service import TripResourceRelationshipsService  # noqa: F401,E501
from swagger_client.models.trip_resource_relationships_shape import TripResourceRelationshipsShape  # noqa: F401,E501


class TripResourceRelationships(object):
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
        'shape': 'TripResourceRelationshipsShape',
        'service': 'TripResourceRelationshipsService',
        'route': 'ScheduleResourceRelationshipsRoute'
    }

    attribute_map = {
        'shape': 'shape',
        'service': 'service',
        'route': 'route'
    }

    def __init__(self, shape=None, service=None, route=None):  # noqa: E501
        """TripResourceRelationships - a model defined in Swagger"""  # noqa: E501

        self._shape = None
        self._service = None
        self._route = None
        self.discriminator = None

        if shape is not None:
            self.shape = shape
        if service is not None:
            self.service = service
        if route is not None:
            self.route = route

    @property
    def shape(self):
        """Gets the shape of this TripResourceRelationships.  # noqa: E501


        :return: The shape of this TripResourceRelationships.  # noqa: E501
        :rtype: TripResourceRelationshipsShape
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """Sets the shape of this TripResourceRelationships.


        :param shape: The shape of this TripResourceRelationships.  # noqa: E501
        :type: TripResourceRelationshipsShape
        """

        self._shape = shape

    @property
    def service(self):
        """Gets the service of this TripResourceRelationships.  # noqa: E501


        :return: The service of this TripResourceRelationships.  # noqa: E501
        :rtype: TripResourceRelationshipsService
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this TripResourceRelationships.


        :param service: The service of this TripResourceRelationships.  # noqa: E501
        :type: TripResourceRelationshipsService
        """

        self._service = service

    @property
    def route(self):
        """Gets the route of this TripResourceRelationships.  # noqa: E501


        :return: The route of this TripResourceRelationships.  # noqa: E501
        :rtype: ScheduleResourceRelationshipsRoute
        """
        return self._route

    @route.setter
    def route(self, route):
        """Sets the route of this TripResourceRelationships.


        :param route: The route of this TripResourceRelationships.  # noqa: E501
        :type: ScheduleResourceRelationshipsRoute
        """

        self._route = route

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
        if not isinstance(other, TripResourceRelationships):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
