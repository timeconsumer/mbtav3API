# coding: utf-8

"""
    MBTA

    MBTA service API. https://www.mbta.com  # noqa: E501

    OpenAPI spec version: 3.0
    Contact: developer@mbta.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.stop_api import StopApi  # noqa: E501
from swagger_client.rest import ApiException


class TestStopApi(unittest.TestCase):
    """StopApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.stop_api.StopApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_web_stop_controller_index(self):
        """Test case for api_web_stop_controller_index

          # noqa: E501
        """
        pass

    def test_api_web_stop_controller_show(self):
        """Test case for api_web_stop_controller_show

          # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
