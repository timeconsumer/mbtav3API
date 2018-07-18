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


class TripResourceAttributes(object):
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
        'wheelchair_accessible': 'int',
        'name': 'str',
        'headsign': 'str',
        'direction_id': 'int',
        'block_id': 'str'
    }

    attribute_map = {
        'wheelchair_accessible': 'wheelchair_accessible',
        'name': 'name',
        'headsign': 'headsign',
        'direction_id': 'direction_id',
        'block_id': 'block_id'
    }

    def __init__(self, wheelchair_accessible=None, name=None, headsign=None, direction_id=None, block_id=None):  # noqa: E501
        """TripResourceAttributes - a model defined in Swagger"""  # noqa: E501

        self._wheelchair_accessible = None
        self._name = None
        self._headsign = None
        self._direction_id = None
        self._block_id = None
        self.discriminator = None

        if wheelchair_accessible is not None:
            self.wheelchair_accessible = wheelchair_accessible
        if name is not None:
            self.name = name
        if headsign is not None:
            self.headsign = headsign
        if direction_id is not None:
            self.direction_id = direction_id
        if block_id is not None:
            self.block_id = block_id

    @property
    def wheelchair_accessible(self):
        """Gets the wheelchair_accessible of this TripResourceAttributes.  # noqa: E501

        Indicator of wheelchair accessibility: `0`, `1`, `2`  Wheelchair accessibility (`*/attributes/wheelchair_accessible`) [as defined in GTFS](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#tripstxt):  | Value | Meaning                                            | |-------|----------------------------------------------------| | `0`   | No information                                     | | `1`   | Accessible (at stops allowing wheelchair_boarding) | | `2`   | Inaccessible                                       |    # noqa: E501

        :return: The wheelchair_accessible of this TripResourceAttributes.  # noqa: E501
        :rtype: int
        """
        return self._wheelchair_accessible

    @wheelchair_accessible.setter
    def wheelchair_accessible(self, wheelchair_accessible):
        """Sets the wheelchair_accessible of this TripResourceAttributes.

        Indicator of wheelchair accessibility: `0`, `1`, `2`  Wheelchair accessibility (`*/attributes/wheelchair_accessible`) [as defined in GTFS](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#tripstxt):  | Value | Meaning                                            | |-------|----------------------------------------------------| | `0`   | No information                                     | | `1`   | Accessible (at stops allowing wheelchair_boarding) | | `2`   | Inaccessible                                       |    # noqa: E501

        :param wheelchair_accessible: The wheelchair_accessible of this TripResourceAttributes.  # noqa: E501
        :type: int
        """

        self._wheelchair_accessible = wheelchair_accessible

    @property
    def name(self):
        """Gets the name of this TripResourceAttributes.  # noqa: E501

        The text that appears in schedules and sign boards to identify the trip to passengers, for example, to identify train numbers for commuter rail trips. See [GTFS `trips.txt` `trip_short_name`](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#tripstxt)   # noqa: E501

        :return: The name of this TripResourceAttributes.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TripResourceAttributes.

        The text that appears in schedules and sign boards to identify the trip to passengers, for example, to identify train numbers for commuter rail trips. See [GTFS `trips.txt` `trip_short_name`](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#tripstxt)   # noqa: E501

        :param name: The name of this TripResourceAttributes.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def headsign(self):
        """Gets the headsign of this TripResourceAttributes.  # noqa: E501

        The text that appears on a sign that identifies the trip's destination to passengers. See [GTFS `trips.txt` `trip_headsign`](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#tripstxt).   # noqa: E501

        :return: The headsign of this TripResourceAttributes.  # noqa: E501
        :rtype: str
        """
        return self._headsign

    @headsign.setter
    def headsign(self, headsign):
        """Sets the headsign of this TripResourceAttributes.

        The text that appears on a sign that identifies the trip's destination to passengers. See [GTFS `trips.txt` `trip_headsign`](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#tripstxt).   # noqa: E501

        :param headsign: The headsign of this TripResourceAttributes.  # noqa: E501
        :type: str
        """

        self._headsign = headsign

    @property
    def direction_id(self):
        """Gets the direction_id of this TripResourceAttributes.  # noqa: E501

        Direction in which trip is traveling: `0` or `1`.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.    # noqa: E501

        :return: The direction_id of this TripResourceAttributes.  # noqa: E501
        :rtype: int
        """
        return self._direction_id

    @direction_id.setter
    def direction_id(self, direction_id):
        """Sets the direction_id of this TripResourceAttributes.

        Direction in which trip is traveling: `0` or `1`.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.    # noqa: E501

        :param direction_id: The direction_id of this TripResourceAttributes.  # noqa: E501
        :type: int
        """

        self._direction_id = direction_id

    @property
    def block_id(self):
        """Gets the block_id of this TripResourceAttributes.  # noqa: E501

        ID used to group sequential trips with the same vehicle for a given service_id. See [GTFS `trips.txt` `block_id`](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#tripstxt)   # noqa: E501

        :return: The block_id of this TripResourceAttributes.  # noqa: E501
        :rtype: str
        """
        return self._block_id

    @block_id.setter
    def block_id(self, block_id):
        """Sets the block_id of this TripResourceAttributes.

        ID used to group sequential trips with the same vehicle for a given service_id. See [GTFS `trips.txt` `block_id`](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#tripstxt)   # noqa: E501

        :param block_id: The block_id of this TripResourceAttributes.  # noqa: E501
        :type: str
        """

        self._block_id = block_id

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
        if not isinstance(other, TripResourceAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
