# coding: utf-8

"""
    OOXML Automation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0-no-tags
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ChartChartData(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'chart_id': 'str',
        'chart': 'ChartCharts',
        'row_collection': 'ChartRowCollections',
        'column_collection': 'ChartColumnCollections',
        'data_points': 'list[ChartDataPoints]',
        'id': 'str',
        'date_created': 'datetime',
        'user_created': 'str',
        'date_modified': 'datetime',
        'user_modified': 'str'
    }

    attribute_map = {
        'chart_id': 'chartId',
        'chart': 'chart',
        'row_collection': 'rowCollection',
        'column_collection': 'columnCollection',
        'data_points': 'dataPoints',
        'id': 'id',
        'date_created': 'dateCreated',
        'user_created': 'userCreated',
        'date_modified': 'dateModified',
        'user_modified': 'userModified'
    }

    def __init__(self, chart_id=None, chart=None, row_collection=None, column_collection=None, data_points=None, id=None, date_created=None, user_created=None, date_modified=None, user_modified=None):  # noqa: E501
        """ChartChartData - a model defined in OpenAPI"""  # noqa: E501

        self._chart_id = None
        self._chart = None
        self._row_collection = None
        self._column_collection = None
        self._data_points = None
        self._id = None
        self._date_created = None
        self._user_created = None
        self._date_modified = None
        self._user_modified = None
        self.discriminator = None

        self.chart_id = chart_id
        if chart is not None:
            self.chart = chart
        if row_collection is not None:
            self.row_collection = row_collection
        if column_collection is not None:
            self.column_collection = column_collection
        self.data_points = data_points
        if id is not None:
            self.id = id
        if date_created is not None:
            self.date_created = date_created
        if user_created is not None:
            self.user_created = user_created
        if date_modified is not None:
            self.date_modified = date_modified
        if user_modified is not None:
            self.user_modified = user_modified

    @property
    def chart_id(self):
        """Gets the chart_id of this ChartChartData.  # noqa: E501


        :return: The chart_id of this ChartChartData.  # noqa: E501
        :rtype: str
        """
        return self._chart_id

    @chart_id.setter
    def chart_id(self, chart_id):
        """Sets the chart_id of this ChartChartData.


        :param chart_id: The chart_id of this ChartChartData.  # noqa: E501
        :type: str
        """

        self._chart_id = chart_id

    @property
    def chart(self):
        """Gets the chart of this ChartChartData.  # noqa: E501


        :return: The chart of this ChartChartData.  # noqa: E501
        :rtype: ChartCharts
        """
        return self._chart

    @chart.setter
    def chart(self, chart):
        """Sets the chart of this ChartChartData.


        :param chart: The chart of this ChartChartData.  # noqa: E501
        :type: ChartCharts
        """

        self._chart = chart

    @property
    def row_collection(self):
        """Gets the row_collection of this ChartChartData.  # noqa: E501


        :return: The row_collection of this ChartChartData.  # noqa: E501
        :rtype: ChartRowCollections
        """
        return self._row_collection

    @row_collection.setter
    def row_collection(self, row_collection):
        """Sets the row_collection of this ChartChartData.


        :param row_collection: The row_collection of this ChartChartData.  # noqa: E501
        :type: ChartRowCollections
        """

        self._row_collection = row_collection

    @property
    def column_collection(self):
        """Gets the column_collection of this ChartChartData.  # noqa: E501


        :return: The column_collection of this ChartChartData.  # noqa: E501
        :rtype: ChartColumnCollections
        """
        return self._column_collection

    @column_collection.setter
    def column_collection(self, column_collection):
        """Sets the column_collection of this ChartChartData.


        :param column_collection: The column_collection of this ChartChartData.  # noqa: E501
        :type: ChartColumnCollections
        """

        self._column_collection = column_collection

    @property
    def data_points(self):
        """Gets the data_points of this ChartChartData.  # noqa: E501


        :return: The data_points of this ChartChartData.  # noqa: E501
        :rtype: list[ChartDataPoints]
        """
        return self._data_points

    @data_points.setter
    def data_points(self, data_points):
        """Sets the data_points of this ChartChartData.


        :param data_points: The data_points of this ChartChartData.  # noqa: E501
        :type: list[ChartDataPoints]
        """

        self._data_points = data_points

    @property
    def id(self):
        """Gets the id of this ChartChartData.  # noqa: E501


        :return: The id of this ChartChartData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChartChartData.


        :param id: The id of this ChartChartData.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def date_created(self):
        """Gets the date_created of this ChartChartData.  # noqa: E501


        :return: The date_created of this ChartChartData.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this ChartChartData.


        :param date_created: The date_created of this ChartChartData.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def user_created(self):
        """Gets the user_created of this ChartChartData.  # noqa: E501


        :return: The user_created of this ChartChartData.  # noqa: E501
        :rtype: str
        """
        return self._user_created

    @user_created.setter
    def user_created(self, user_created):
        """Sets the user_created of this ChartChartData.


        :param user_created: The user_created of this ChartChartData.  # noqa: E501
        :type: str
        """

        self._user_created = user_created

    @property
    def date_modified(self):
        """Gets the date_modified of this ChartChartData.  # noqa: E501


        :return: The date_modified of this ChartChartData.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this ChartChartData.


        :param date_modified: The date_modified of this ChartChartData.  # noqa: E501
        :type: datetime
        """

        self._date_modified = date_modified

    @property
    def user_modified(self):
        """Gets the user_modified of this ChartChartData.  # noqa: E501


        :return: The user_modified of this ChartChartData.  # noqa: E501
        :rtype: str
        """
        return self._user_modified

    @user_modified.setter
    def user_modified(self, user_modified):
        """Sets the user_modified of this ChartChartData.


        :param user_modified: The user_modified of this ChartChartData.  # noqa: E501
        :type: str
        """

        self._user_modified = user_modified

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, ChartChartData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
