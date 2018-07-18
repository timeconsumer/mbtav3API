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


class FacilityApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_web_facility_controller_index(self, **kwargs):  # noqa: E501
        """  # noqa: E501

        List Escalators and Elevators  A facility at a station stop (`/data/relationships/stop`) that connects one part of the station to another.  An [MBTA extension](https://groups.google.com/forum/#!topic/gtfs-changes/EzC5m9k45pA).  This spec is not yet finalized.  ## Accessibility  Riders with limited mobility can search any facility, either `ELEVATOR` or `ESCALATOR`, while riders that need wheelchair access can search for `ELEVATOR` only.  The lack of an `ELEVATOR` MAY NOT make a stop wheelchair inaccessible.  Riders should check `/stops/{id}` `/data/attributes/wheelchair_boarding` is `1` to guarantee a path is available from the station entrance to the stop or `0` if it MAY be accessible.  Completely avoid `2` as that is guaranteed to be INACCESSIBLE.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_web_facility_controller_index(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page_offset: Offset (0-based) of first element in the page
        :param int page_limit: Max number of elements to return
        :param str sort: Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any `/data/{index}/attributes` key. Assumes ascending; may be prefixed with '-' for descending  | JSON pointer | Direction | `sort`     | |--------------|-----------|------------| | `/data/{index}/attributes/name` | ascending | `name` | | `/data/{index}/attributes/name` | descending | `-name` | | `/data/{index}/attributes/properties` | ascending | `properties` | | `/data/{index}/attributes/properties` | descending | `-properties` | | `/data/{index}/attributes/type` | ascending | `type` | | `/data/{index}/attributes/type` | descending | `-type` |  
        :param str include: Relationships to include.  * `stop`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)   
        :param str filter_stop: Filter by `/data/{index}/relationships/stop/data/id`. Multiple `/data/{index}/relationships/stop/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list.
        :return: Facilities
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.api_web_facility_controller_index_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_web_facility_controller_index_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_web_facility_controller_index_with_http_info(self, **kwargs):  # noqa: E501
        """  # noqa: E501

        List Escalators and Elevators  A facility at a station stop (`/data/relationships/stop`) that connects one part of the station to another.  An [MBTA extension](https://groups.google.com/forum/#!topic/gtfs-changes/EzC5m9k45pA).  This spec is not yet finalized.  ## Accessibility  Riders with limited mobility can search any facility, either `ELEVATOR` or `ESCALATOR`, while riders that need wheelchair access can search for `ELEVATOR` only.  The lack of an `ELEVATOR` MAY NOT make a stop wheelchair inaccessible.  Riders should check `/stops/{id}` `/data/attributes/wheelchair_boarding` is `1` to guarantee a path is available from the station entrance to the stop or `0` if it MAY be accessible.  Completely avoid `2` as that is guaranteed to be INACCESSIBLE.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_web_facility_controller_index_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page_offset: Offset (0-based) of first element in the page
        :param int page_limit: Max number of elements to return
        :param str sort: Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any `/data/{index}/attributes` key. Assumes ascending; may be prefixed with '-' for descending  | JSON pointer | Direction | `sort`     | |--------------|-----------|------------| | `/data/{index}/attributes/name` | ascending | `name` | | `/data/{index}/attributes/name` | descending | `-name` | | `/data/{index}/attributes/properties` | ascending | `properties` | | `/data/{index}/attributes/properties` | descending | `-properties` | | `/data/{index}/attributes/type` | ascending | `type` | | `/data/{index}/attributes/type` | descending | `-type` |  
        :param str include: Relationships to include.  * `stop`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)   
        :param str filter_stop: Filter by `/data/{index}/relationships/stop/data/id`. Multiple `/data/{index}/relationships/stop/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list.
        :return: Facilities
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_offset', 'page_limit', 'sort', 'include', 'filter_stop']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_web_facility_controller_index" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page_offset' in params and params['page_offset'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_offset` when calling `api_web_facility_controller_index`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'page_limit' in params and params['page_limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_limit` when calling `api_web_facility_controller_index`, must be a value greater than or equal to `1`")  # noqa: E501
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
        if 'filter_stop' in params:
            query_params.append(('filter[stop]', params['filter_stop']))  # noqa: E501

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
            '/facilities', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Facilities',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_web_facility_controller_show(self, id, **kwargs):  # noqa: E501
        """  # noqa: E501

        Specific Escalator or Elevator  A facility at a station stop (`/data/{index}/relationships/stop`) that connects one part of the station to another.  An [MBTA extension](https://groups.google.com/forum/#!topic/gtfs-changes/EzC5m9k45pA).  This spec is not yet finalized.  ## Accessibility  Riders with limited mobility can search any facility, either `ELEVATOR` or `ESCALATOR`, while riders that need wheelchair access can search for `ELEVATOR` only.  The lack of an `ELEVATOR` MAY NOT make a stop wheelchair inaccessible.  Riders should check `/stops/{id}` `/data/attributes/wheelchair_boarding` is `1` to guarantee a path is available from the station entrance to the stop or `0` if it MAY be accessible.  Completely avoid `2` as that is guaranteed to be INACCESSIBLE.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_web_facility_controller_show(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: Unique identifier for facility (required)
        :param str include: Relationships to include.  * `stops`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)   
        :return: Facility
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.api_web_facility_controller_show_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_web_facility_controller_show_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def api_web_facility_controller_show_with_http_info(self, id, **kwargs):  # noqa: E501
        """  # noqa: E501

        Specific Escalator or Elevator  A facility at a station stop (`/data/{index}/relationships/stop`) that connects one part of the station to another.  An [MBTA extension](https://groups.google.com/forum/#!topic/gtfs-changes/EzC5m9k45pA).  This spec is not yet finalized.  ## Accessibility  Riders with limited mobility can search any facility, either `ELEVATOR` or `ESCALATOR`, while riders that need wheelchair access can search for `ELEVATOR` only.  The lack of an `ELEVATOR` MAY NOT make a stop wheelchair inaccessible.  Riders should check `/stops/{id}` `/data/attributes/wheelchair_boarding` is `1` to guarantee a path is available from the station entrance to the stop or `0` if it MAY be accessible.  Completely avoid `2` as that is guaranteed to be INACCESSIBLE.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_web_facility_controller_show_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: Unique identifier for facility (required)
        :param str include: Relationships to include.  * `stops`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)   
        :return: Facility
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'include']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_web_facility_controller_show" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `api_web_facility_controller_show`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'include' in params:
            query_params.append(('include', params['include']))  # noqa: E501

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
            '/facilities/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Facility',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
