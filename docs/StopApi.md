# swagger_client.StopApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_web_stop_controller_index**](StopApi.md#api_web_stop_controller_index) | **GET** /stops | 
[**api_web_stop_controller_show**](StopApi.md#api_web_stop_controller_show) | **GET** /stops/{id} | 


# **api_web_stop_controller_index**
> Stops api_web_stop_controller_index(page_offset=page_offset, page_limit=page_limit, sort=sort, include=include, filter_date=filter_date, filter_direction_id=filter_direction_id, filter_latitude=filter_latitude, filter_longitude=filter_longitude, filter_radius=filter_radius, filter_id=filter_id, filter_route_type=filter_route_type, filter_route=filter_route)



List stops.  ## Accessibility  Wheelchair boarding (`/data/{index}/attributes/wheelchair_boarding`) corresponds to [GTFS wheelchair_boarding](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#stopstxt). The MBTA handles parent station inheritance itself, so value can be treated simply:  | Value | Meaning                                       | |-------|-----------------------------------------------| | `0`   | No Information                                | | `1`   | Accessible (if trip is wheelchair accessible) | | `2`   | Inaccessible                                  |   ## Location  ### World  Use `/data/{index}/attributes/latitude` and `/data/{index}/attributes/longitude` to get the location of a stop.  ### Entrance  The stop may be inside a station.  If `/data/{index}/relationships/parent_station/data/id` is present, you should look up the parent station (`/stops/{parent_id}`) and use its location to give direction first to the parent station and then route from there to the stop.    ### Nearby  The `filter[latitude]` and `filter[longitude]` can be used together to find any stops near that latitude and longitude.  The distance is in degrees as if latitude and longitude were on a flat 2D plane and normal Pythagorean distance was calculated.  Over the region MBTA serves, `0.02` degrees is approximately `1` mile. How close is considered nearby, is controlled by `filter[radius]`, which default to `0.01` degrees (approximately a half mile). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_in_header
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure API key authorization: api_key_in_query
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.StopApi(swagger_client.ApiClient(configuration))
page_offset = 56 # int | Offset (0-based) of first element in the page (optional)
page_limit = 56 # int | Max number of elements to return (optional)
sort = 'sort_example' # str | Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any `/data/{index}/attributes` key. Assumes ascending; may be prefixed with '-' for descending  | JSON pointer | Direction | `sort`     | |--------------|-----------|------------| | `/data/{index}/attributes/address` | ascending | `address` | | `/data/{index}/attributes/address` | descending | `-address` | | `/data/{index}/attributes/description` | ascending | `description` | | `/data/{index}/attributes/description` | descending | `-description` | | `/data/{index}/attributes/latitude` | ascending | `latitude` | | `/data/{index}/attributes/latitude` | descending | `-latitude` | | `/data/{index}/attributes/location_type` | ascending | `location_type` | | `/data/{index}/attributes/location_type` | descending | `-location_type` | | `/data/{index}/attributes/longitude` | ascending | `longitude` | | `/data/{index}/attributes/longitude` | descending | `-longitude` | | `/data/{index}/attributes/name` | ascending | `name` | | `/data/{index}/attributes/name` | descending | `-name` | | `/data/{index}/attributes/platform_code` | ascending | `platform_code` | | `/data/{index}/attributes/platform_code` | descending | `-platform_code` | | `/data/{index}/attributes/platform_name` | ascending | `platform_name` | | `/data/{index}/attributes/platform_name` | descending | `-platform_name` | | `/data/{index}/attributes/wheelchair_boarding` | ascending | `wheelchair_boarding` | | `/data/{index}/attributes/wheelchair_boarding` | descending | `-wheelchair_boarding` |   (optional)
include = 'include_example' # str | Relationships to include.  * `parent_station` * `child_stops`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)    (optional)
filter_date = '2013-10-20' # date | Filter by date when stop is in use The active date is the service date. Trips that begin between midnight and 3am are considered part of the previous service day. The format is ISO8601 with the template of YYYY-MM-DD. (optional)
filter_direction_id = 'filter_direction_id_example' # str | Filter by direction of travel along the route.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.     (optional)
filter_latitude = 'filter_latitude_example' # str | Latitude in degrees North in the [WGS-84](https://en.wikipedia.org/wiki/World_Geodetic_System#A_new_World_Geodetic_System:_WGS.C2.A084) coordinate system to search `filter[radius]` degrees around with `filter[longitude]`.  (optional)
filter_longitude = 'filter_longitude_example' # str | Longitude in degrees East in the [WGS-84](https://en.wikipedia.org/wiki/World_Geodetic_System#Longitudes_on_WGS.C2.A084) coordinate system to search `filter[radius]` degrees around with `filter[latitude]`.  (optional)
filter_radius = 8.14 # float | The distance is in degrees as if latitude and longitude were on a flat 2D plane and normal Pythagorean distance was calculated.  Over the region MBTA serves, `0.02` degrees is approximately `1` mile. Defaults to `0.01` degrees (approximately a half mile).  (optional)
filter_id = 'filter_id_example' # str | Filter by `/data/{index}/id` (the stop ID). Multiple `/data/{index}/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list.  (optional)
filter_route_type = 'filter_route_type_example' # str | Filter by route type https://developers.google.com/transit/gtfs/reference/routes-file (optional)
filter_route = 'filter_route_example' # str | Filter by `/data/{index}/relationships/route/data/id`. Multiple `/data/{index}/relationships/route/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)

try:
    # 
    api_response = api_instance.api_web_stop_controller_index(page_offset=page_offset, page_limit=page_limit, sort=sort, include=include, filter_date=filter_date, filter_direction_id=filter_direction_id, filter_latitude=filter_latitude, filter_longitude=filter_longitude, filter_radius=filter_radius, filter_id=filter_id, filter_route_type=filter_route_type, filter_route=filter_route)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StopApi->api_web_stop_controller_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_offset** | **int**| Offset (0-based) of first element in the page | [optional] 
 **page_limit** | **int**| Max number of elements to return | [optional] 
 **sort** | **str**| Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any &#x60;/data/{index}/attributes&#x60; key. Assumes ascending; may be prefixed with &#39;-&#39; for descending  | JSON pointer | Direction | &#x60;sort&#x60;     | |--------------|-----------|------------| | &#x60;/data/{index}/attributes/address&#x60; | ascending | &#x60;address&#x60; | | &#x60;/data/{index}/attributes/address&#x60; | descending | &#x60;-address&#x60; | | &#x60;/data/{index}/attributes/description&#x60; | ascending | &#x60;description&#x60; | | &#x60;/data/{index}/attributes/description&#x60; | descending | &#x60;-description&#x60; | | &#x60;/data/{index}/attributes/latitude&#x60; | ascending | &#x60;latitude&#x60; | | &#x60;/data/{index}/attributes/latitude&#x60; | descending | &#x60;-latitude&#x60; | | &#x60;/data/{index}/attributes/location_type&#x60; | ascending | &#x60;location_type&#x60; | | &#x60;/data/{index}/attributes/location_type&#x60; | descending | &#x60;-location_type&#x60; | | &#x60;/data/{index}/attributes/longitude&#x60; | ascending | &#x60;longitude&#x60; | | &#x60;/data/{index}/attributes/longitude&#x60; | descending | &#x60;-longitude&#x60; | | &#x60;/data/{index}/attributes/name&#x60; | ascending | &#x60;name&#x60; | | &#x60;/data/{index}/attributes/name&#x60; | descending | &#x60;-name&#x60; | | &#x60;/data/{index}/attributes/platform_code&#x60; | ascending | &#x60;platform_code&#x60; | | &#x60;/data/{index}/attributes/platform_code&#x60; | descending | &#x60;-platform_code&#x60; | | &#x60;/data/{index}/attributes/platform_name&#x60; | ascending | &#x60;platform_name&#x60; | | &#x60;/data/{index}/attributes/platform_name&#x60; | descending | &#x60;-platform_name&#x60; | | &#x60;/data/{index}/attributes/wheelchair_boarding&#x60; | ascending | &#x60;wheelchair_boarding&#x60; | | &#x60;/data/{index}/attributes/wheelchair_boarding&#x60; | descending | &#x60;-wheelchair_boarding&#x60; |   | [optional] 
 **include** | **str**| Relationships to include.  * &#x60;parent_station&#x60; * &#x60;child_stops&#x60;  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \&quot;.\&quot;) list of relationship names. [JSONAPI \&quot;include\&quot; behavior](http://jsonapi.org/format/#fetching-includes)    | [optional] 
 **filter_date** | **date**| Filter by date when stop is in use The active date is the service date. Trips that begin between midnight and 3am are considered part of the previous service day. The format is ISO8601 with the template of YYYY-MM-DD. | [optional] 
 **filter_direction_id** | **str**| Filter by direction of travel along the route.  The meaning of &#x60;direction_id&#x60; varies based on the route. You can programmatically get the direction names from &#x60;/routes&#x60; &#x60;/data/{index}/attributes/direction_names&#x60; or &#x60;/routes/{id}&#x60; &#x60;/data/attributes/direction_names&#x60;.     | [optional] 
 **filter_latitude** | **str**| Latitude in degrees North in the [WGS-84](https://en.wikipedia.org/wiki/World_Geodetic_System#A_new_World_Geodetic_System:_WGS.C2.A084) coordinate system to search &#x60;filter[radius]&#x60; degrees around with &#x60;filter[longitude]&#x60;.  | [optional] 
 **filter_longitude** | **str**| Longitude in degrees East in the [WGS-84](https://en.wikipedia.org/wiki/World_Geodetic_System#Longitudes_on_WGS.C2.A084) coordinate system to search &#x60;filter[radius]&#x60; degrees around with &#x60;filter[latitude]&#x60;.  | [optional] 
 **filter_radius** | **float**| The distance is in degrees as if latitude and longitude were on a flat 2D plane and normal Pythagorean distance was calculated.  Over the region MBTA serves, &#x60;0.02&#x60; degrees is approximately &#x60;1&#x60; mile. Defaults to &#x60;0.01&#x60; degrees (approximately a half mile).  | [optional] 
 **filter_id** | **str**| Filter by &#x60;/data/{index}/id&#x60; (the stop ID). Multiple &#x60;/data/{index}/id&#x60; **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list.  | [optional] 
 **filter_route_type** | **str**| Filter by route type https://developers.google.com/transit/gtfs/reference/routes-file | [optional] 
 **filter_route** | **str**| Filter by &#x60;/data/{index}/relationships/route/data/id&#x60;. Multiple &#x60;/data/{index}/relationships/route/data/id&#x60; **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list. | [optional] 

### Return type

[**Stops**](Stops.md)

### Authorization

[api_key_in_header](../README.md#api_key_in_header), [api_key_in_query](../README.md#api_key_in_query)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_web_stop_controller_show**
> Stop api_web_stop_controller_show(id, include=include)



Detail for a specific stop.  ## Accessibility  Wheelchair boarding (`/data/attributes/wheelchair_boarding`) corresponds to [GTFS wheelchair_boarding](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#stopstxt). The MBTA handles parent station inheritance itself, so value can be treated simply:  | Value | Meaning                                       | |-------|-----------------------------------------------| | `0`   | No Information                                | | `1`   | Accessible (if trip is wheelchair accessible) | | `2`   | Inaccessible                                  |   ## Location  ### World  Use `/data/attributes/latitude` and `/data/attributes/longitude` to get the location of a stop.  ### Entrance  The stop may be inside a station.  If `/data/relationships/parent_station/data/id` is present, you should look up the parent station (`/stops/{parent_id}`) and use its location to give direction first to the parent station and then route from there to the stop.   

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_in_header
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure API key authorization: api_key_in_query
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.StopApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique identifier for stop
include = 'include_example' # str | Relationships to include.  * `parent_station` * `child_stops`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)    (optional)

try:
    # 
    api_response = api_instance.api_web_stop_controller_show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StopApi->api_web_stop_controller_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for stop | 
 **include** | **str**| Relationships to include.  * &#x60;parent_station&#x60; * &#x60;child_stops&#x60;  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \&quot;.\&quot;) list of relationship names. [JSONAPI \&quot;include\&quot; behavior](http://jsonapi.org/format/#fetching-includes)    | [optional] 

### Return type

[**Stop**](Stop.md)

### Authorization

[api_key_in_header](../README.md#api_key_in_header), [api_key_in_query](../README.md#api_key_in_query)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

