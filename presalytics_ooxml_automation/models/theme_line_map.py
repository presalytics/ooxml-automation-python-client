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


class ThemeLineMap(object):
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
        'theme': 'ThemeThemes',
        'intensity_id': 'int',
        'line_id': 'str',
        'line': 'SharedLines',
        'id': 'str',
        'date_created': 'datetime',
        'user_created': 'str',
        'date_modified': 'datetime',
        'user_modified': 'str'
    }

    attribute_map = {
        'theme_id': 'themeId',
        'theme': 'theme',
        'intensity_id': 'intensityId',
        'line_id': 'lineId',
        'line': 'line',
        'id': 'id',
        'date_created': 'dateCreated',
        'user_created': 'userCreated',
        'date_modified': 'dateModified',
        'user_modified': 'userModified'
    }

    def __init__(self, theme_id=None, theme=None, intensity_id=None, line_id=None, line=None, id=None, date_created=None, user_created=None, date_modified=None, user_modified=None):  # noqa: E501
        """ThemeLineMap - a model defined in OpenAPI"""  # noqa: E501

        self._theme_id = None
        self._theme = None
        self._intensity_id = None
        self._line_id = None
        self._line = None
        self._id = None
        self._date_created = None
        self._user_created = None
        self._date_modified = None
        self._user_modified = None
        self.discriminator = None

        self.theme_id = theme_id
        if theme is not None:
            self.theme = theme
        if intensity_id is not None:
            self.intensity_id = intensity_id
        self.line_id = line_id
        if line is not None:
            self.line = line
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
    def theme_id(self):
        """Gets the theme_id of this ThemeLineMap.  # noqa: E501


        :return: The theme_id of this ThemeLineMap.  # noqa: E501
        :rtype: str
        """
        return self._theme_id

    @theme_id.setter
    def theme_id(self, theme_id):
        """Sets the theme_id of this ThemeLineMap.


        :param theme_id: The theme_id of this ThemeLineMap.  # noqa: E501
        :type: str
        """

        self._theme_id = theme_id

    @property
    def theme(self):
        """Gets the theme of this ThemeLineMap.  # noqa: E501


        :return: The theme of this ThemeLineMap.  # noqa: E501
        :rtype: ThemeThemes
        """
        return self._theme

    @theme.setter
    def theme(self, theme):
        """Sets the theme of this ThemeLineMap.


        :param theme: The theme of this ThemeLineMap.  # noqa: E501
        :type: ThemeThemes
        """

        self._theme = theme

    @property
    def intensity_id(self):
        """Gets the intensity_id of this ThemeLineMap.  # noqa: E501


        :return: The intensity_id of this ThemeLineMap.  # noqa: E501
        :rtype: int
        """
        return self._intensity_id

    @intensity_id.setter
    def intensity_id(self, intensity_id):
        """Sets the intensity_id of this ThemeLineMap.


        :param intensity_id: The intensity_id of this ThemeLineMap.  # noqa: E501
        :type: int
        """

        self._intensity_id = intensity_id

    @property
    def line_id(self):
        """Gets the line_id of this ThemeLineMap.  # noqa: E501


        :return: The line_id of this ThemeLineMap.  # noqa: E501
        :rtype: str
        """
        return self._line_id

    @line_id.setter
    def line_id(self, line_id):
        """Sets the line_id of this ThemeLineMap.


        :param line_id: The line_id of this ThemeLineMap.  # noqa: E501
        :type: str
        """

        self._line_id = line_id

    @property
    def line(self):
        """Gets the line of this ThemeLineMap.  # noqa: E501


        :return: The line of this ThemeLineMap.  # noqa: E501
        :rtype: SharedLines
        """
        return self._line

    @line.setter
    def line(self, line):
        """Sets the line of this ThemeLineMap.


        :param line: The line of this ThemeLineMap.  # noqa: E501
        :type: SharedLines
        """

        self._line = line

    @property
    def id(self):
        """Gets the id of this ThemeLineMap.  # noqa: E501


        :return: The id of this ThemeLineMap.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ThemeLineMap.


        :param id: The id of this ThemeLineMap.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def date_created(self):
        """Gets the date_created of this ThemeLineMap.  # noqa: E501


        :return: The date_created of this ThemeLineMap.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this ThemeLineMap.


        :param date_created: The date_created of this ThemeLineMap.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def user_created(self):
        """Gets the user_created of this ThemeLineMap.  # noqa: E501


        :return: The user_created of this ThemeLineMap.  # noqa: E501
        :rtype: str
        """
        return self._user_created

    @user_created.setter
    def user_created(self, user_created):
        """Sets the user_created of this ThemeLineMap.


        :param user_created: The user_created of this ThemeLineMap.  # noqa: E501
        :type: str
        """

        self._user_created = user_created

    @property
    def date_modified(self):
        """Gets the date_modified of this ThemeLineMap.  # noqa: E501


        :return: The date_modified of this ThemeLineMap.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this ThemeLineMap.


        :param date_modified: The date_modified of this ThemeLineMap.  # noqa: E501
        :type: datetime
        """

        self._date_modified = date_modified

    @property
    def user_modified(self):
        """Gets the user_modified of this ThemeLineMap.  # noqa: E501


        :return: The user_modified of this ThemeLineMap.  # noqa: E501
        :rtype: str
        """
        return self._user_modified

    @user_modified.setter
    def user_modified(self, user_modified):
        """Sets the user_modified of this ThemeLineMap.


        :param user_modified: The user_modified of this ThemeLineMap.  # noqa: E501
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
        if not isinstance(other, ThemeLineMap):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
