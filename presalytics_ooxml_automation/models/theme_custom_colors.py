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


class ThemeCustomColors(object):
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
        'theme_id': 'str',
        'name': 'str',
        'hex_value': 'str',
        'id': 'str'
    }

    attribute_map = {
        'theme_id': 'themeId',
        'name': 'name',
        'hex_value': 'hexValue',
        'id': 'id'
    }

    def __init__(self, theme_id=None, name=None, hex_value=None, id=None, local_vars_configuration=None):  # noqa: E501
        """ThemeCustomColors - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._theme_id = None
        self._name = None
        self._hex_value = None
        self._id = None
        self.discriminator = None

        self.theme_id = theme_id
        self.name = name
        self.hex_value = hex_value
        if id is not None:
            self.id = id

    @property
    def theme_id(self):
        """Gets the theme_id of this ThemeCustomColors.  # noqa: E501


        :return: The theme_id of this ThemeCustomColors.  # noqa: E501
        :rtype: str
        """
        return self._theme_id

    @theme_id.setter
    def theme_id(self, theme_id):
        """Sets the theme_id of this ThemeCustomColors.


        :param theme_id: The theme_id of this ThemeCustomColors.  # noqa: E501
        :type: str
        """

        self._theme_id = theme_id

    @property
    def name(self):
        """Gets the name of this ThemeCustomColors.  # noqa: E501


        :return: The name of this ThemeCustomColors.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ThemeCustomColors.


        :param name: The name of this ThemeCustomColors.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def hex_value(self):
        """Gets the hex_value of this ThemeCustomColors.  # noqa: E501


        :return: The hex_value of this ThemeCustomColors.  # noqa: E501
        :rtype: str
        """
        return self._hex_value

    @hex_value.setter
    def hex_value(self, hex_value):
        """Sets the hex_value of this ThemeCustomColors.


        :param hex_value: The hex_value of this ThemeCustomColors.  # noqa: E501
        :type: str
        """

        self._hex_value = hex_value

    @property
    def id(self):
        """Gets the id of this ThemeCustomColors.  # noqa: E501


        :return: The id of this ThemeCustomColors.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ThemeCustomColors.


        :param id: The id of this ThemeCustomColors.  # noqa: E501
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
        if not isinstance(other, ThemeCustomColors):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ThemeCustomColors):
            return True

        return self.to_dict() != other.to_dict()
