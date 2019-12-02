# coding: utf-8

"""
    OOXML Automation

    This API helps users convert Excel and Powerpoint documents into rich, live dashboards and stories.  # noqa: E501

    The version of the OpenAPI document: 0.1.0-no-tags
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from presalytics_ooxml_automation.configuration import Configuration


class ChartRowCollections(object):
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
        'name_format_type': 'int',
        'axis_id': 'str',
        'axis': 'object',
        'chart_data_id': 'str',
        'chart_data': 'object',
        'rows': 'object',
        'id': 'str',
        'date_created': 'datetime',
        'user_created': 'str',
        'date_modified': 'datetime',
        'user_modified': 'str'
    }

    attribute_map = {
        'name_format_type': 'nameFormatType',
        'axis_id': 'axisId',
        'axis': 'axis',
        'chart_data_id': 'chartDataId',
        'chart_data': 'chartData',
        'rows': 'rows',
        'id': 'id',
        'date_created': 'dateCreated',
        'user_created': 'userCreated',
        'date_modified': 'dateModified',
        'user_modified': 'userModified'
    }

    def __init__(self, name_format_type=None, axis_id=None, axis=None, chart_data_id=None, chart_data=None, rows=None, id=None, date_created=None, user_created=None, date_modified=None, user_modified=None, local_vars_configuration=None):  # noqa: E501
        """ChartRowCollections - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name_format_type = None
        self._axis_id = None
        self._axis = None
        self._chart_data_id = None
        self._chart_data = None
        self._rows = None
        self._id = None
        self._date_created = None
        self._user_created = None
        self._date_modified = None
        self._user_modified = None
        self.discriminator = None

        if name_format_type is not None:
            self.name_format_type = name_format_type
        self.axis_id = axis_id
        if axis is not None:
            self.axis = axis
        self.chart_data_id = chart_data_id
        if chart_data is not None:
            self.chart_data = chart_data
        self.rows = rows
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
    def name_format_type(self):
        """Gets the name_format_type of this ChartRowCollections.  # noqa: E501


        :return: The name_format_type of this ChartRowCollections.  # noqa: E501
        :rtype: int
        """
        return self._name_format_type

    @name_format_type.setter
    def name_format_type(self, name_format_type):
        """Sets the name_format_type of this ChartRowCollections.


        :param name_format_type: The name_format_type of this ChartRowCollections.  # noqa: E501
        :type: int
        """

        self._name_format_type = name_format_type

    @property
    def axis_id(self):
        """Gets the axis_id of this ChartRowCollections.  # noqa: E501


        :return: The axis_id of this ChartRowCollections.  # noqa: E501
        :rtype: str
        """
        return self._axis_id

    @axis_id.setter
    def axis_id(self, axis_id):
        """Sets the axis_id of this ChartRowCollections.


        :param axis_id: The axis_id of this ChartRowCollections.  # noqa: E501
        :type: str
        """

        self._axis_id = axis_id

    @property
    def axis(self):
        """Gets the axis of this ChartRowCollections.  # noqa: E501


        :return: The axis of this ChartRowCollections.  # noqa: E501
        :rtype: object
        """
        return self._axis

    @axis.setter
    def axis(self, axis):
        """Sets the axis of this ChartRowCollections.


        :param axis: The axis of this ChartRowCollections.  # noqa: E501
        :type: object
        """

        self._axis = axis

    @property
    def chart_data_id(self):
        """Gets the chart_data_id of this ChartRowCollections.  # noqa: E501


        :return: The chart_data_id of this ChartRowCollections.  # noqa: E501
        :rtype: str
        """
        return self._chart_data_id

    @chart_data_id.setter
    def chart_data_id(self, chart_data_id):
        """Sets the chart_data_id of this ChartRowCollections.


        :param chart_data_id: The chart_data_id of this ChartRowCollections.  # noqa: E501
        :type: str
        """

        self._chart_data_id = chart_data_id

    @property
    def chart_data(self):
        """Gets the chart_data of this ChartRowCollections.  # noqa: E501


        :return: The chart_data of this ChartRowCollections.  # noqa: E501
        :rtype: object
        """
        return self._chart_data

    @chart_data.setter
    def chart_data(self, chart_data):
        """Sets the chart_data of this ChartRowCollections.


        :param chart_data: The chart_data of this ChartRowCollections.  # noqa: E501
        :type: object
        """

        self._chart_data = chart_data

    @property
    def rows(self):
        """Gets the rows of this ChartRowCollections.  # noqa: E501


        :return: The rows of this ChartRowCollections.  # noqa: E501
        :rtype: object
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this ChartRowCollections.


        :param rows: The rows of this ChartRowCollections.  # noqa: E501
        :type: object
        """

        self._rows = rows

    @property
    def id(self):
        """Gets the id of this ChartRowCollections.  # noqa: E501


        :return: The id of this ChartRowCollections.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChartRowCollections.


        :param id: The id of this ChartRowCollections.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def date_created(self):
        """Gets the date_created of this ChartRowCollections.  # noqa: E501


        :return: The date_created of this ChartRowCollections.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this ChartRowCollections.


        :param date_created: The date_created of this ChartRowCollections.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def user_created(self):
        """Gets the user_created of this ChartRowCollections.  # noqa: E501


        :return: The user_created of this ChartRowCollections.  # noqa: E501
        :rtype: str
        """
        return self._user_created

    @user_created.setter
    def user_created(self, user_created):
        """Sets the user_created of this ChartRowCollections.


        :param user_created: The user_created of this ChartRowCollections.  # noqa: E501
        :type: str
        """

        self._user_created = user_created

    @property
    def date_modified(self):
        """Gets the date_modified of this ChartRowCollections.  # noqa: E501


        :return: The date_modified of this ChartRowCollections.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this ChartRowCollections.


        :param date_modified: The date_modified of this ChartRowCollections.  # noqa: E501
        :type: datetime
        """

        self._date_modified = date_modified

    @property
    def user_modified(self):
        """Gets the user_modified of this ChartRowCollections.  # noqa: E501


        :return: The user_modified of this ChartRowCollections.  # noqa: E501
        :rtype: str
        """
        return self._user_modified

    @user_modified.setter
    def user_modified(self, user_modified):
        """Sets the user_modified of this ChartRowCollections.


        :param user_modified: The user_modified of this ChartRowCollections.  # noqa: E501
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
        if not isinstance(other, ChartRowCollections):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChartRowCollections):
            return True

        return self.to_dict() != other.to_dict()
