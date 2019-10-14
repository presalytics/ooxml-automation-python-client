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


class ChartAxes(object):
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
        'charts_id': 'str',
        'chart': 'ChartCharts',
        'title_text_container_id': 'str',
        'title_text_container': 'SharedTextContainer',
        'ooxml_id': 'int',
        'axis_data_type_id': 'int',
        'id': 'str',
        'date_created': 'datetime',
        'user_created': 'str',
        'date_modified': 'datetime',
        'user_modified': 'str'
    }

    attribute_map = {
        'charts_id': 'chartsId',
        'chart': 'chart',
        'title_text_container_id': 'titleTextContainerId',
        'title_text_container': 'titleTextContainer',
        'ooxml_id': 'ooxmlId',
        'axis_data_type_id': 'axisDataTypeId',
        'id': 'id',
        'date_created': 'dateCreated',
        'user_created': 'userCreated',
        'date_modified': 'dateModified',
        'user_modified': 'userModified'
    }

    def __init__(self, charts_id=None, chart=None, title_text_container_id=None, title_text_container=None, ooxml_id=None, axis_data_type_id=None, id=None, date_created=None, user_created=None, date_modified=None, user_modified=None):  # noqa: E501
        """ChartAxes - a model defined in OpenAPI"""  # noqa: E501

        self._charts_id = None
        self._chart = None
        self._title_text_container_id = None
        self._title_text_container = None
        self._ooxml_id = None
        self._axis_data_type_id = None
        self._id = None
        self._date_created = None
        self._user_created = None
        self._date_modified = None
        self._user_modified = None
        self.discriminator = None

        if charts_id is not None:
            self.charts_id = charts_id
        if chart is not None:
            self.chart = chart
        self.title_text_container_id = title_text_container_id
        if title_text_container is not None:
            self.title_text_container = title_text_container
        if ooxml_id is not None:
            self.ooxml_id = ooxml_id
        if axis_data_type_id is not None:
            self.axis_data_type_id = axis_data_type_id
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
    def charts_id(self):
        """Gets the charts_id of this ChartAxes.  # noqa: E501


        :return: The charts_id of this ChartAxes.  # noqa: E501
        :rtype: str
        """
        return self._charts_id

    @charts_id.setter
    def charts_id(self, charts_id):
        """Sets the charts_id of this ChartAxes.


        :param charts_id: The charts_id of this ChartAxes.  # noqa: E501
        :type: str
        """

        self._charts_id = charts_id

    @property
    def chart(self):
        """Gets the chart of this ChartAxes.  # noqa: E501


        :return: The chart of this ChartAxes.  # noqa: E501
        :rtype: ChartCharts
        """
        return self._chart

    @chart.setter
    def chart(self, chart):
        """Sets the chart of this ChartAxes.


        :param chart: The chart of this ChartAxes.  # noqa: E501
        :type: ChartCharts
        """

        self._chart = chart

    @property
    def title_text_container_id(self):
        """Gets the title_text_container_id of this ChartAxes.  # noqa: E501


        :return: The title_text_container_id of this ChartAxes.  # noqa: E501
        :rtype: str
        """
        return self._title_text_container_id

    @title_text_container_id.setter
    def title_text_container_id(self, title_text_container_id):
        """Sets the title_text_container_id of this ChartAxes.


        :param title_text_container_id: The title_text_container_id of this ChartAxes.  # noqa: E501
        :type: str
        """

        self._title_text_container_id = title_text_container_id

    @property
    def title_text_container(self):
        """Gets the title_text_container of this ChartAxes.  # noqa: E501


        :return: The title_text_container of this ChartAxes.  # noqa: E501
        :rtype: SharedTextContainer
        """
        return self._title_text_container

    @title_text_container.setter
    def title_text_container(self, title_text_container):
        """Sets the title_text_container of this ChartAxes.


        :param title_text_container: The title_text_container of this ChartAxes.  # noqa: E501
        :type: SharedTextContainer
        """

        self._title_text_container = title_text_container

    @property
    def ooxml_id(self):
        """Gets the ooxml_id of this ChartAxes.  # noqa: E501


        :return: The ooxml_id of this ChartAxes.  # noqa: E501
        :rtype: int
        """
        return self._ooxml_id

    @ooxml_id.setter
    def ooxml_id(self, ooxml_id):
        """Sets the ooxml_id of this ChartAxes.


        :param ooxml_id: The ooxml_id of this ChartAxes.  # noqa: E501
        :type: int
        """

        self._ooxml_id = ooxml_id

    @property
    def axis_data_type_id(self):
        """Gets the axis_data_type_id of this ChartAxes.  # noqa: E501


        :return: The axis_data_type_id of this ChartAxes.  # noqa: E501
        :rtype: int
        """
        return self._axis_data_type_id

    @axis_data_type_id.setter
    def axis_data_type_id(self, axis_data_type_id):
        """Sets the axis_data_type_id of this ChartAxes.


        :param axis_data_type_id: The axis_data_type_id of this ChartAxes.  # noqa: E501
        :type: int
        """

        self._axis_data_type_id = axis_data_type_id

    @property
    def id(self):
        """Gets the id of this ChartAxes.  # noqa: E501


        :return: The id of this ChartAxes.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChartAxes.


        :param id: The id of this ChartAxes.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def date_created(self):
        """Gets the date_created of this ChartAxes.  # noqa: E501


        :return: The date_created of this ChartAxes.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this ChartAxes.


        :param date_created: The date_created of this ChartAxes.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def user_created(self):
        """Gets the user_created of this ChartAxes.  # noqa: E501


        :return: The user_created of this ChartAxes.  # noqa: E501
        :rtype: str
        """
        return self._user_created

    @user_created.setter
    def user_created(self, user_created):
        """Sets the user_created of this ChartAxes.


        :param user_created: The user_created of this ChartAxes.  # noqa: E501
        :type: str
        """

        self._user_created = user_created

    @property
    def date_modified(self):
        """Gets the date_modified of this ChartAxes.  # noqa: E501


        :return: The date_modified of this ChartAxes.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this ChartAxes.


        :param date_modified: The date_modified of this ChartAxes.  # noqa: E501
        :type: datetime
        """

        self._date_modified = date_modified

    @property
    def user_modified(self):
        """Gets the user_modified of this ChartAxes.  # noqa: E501


        :return: The user_modified of this ChartAxes.  # noqa: E501
        :rtype: str
        """
        return self._user_modified

    @user_modified.setter
    def user_modified(self, user_modified):
        """Sets the user_modified of this ChartAxes.


        :param user_modified: The user_modified of this ChartAxes.  # noqa: E501
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
        if not isinstance(other, ChartAxes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
