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


class ThemeBackgroundFills(object):
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
        'theme_id': 'int',
        'intensity_id': 'int',
        'fill_maps_id': 'int',
        'id': 'int',
        'date_created': 'datetime',
        'user_created': 'str',
        'date_modified': 'datetime',
        'user_modified': 'str'
    }

    attribute_map = {
        'theme_id': 'ThemeId',
        'intensity_id': 'IntensityId',
        'fill_maps_id': 'FillMapsId',
        'id': 'Id',
        'date_created': 'DateCreated',
        'user_created': 'UserCreated',
        'date_modified': 'DateModified',
        'user_modified': 'UserModified'
    }

    def __init__(self, theme_id=None, intensity_id=None, fill_maps_id=None, id=None, date_created=None, user_created=None, date_modified=None, user_modified=None):  # noqa: E501
        """ThemeBackgroundFills - a model defined in OpenAPI"""  # noqa: E501

        self._theme_id = None
        self._intensity_id = None
        self._fill_maps_id = None
        self._id = None
        self._date_created = None
        self._user_created = None
        self._date_modified = None
        self._user_modified = None
        self.discriminator = None

        if theme_id is not None:
            self.theme_id = theme_id
        if intensity_id is not None:
            self.intensity_id = intensity_id
        if fill_maps_id is not None:
            self.fill_maps_id = fill_maps_id
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
        """Gets the theme_id of this ThemeBackgroundFills.  # noqa: E501


        :return: The theme_id of this ThemeBackgroundFills.  # noqa: E501
        :rtype: int
        """
        return self._theme_id

    @theme_id.setter
    def theme_id(self, theme_id):
        """Sets the theme_id of this ThemeBackgroundFills.


        :param theme_id: The theme_id of this ThemeBackgroundFills.  # noqa: E501
        :type: int
        """

        self._theme_id = theme_id

    @property
    def intensity_id(self):
        """Gets the intensity_id of this ThemeBackgroundFills.  # noqa: E501


        :return: The intensity_id of this ThemeBackgroundFills.  # noqa: E501
        :rtype: int
        """
        return self._intensity_id

    @intensity_id.setter
    def intensity_id(self, intensity_id):
        """Sets the intensity_id of this ThemeBackgroundFills.


        :param intensity_id: The intensity_id of this ThemeBackgroundFills.  # noqa: E501
        :type: int
        """

        self._intensity_id = intensity_id

    @property
    def fill_maps_id(self):
        """Gets the fill_maps_id of this ThemeBackgroundFills.  # noqa: E501


        :return: The fill_maps_id of this ThemeBackgroundFills.  # noqa: E501
        :rtype: int
        """
        return self._fill_maps_id

    @fill_maps_id.setter
    def fill_maps_id(self, fill_maps_id):
        """Sets the fill_maps_id of this ThemeBackgroundFills.


        :param fill_maps_id: The fill_maps_id of this ThemeBackgroundFills.  # noqa: E501
        :type: int
        """

        self._fill_maps_id = fill_maps_id

    @property
    def id(self):
        """Gets the id of this ThemeBackgroundFills.  # noqa: E501


        :return: The id of this ThemeBackgroundFills.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ThemeBackgroundFills.


        :param id: The id of this ThemeBackgroundFills.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def date_created(self):
        """Gets the date_created of this ThemeBackgroundFills.  # noqa: E501


        :return: The date_created of this ThemeBackgroundFills.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this ThemeBackgroundFills.


        :param date_created: The date_created of this ThemeBackgroundFills.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def user_created(self):
        """Gets the user_created of this ThemeBackgroundFills.  # noqa: E501


        :return: The user_created of this ThemeBackgroundFills.  # noqa: E501
        :rtype: str
        """
        return self._user_created

    @user_created.setter
    def user_created(self, user_created):
        """Sets the user_created of this ThemeBackgroundFills.


        :param user_created: The user_created of this ThemeBackgroundFills.  # noqa: E501
        :type: str
        """

        self._user_created = user_created

    @property
    def date_modified(self):
        """Gets the date_modified of this ThemeBackgroundFills.  # noqa: E501


        :return: The date_modified of this ThemeBackgroundFills.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this ThemeBackgroundFills.


        :param date_modified: The date_modified of this ThemeBackgroundFills.  # noqa: E501
        :type: datetime
        """

        self._date_modified = date_modified

    @property
    def user_modified(self):
        """Gets the user_modified of this ThemeBackgroundFills.  # noqa: E501


        :return: The user_modified of this ThemeBackgroundFills.  # noqa: E501
        :rtype: str
        """
        return self._user_modified

    @user_modified.setter
    def user_modified(self, user_modified):
        """Sets the user_modified of this ThemeBackgroundFills.


        :param user_modified: The user_modified of this ThemeBackgroundFills.  # noqa: E501
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
        if not isinstance(other, ThemeBackgroundFills):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other