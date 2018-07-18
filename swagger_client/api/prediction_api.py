# coding: utf-8

"""
    MBTA

    MBTA service API. https://www.mbta.com  # noqa: E501

    OpenAPI spec version: 3.0
    Contact: developer@mbta.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class PredictionApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_web_prediction_controller_index(self, **kwargs):  # noqa: E501
        """  # noqa: E501

        **NOTE:** A filter **MUST** be present for any predictions to be returned.  List of predictions for trips.  To get the scheduled times instead of the predictions, use `/schedules`.  The predicted arrival time (`//data/{index}/attributes/arrival_time`) and departure time (`/data/{index}/attributes/departure_time`) to/from a stop (`/data/{index}/relationships/stop/data/id`) at a given sequence (`/data/{index}/attriutes/stop_sequence`) along a trip (`/data/{index}/relationships/trip/data/id`) going a direction (`/data/{index}/attributes/direction_id`) along a route (`/data/{index}/relationships/route/data/id`).  See [GTFS Realtime `FeedMesage` `FeedEntity` `TripUpdate` `TripDescriptor`](https://github.com/google/transit/blob/master/gtfs-realtime/spec/en/reference.md#message-tripdescriptor) See [GTFS Realtime `FeedMesage` `FeedEntity` `TripUpdate` `StopTimeUpdate`](https://github.com/google/transit/blob/master/gtfs-realtime/spec/en/reference.md#message-stoptimeupdate)   ## When a vehicle is predicted to be at a stop  `/predictions?filter[stop]=STOP_ID`  ## The predicted schedule for one route  `/predictions?filter[route]=ROUTE_ID`  ## The predicted schedule for a whole trip  `/predictions?filter[trip]=TRIP_ID`    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_web_prediction_controller_index(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page_offset: Offset (0-based) of first element in the page
        :param int page_limit: Max number of elements to return
        :param str sort: Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any `/data/{index}/attributes` key. Assumes ascending; may be prefixed with '-' for descending  | JSON pointer | Direction | `sort`     | |--------------|-----------|------------| | `/data/{index}/attributes/arrival_time` | ascending | `arrival_time` | | `/data/{index}/attributes/arrival_time` | descending | `-arrival_time` | | `/data/{index}/attributes/departure_time` | ascending | `departure_time` | | `/data/{index}/attributes/departure_time` | descending | `-departure_time` | | `/data/{index}/attributes/direction_id` | ascending | `direction_id` | | `/data/{index}/attributes/direction_id` | descending | `-direction_id` | | `/data/{index}/attributes/schedule_relationship` | ascending | `schedule_relationship` | | `/data/{index}/attributes/schedule_relationship` | descending | `-schedule_relationship` | | `/data/{index}/attributes/status` | ascending | `status` | | `/data/{index}/attributes/status` | descending | `-status` | | `/data/{index}/attributes/stop_sequence` | ascending | `stop_sequence` | | `/data/{index}/attributes/stop_sequence` | descending | `-stop_sequence` | | `/data/{index}/attributes/track` | ascending | `track` | | `/data/{index}/attributes/track` | descending | `-track` |  
        :param str include: Relationships to include.  * `schedule` * `stop` * `route` * `trip` * `vehicle` * `alerts`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)   
        :param str filter_latitude:  Latitude/Longitude must be both present or both absent.
        :param str filter_longitude:  Latitude/Longitude must be both present or both absent.
        :param str filter_direction_id: Filter by direction of travel along the route.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.    
        :param str filter_stop: Filter by `/data/{index}/relationships/stop/data/id`. Multiple `/data/{index}/relationships/stop/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list.
        :param str filter_route: Filter by `/data/{index}/relationships/route/data/id`. Multiple `/data/{index}/relationships/route/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list.
        :param str filter_trip: Filter by `/data/{index}/relationships/trip/data/id`. Multiple `/data/{index}/relationships/trip/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list.
        :return: Predictions
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.api_web_prediction_controller_index_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_web_prediction_controller_index_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_web_prediction_controller_index_with_http_info(self, **kwargs):  # noqa: E501
        """  # noqa: E501

        **NOTE:** A filter **MUST** be present for any predictions to be returned.  List of predictions for trips.  To get the scheduled times instead of the predictions, use `/schedules`.  The predicted arrival time (`//data/{index}/attributes/arrival_time`) and departure time (`/data/{index}/attributes/departure_time`) to/from a stop (`/data/{index}/relationships/stop/data/id`) at a given sequence (`/data/{index}/attriutes/stop_sequence`) along a trip (`/data/{index}/relationships/trip/data/id`) going a direction (`/data/{index}/attributes/direction_id`) along a route (`/data/{index}/relationships/route/data/id`).  See [GTFS Realtime `FeedMesage` `FeedEntity` `TripUpdate` `TripDescriptor`](https://github.com/google/transit/blob/master/gtfs-realtime/spec/en/reference.md#message-tripdescriptor) See [GTFS Realtime `FeedMesage` `FeedEntity` `TripUpdate` `StopTimeUpdate`](https://github.com/google/transit/blob/master/gtfs-realtime/spec/en/reference.md#message-stoptimeupdate)   ## When a vehicle is predicted to be at a stop  `/predictions?filter[stop]=STOP_ID`  ## The predicted schedule for one route  `/predictions?filter[route]=ROUTE_ID`  ## The predicted schedule for a whole trip  `/predictions?filter[trip]=TRIP_ID`    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_web_prediction_controller_index_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page_offset: Offset (0-based) of first element in the page
        :param int page_limit: Max number of elements to return
        :param str sort: Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any `/data/{index}/attributes` key. Assumes ascending; may be prefixed with '-' for descending  | JSON pointer | Direction | `sort`     | |--------------|-----------|------------| | `/data/{index}/attributes/arrival_time` | ascending | `arrival_time` | | `/data/{index}/attributes/arrival_time` | descending | `-arrival_time` | | `/data/{index}/attributes/departure_time` | ascending | `departure_time` | | `/data/{index}/attributes/departure_time` | descending | `-departure_time` | | `/data/{index}/attributes/direction_id` | ascending | `direction_id` | | `/data/{index}/attributes/direction_id` | descending | `-direction_id` | | `/data/{index}/attributes/schedule_relationship` | ascending | `schedule_relationship` | | `/data/{index}/attributes/schedule_relationship` | descending | `-schedule_relationship` | | `/data/{index}/attributes/status` | ascending | `status` | | `/data/{index}/attributes/status` | descending | `-status` | | `/data/{index}/attributes/stop_sequence` | ascending | `stop_sequence` | | `/data/{index}/attributes/stop_sequence` | descending | `-stop_sequence` | | `/data/{index}/attributes/track` | ascending | `track` | | `/data/{index}/attributes/track` | descending | `-track` |  
        :param str include: Relationships to include.  * `schedule` * `stop` * `route` * `trip` * `vehicle` * `alerts`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)   
        :param str filter_latitude:  Latitude/Longitude must be both present or both absent.
        :param str filter_longitude:  Latitude/Longitude must be both present or both absent.
        :param str filter_direction_id: Filter by direction of travel along the route.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.    
        :param str filter_stop: Filter by `/data/{index}/relationships/stop/data/id`. Multiple `/data/{index}/relationships/stop/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list.
        :param str filter_route: Filter by `/data/{index}/relationships/route/data/id`. Multiple `/data/{index}/relationships/route/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list.
        :param str filter_trip: Filter by `/data/{index}/relationships/trip/data/id`. Multiple `/data/{index}/relationships/trip/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list.
        :return: Predictions
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_offset', 'page_limit', 'sort', 'include', 'filter_latitude', 'filter_longitude', 'filter_direction_id', 'filter_stop', 'filter_route', 'filter_trip']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_web_prediction_controller_index" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page_offset' in params and params['page_offset'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_offset` when calling `api_web_prediction_controller_index`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'page_limit' in params and params['page_limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_limit` when calling `api_web_prediction_controller_index`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_offset' in params:
            query_params.append(('page[offset]', params['page_offset']))  # noqa: E501
        if 'page_limit' in params:
            query_params.append(('page[limit]', params['page_limit']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'include' in params:
            query_params.append(('include', params['include']))  # noqa: E501
        if 'filter_latitude' in params:
            query_params.append(('filter[latitude]', params['filter_latitude']))  # noqa: E501
        if 'filter_longitude' in params:
            query_params.append(('filter[longitude]', params['filter_longitude']))  # noqa: E501
        if 'filter_direction_id' in params:
            query_params.append(('filter[direction_id]', params['filter_direction_id']))  # noqa: E501
        if 'filter_stop' in params:
            query_params.append(('filter[stop]', params['filter_stop']))  # noqa: E501
        if 'filter_route' in params:
            query_params.append(('filter[route]', params['filter_route']))  # noqa: E501
        if 'filter_trip' in params:
            query_params.append(('filter[trip]', params['filter_trip']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.api+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/vnd.api+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key_in_header', 'api_key_in_query']  # noqa: E501

        return self.api_client.call_api(
            '/predictions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Predictions',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
