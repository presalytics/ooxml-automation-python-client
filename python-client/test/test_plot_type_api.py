# coding: utf-8

"""
    OOXML Automation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import presalytics_ooxml_automation
from presalytics_ooxml_automation.api.plot_type_api import PlotTypeApi  # noqa: E501
from presalytics_ooxml_automation.rest import ApiException


class TestPlotTypeApi(unittest.TestCase):
    """PlotTypeApi unit test stubs"""

    def setUp(self):
        self.api = presalytics_ooxml_automation.api.plot_type_api.PlotTypeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_o_a_plot_type_get(self):
        """Test case for o_a_plot_type_get

        PlotType: List All Possible Types  # noqa: E501
        """
        pass

    def test_o_a_plot_type_get_id(self):
        """Test case for o_a_plot_type_get_id

        PlotType: Get by Id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
