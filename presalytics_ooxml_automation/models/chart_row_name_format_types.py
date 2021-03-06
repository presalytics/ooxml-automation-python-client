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


class ChartRowNameFormatTypes(object):
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
        'type_id': 'int',
        'power_tools_id': 'int',
        'format_code': 'str',
        'id': 'str'
    }

    attribute_map = {
        'type_id': 'typeId',
        'power_tools_id': 'powerToolsId',
        'format_code': 'formatCode',
        'id': 'id'
    }

    def __init__(self, type_id=None, power_tools_id=None, format_code=None, id=None, local_vars_configuration=None):  # noqa: E501
        """ChartRowNameFormatTypes - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type_id = None
        self._power_tools_id = None
        self._format_code = None
        self._id = None
        self.discriminator = None

        if type_id is not None:
            self.type_id = type_id
        if power_tools_id is not None:
            self.power_tools_id = power_tools_id
        self.format_code = format_code
        if id is not None:
            self.id = id

    @property
    def type_id(self):
        """Gets the type_id of this ChartRowNameFormatTypes.  # noqa: E501


        :return: The type_id of this ChartRowNameFormatTypes.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this ChartRowNameFormatTypes.


        :param type_id: The type_id of this ChartRowNameFormatTypes.  # noqa: E501
        :type: int
        """

        self._type_id = type_id

    @property
    def power_tools_id(self):
        """Gets the power_tools_id of this ChartRowNameFormatTypes.  # noqa: E501


        :return: The power_tools_id of this ChartRowNameFormatTypes.  # noqa: E501
        :rtype: int
        """
        return self._power_tools_id

    @power_tools_id.setter
    def power_tools_id(self, power_tools_id):
        """Sets the power_tools_id of this ChartRowNameFormatTypes.


        :param power_tools_id: The power_tools_id of this ChartRowNameFormatTypes.  # noqa: E501
        :type: int
        """

        self._power_tools_id = power_tools_id

    @property
    def format_code(self):
        """Gets the format_code of this ChartRowNameFormatTypes.  # noqa: E501


        :return: The format_code of this ChartRowNameFormatTypes.  # noqa: E501
        :rtype: str
        """
        return self._format_code

    @format_code.setter
    def format_code(self, format_code):
        """Sets the format_code of this ChartRowNameFormatTypes.


        :param format_code: The format_code of this ChartRowNameFormatTypes.  # noqa: E501
        :type: str
        """

        self._format_code = format_code

    @property
    def id(self):
        """Gets the id of this ChartRowNameFormatTypes.  # noqa: E501


        :return: The id of this ChartRowNameFormatTypes.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChartRowNameFormatTypes.


        :param id: The id of this ChartRowNameFormatTypes.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if not isinstance(other, ChartRowNameFormatTypes):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChartRowNameFormatTypes):
            return True

        return self.to_dict() != other.to_dict()
