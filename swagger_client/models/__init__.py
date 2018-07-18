# coding: utf-8

# flake8: noqa
"""
    MBTA

    MBTA service API. https://www.mbta.com  # noqa: E501

    OpenAPI spec version: 3.0
    Contact: developer@mbta.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from swagger_client.models.active_period import ActivePeriod
from swagger_client.models.activity import Activity
from swagger_client.models.alert import Alert
from swagger_client.models.alert_resource import AlertResource
from swagger_client.models.alert_resource_attributes import AlertResourceAttributes
from swagger_client.models.alert_resource_relationships import AlertResourceRelationships
from swagger_client.models.alert_resource_relationships_facility import AlertResourceRelationshipsFacility
from swagger_client.models.alert_resource_relationships_facility_data import AlertResourceRelationshipsFacilityData
from swagger_client.models.alert_resource_relationships_facility_links import AlertResourceRelationshipsFacilityLinks
from swagger_client.models.alerts import Alerts
from swagger_client.models.bad_request import BadRequest
from swagger_client.models.bad_request_errors import BadRequestErrors
from swagger_client.models.bad_request_source import BadRequestSource
from swagger_client.models.facilities import Facilities
from swagger_client.models.facility import Facility
from swagger_client.models.facility_property import FacilityProperty
from swagger_client.models.facility_resource import FacilityResource
from swagger_client.models.facility_resource_attributes import FacilityResourceAttributes
from swagger_client.models.facility_resource_relationships import FacilityResourceRelationships
from swagger_client.models.forbidden import Forbidden
from swagger_client.models.forbidden_errors import ForbiddenErrors
from swagger_client.models.informed_entity import InformedEntity
from swagger_client.models.not_found import NotFound
from swagger_client.models.not_found_errors import NotFoundErrors
from swagger_client.models.not_found_source import NotFoundSource
from swagger_client.models.prediction_resource import PredictionResource
from swagger_client.models.prediction_resource_attributes import PredictionResourceAttributes
from swagger_client.models.prediction_resource_relationships import PredictionResourceRelationships
from swagger_client.models.prediction_resource_relationships_alerts import PredictionResourceRelationshipsAlerts
from swagger_client.models.prediction_resource_relationships_alerts_data import PredictionResourceRelationshipsAlertsData
from swagger_client.models.prediction_resource_relationships_alerts_links import PredictionResourceRelationshipsAlertsLinks
from swagger_client.models.prediction_resource_relationships_schedule import PredictionResourceRelationshipsSchedule
from swagger_client.models.prediction_resource_relationships_schedule_data import PredictionResourceRelationshipsScheduleData
from swagger_client.models.prediction_resource_relationships_schedule_links import PredictionResourceRelationshipsScheduleLinks
from swagger_client.models.prediction_resource_relationships_vehicle import PredictionResourceRelationshipsVehicle
from swagger_client.models.prediction_resource_relationships_vehicle_data import PredictionResourceRelationshipsVehicleData
from swagger_client.models.prediction_resource_relationships_vehicle_links import PredictionResourceRelationshipsVehicleLinks
from swagger_client.models.predictions import Predictions
from swagger_client.models.route import Route
from swagger_client.models.route_links import RouteLinks
from swagger_client.models.route_resource import RouteResource
from swagger_client.models.route_resource_attributes import RouteResourceAttributes
from swagger_client.models.routes import Routes
from swagger_client.models.schedule_resource import ScheduleResource
from swagger_client.models.schedule_resource_attributes import ScheduleResourceAttributes
from swagger_client.models.schedule_resource_relationships import ScheduleResourceRelationships
from swagger_client.models.schedule_resource_relationships_prediction import ScheduleResourceRelationshipsPrediction
from swagger_client.models.schedule_resource_relationships_prediction_data import ScheduleResourceRelationshipsPredictionData
from swagger_client.models.schedule_resource_relationships_prediction_links import ScheduleResourceRelationshipsPredictionLinks
from swagger_client.models.schedule_resource_relationships_route import ScheduleResourceRelationshipsRoute
from swagger_client.models.schedule_resource_relationships_route_data import ScheduleResourceRelationshipsRouteData
from swagger_client.models.schedule_resource_relationships_route_links import ScheduleResourceRelationshipsRouteLinks
from swagger_client.models.schedule_resource_relationships_stop import ScheduleResourceRelationshipsStop
from swagger_client.models.schedule_resource_relationships_stop_data import ScheduleResourceRelationshipsStopData
from swagger_client.models.schedule_resource_relationships_stop_links import ScheduleResourceRelationshipsStopLinks
from swagger_client.models.schedule_resource_relationships_trip import ScheduleResourceRelationshipsTrip
from swagger_client.models.schedule_resource_relationships_trip_data import ScheduleResourceRelationshipsTripData
from swagger_client.models.schedule_resource_relationships_trip_links import ScheduleResourceRelationshipsTripLinks
from swagger_client.models.schedules import Schedules
from swagger_client.models.shape import Shape
from swagger_client.models.shape_resource import ShapeResource
from swagger_client.models.shape_resource_attributes import ShapeResourceAttributes
from swagger_client.models.shape_resource_relationships import ShapeResourceRelationships
from swagger_client.models.shape_resource_relationships_stops import ShapeResourceRelationshipsStops
from swagger_client.models.shape_resource_relationships_stops_data import ShapeResourceRelationshipsStopsData
from swagger_client.models.shape_resource_relationships_stops_links import ShapeResourceRelationshipsStopsLinks
from swagger_client.models.shapes import Shapes
from swagger_client.models.stop import Stop
from swagger_client.models.stop_resource import StopResource
from swagger_client.models.stop_resource_attributes import StopResourceAttributes
from swagger_client.models.stop_resource_relationships import StopResourceRelationships
from swagger_client.models.stop_resource_relationships_parent_station import StopResourceRelationshipsParentStation
from swagger_client.models.stop_resource_relationships_parent_station_data import StopResourceRelationshipsParentStationData
from swagger_client.models.stop_resource_relationships_parent_station_links import StopResourceRelationshipsParentStationLinks
from swagger_client.models.stops import Stops
from swagger_client.models.too_many_requests import TooManyRequests
from swagger_client.models.too_many_requests_errors import TooManyRequestsErrors
from swagger_client.models.trip import Trip
from swagger_client.models.trip_resource import TripResource
from swagger_client.models.trip_resource_attributes import TripResourceAttributes
from swagger_client.models.trip_resource_relationships import TripResourceRelationships
from swagger_client.models.trip_resource_relationships_service import TripResourceRelationshipsService
from swagger_client.models.trip_resource_relationships_service_data import TripResourceRelationshipsServiceData
from swagger_client.models.trip_resource_relationships_service_links import TripResourceRelationshipsServiceLinks
from swagger_client.models.trip_resource_relationships_shape import TripResourceRelationshipsShape
from swagger_client.models.trip_resource_relationships_shape_data import TripResourceRelationshipsShapeData
from swagger_client.models.trip_resource_relationships_shape_links import TripResourceRelationshipsShapeLinks
from swagger_client.models.trips import Trips
from swagger_client.models.vehicle import Vehicle
from swagger_client.models.vehicle_resource import VehicleResource
from swagger_client.models.vehicle_resource_attributes import VehicleResourceAttributes
from swagger_client.models.vehicle_resource_relationships import VehicleResourceRelationships
from swagger_client.models.vehicles import Vehicles
from swagger_client.models.vehicles_links import VehiclesLinks