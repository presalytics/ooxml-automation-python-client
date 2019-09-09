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


class SlideGraphics(object):
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
        'group_elements_id': 'str',
        'ooxml_id': 'int',
        'graphic_type_id': 'int',
        'height': 'int',
        'width': 'int',
        'x_offset': 'int',
        'y_offset': 'int',
        'id': 'str',
        'date_created': 'datetime',
        'user_created': 'str',
        'date_modified': 'datetime',
        'user_modified': 'str'
    }

    attribute_map = {
        'group_elements_id': 'groupElementsId',
        'ooxml_id': 'ooxmlId',
        'graphic_type_id': 'graphicTypeId',
        'height': 'height',
        'width': 'width',
        'x_offset': 'xOffset',
        'y_offset': 'yOffset',
        'id': 'id',
        'date_created': 'dateCreated',
        'user_created': 'userCreated',
        'date_modified': 'dateModified',
        'user_modified': 'userModified'
    }

    def __init__(self, group_elements_id=None, ooxml_id=None, graphic_type_id=None, height=None, width=None, x_offset=None, y_offset=None, id=None, date_created=None, user_created=None, date_modified=None, user_modified=None):  # noqa: E501
        """SlideGraphics - a model defined in OpenAPI"""  # noqa: E501

        self._group_elements_id = None
        self._ooxml_id = None
        self._graphic_type_id = None
        self._height = None
        self._width = None
        self._x_offset = None
        self._y_offset = None
        self._id = None
        self._date_created = None
        self._user_created = None
        self._date_modified = None
        self._user_modified = None
        self.discriminator = None

        self.group_elements_id = group_elements_id
        if ooxml_id is not None:
            self.ooxml_id = ooxml_id
        if graphic_type_id is not None:
            self.graphic_type_id = graphic_type_id
        if height is not None:
            self.height = height
        if width is not None:
            self.width = width
        if x_offset is not None:
            self.x_offset = x_offset
        if y_offset is not None:
            self.y_offset = y_offset
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
    def group_elements_id(self):
        """Gets the group_elements_id of this SlideGraphics.  # noqa: E501


        :return: The group_elements_id of this SlideGraphics.  # noqa: E501
        :rtype: str
        """
        return self._group_elements_id

    @group_elements_id.setter
    def group_elements_id(self, group_elements_id):
        """Sets the group_elements_id of this SlideGraphics.


        :param group_elements_id: The group_elements_id of this SlideGraphics.  # noqa: E501
        :type: str
        """

        self._group_elements_id = group_elements_id

    @property
    def ooxml_id(self):
        """Gets the ooxml_id of this SlideGraphics.  # noqa: E501


        :return: The ooxml_id of this SlideGraphics.  # noqa: E501
        :rtype: int
        """
        return self._ooxml_id

    @ooxml_id.setter
    def ooxml_id(self, ooxml_id):
        """Sets the ooxml_id of this SlideGraphics.


        :param ooxml_id: The ooxml_id of this SlideGraphics.  # noqa: E501
        :type: int
        """

        self._ooxml_id = ooxml_id

    @property
    def graphic_type_id(self):
        """Gets the graphic_type_id of this SlideGraphics.  # noqa: E501


        :return: The graphic_type_id of this SlideGraphics.  # noqa: E501
        :rtype: int
        """
        return self._graphic_type_id

    @graphic_type_id.setter
    def graphic_type_id(self, graphic_type_id):
        """Sets the graphic_type_id of this SlideGraphics.


        :param graphic_type_id: The graphic_type_id of this SlideGraphics.  # noqa: E501
        :type: int
        """

        self._graphic_type_id = graphic_type_id

    @property
    def height(self):
        """Gets the height of this SlideGraphics.  # noqa: E501


        :return: The height of this SlideGraphics.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this SlideGraphics.


        :param height: The height of this SlideGraphics.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def width(self):
        """Gets the width of this SlideGraphics.  # noqa: E501


        :return: The width of this SlideGraphics.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this SlideGraphics.


        :param width: The width of this SlideGraphics.  # noqa: E501
        :type: int
        """

        self._width = width

    @property
    def x_offset(self):
        """Gets the x_offset of this SlideGraphics.  # noqa: E501


        :return: The x_offset of this SlideGraphics.  # noqa: E501
        :rtype: int
        """
        return self._x_offset

    @x_offset.setter
    def x_offset(self, x_offset):
        """Sets the x_offset of this SlideGraphics.


        :param x_offset: The x_offset of this SlideGraphics.  # noqa: E501
        :type: int
        """

        self._x_offset = x_offset

    @property
    def y_offset(self):
        """Gets the y_offset of this SlideGraphics.  # noqa: E501


        :return: The y_offset of this SlideGraphics.  # noqa: E501
        :rtype: int
        """
        return self._y_offset

    @y_offset.setter
    def y_offset(self, y_offset):
        """Sets the y_offset of this SlideGraphics.


        :param y_offset: The y_offset of this SlideGraphics.  # noqa: E501
        :type: int
        """

        self._y_offset = y_offset

    @property
    def id(self):
        """Gets the id of this SlideGraphics.  # noqa: E501


        :return: The id of this SlideGraphics.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SlideGraphics.


        :param id: The id of this SlideGraphics.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def date_created(self):
        """Gets the date_created of this SlideGraphics.  # noqa: E501


        :return: The date_created of this SlideGraphics.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this SlideGraphics.


        :param date_created: The date_created of this SlideGraphics.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def user_created(self):
        """Gets the user_created of this SlideGraphics.  # noqa: E501


        :return: The user_created of this SlideGraphics.  # noqa: E501
        :rtype: str
        """
        return self._user_created

    @user_created.setter
    def user_created(self, user_created):
        """Sets the user_created of this SlideGraphics.


        :param user_created: The user_created of this SlideGraphics.  # noqa: E501
        :type: str
        """

        self._user_created = user_created

    @property
    def date_modified(self):
        """Gets the date_modified of this SlideGraphics.  # noqa: E501


        :return: The date_modified of this SlideGraphics.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this SlideGraphics.


        :param date_modified: The date_modified of this SlideGraphics.  # noqa: E501
        :type: datetime
        """

        self._date_modified = date_modified

    @property
    def user_modified(self):
        """Gets the user_modified of this SlideGraphics.  # noqa: E501


        :return: The user_modified of this SlideGraphics.  # noqa: E501
        :rtype: str
        """
        return self._user_modified

    @user_modified.setter
    def user_modified(self, user_modified):
        """Sets the user_modified of this SlideGraphics.


        :param user_modified: The user_modified of this SlideGraphics.  # noqa: E501
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
        if not isinstance(other, SlideGraphics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
