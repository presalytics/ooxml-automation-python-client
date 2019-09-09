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


class SharedText(object):
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
        'paragraph_id': 'str',
        'sequence': 'int',
        'raw_text': 'str',
        'color_solid_fills_id': 'str',
        'is_bold': 'bool',
        'is_italic': 'bool',
        'is_underline': 'bool',
        'font_size': 'int',
        'font': 'str',
        'is_theme_font': 'bool',
        'id': 'str',
        'date_created': 'datetime',
        'user_created': 'str',
        'date_modified': 'datetime',
        'user_modified': 'str'
    }

    attribute_map = {
        'paragraph_id': 'paragraphId',
        'sequence': 'sequence',
        'raw_text': 'rawText',
        'color_solid_fills_id': 'colorSolidFillsId',
        'is_bold': 'isBold',
        'is_italic': 'isItalic',
        'is_underline': 'isUnderline',
        'font_size': 'fontSize',
        'font': 'font',
        'is_theme_font': 'isThemeFont',
        'id': 'id',
        'date_created': 'dateCreated',
        'user_created': 'userCreated',
        'date_modified': 'dateModified',
        'user_modified': 'userModified'
    }

    def __init__(self, paragraph_id=None, sequence=None, raw_text=None, color_solid_fills_id=None, is_bold=None, is_italic=None, is_underline=None, font_size=None, font=None, is_theme_font=None, id=None, date_created=None, user_created=None, date_modified=None, user_modified=None):  # noqa: E501
        """SharedText - a model defined in OpenAPI"""  # noqa: E501

        self._paragraph_id = None
        self._sequence = None
        self._raw_text = None
        self._color_solid_fills_id = None
        self._is_bold = None
        self._is_italic = None
        self._is_underline = None
        self._font_size = None
        self._font = None
        self._is_theme_font = None
        self._id = None
        self._date_created = None
        self._user_created = None
        self._date_modified = None
        self._user_modified = None
        self.discriminator = None

        self.paragraph_id = paragraph_id
        if sequence is not None:
            self.sequence = sequence
        if raw_text is not None:
            self.raw_text = raw_text
        self.color_solid_fills_id = color_solid_fills_id
        if is_bold is not None:
            self.is_bold = is_bold
        if is_italic is not None:
            self.is_italic = is_italic
        if is_underline is not None:
            self.is_underline = is_underline
        self.font_size = font_size
        if font is not None:
            self.font = font
        if is_theme_font is not None:
            self.is_theme_font = is_theme_font
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
    def paragraph_id(self):
        """Gets the paragraph_id of this SharedText.  # noqa: E501


        :return: The paragraph_id of this SharedText.  # noqa: E501
        :rtype: str
        """
        return self._paragraph_id

    @paragraph_id.setter
    def paragraph_id(self, paragraph_id):
        """Sets the paragraph_id of this SharedText.


        :param paragraph_id: The paragraph_id of this SharedText.  # noqa: E501
        :type: str
        """

        self._paragraph_id = paragraph_id

    @property
    def sequence(self):
        """Gets the sequence of this SharedText.  # noqa: E501


        :return: The sequence of this SharedText.  # noqa: E501
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this SharedText.


        :param sequence: The sequence of this SharedText.  # noqa: E501
        :type: int
        """

        self._sequence = sequence

    @property
    def raw_text(self):
        """Gets the raw_text of this SharedText.  # noqa: E501


        :return: The raw_text of this SharedText.  # noqa: E501
        :rtype: str
        """
        return self._raw_text

    @raw_text.setter
    def raw_text(self, raw_text):
        """Sets the raw_text of this SharedText.


        :param raw_text: The raw_text of this SharedText.  # noqa: E501
        :type: str
        """

        self._raw_text = raw_text

    @property
    def color_solid_fills_id(self):
        """Gets the color_solid_fills_id of this SharedText.  # noqa: E501


        :return: The color_solid_fills_id of this SharedText.  # noqa: E501
        :rtype: str
        """
        return self._color_solid_fills_id

    @color_solid_fills_id.setter
    def color_solid_fills_id(self, color_solid_fills_id):
        """Sets the color_solid_fills_id of this SharedText.


        :param color_solid_fills_id: The color_solid_fills_id of this SharedText.  # noqa: E501
        :type: str
        """

        self._color_solid_fills_id = color_solid_fills_id

    @property
    def is_bold(self):
        """Gets the is_bold of this SharedText.  # noqa: E501


        :return: The is_bold of this SharedText.  # noqa: E501
        :rtype: bool
        """
        return self._is_bold

    @is_bold.setter
    def is_bold(self, is_bold):
        """Sets the is_bold of this SharedText.


        :param is_bold: The is_bold of this SharedText.  # noqa: E501
        :type: bool
        """

        self._is_bold = is_bold

    @property
    def is_italic(self):
        """Gets the is_italic of this SharedText.  # noqa: E501


        :return: The is_italic of this SharedText.  # noqa: E501
        :rtype: bool
        """
        return self._is_italic

    @is_italic.setter
    def is_italic(self, is_italic):
        """Sets the is_italic of this SharedText.


        :param is_italic: The is_italic of this SharedText.  # noqa: E501
        :type: bool
        """

        self._is_italic = is_italic

    @property
    def is_underline(self):
        """Gets the is_underline of this SharedText.  # noqa: E501


        :return: The is_underline of this SharedText.  # noqa: E501
        :rtype: bool
        """
        return self._is_underline

    @is_underline.setter
    def is_underline(self, is_underline):
        """Sets the is_underline of this SharedText.


        :param is_underline: The is_underline of this SharedText.  # noqa: E501
        :type: bool
        """

        self._is_underline = is_underline

    @property
    def font_size(self):
        """Gets the font_size of this SharedText.  # noqa: E501


        :return: The font_size of this SharedText.  # noqa: E501
        :rtype: int
        """
        return self._font_size

    @font_size.setter
    def font_size(self, font_size):
        """Sets the font_size of this SharedText.


        :param font_size: The font_size of this SharedText.  # noqa: E501
        :type: int
        """

        self._font_size = font_size

    @property
    def font(self):
        """Gets the font of this SharedText.  # noqa: E501


        :return: The font of this SharedText.  # noqa: E501
        :rtype: str
        """
        return self._font

    @font.setter
    def font(self, font):
        """Sets the font of this SharedText.


        :param font: The font of this SharedText.  # noqa: E501
        :type: str
        """

        self._font = font

    @property
    def is_theme_font(self):
        """Gets the is_theme_font of this SharedText.  # noqa: E501


        :return: The is_theme_font of this SharedText.  # noqa: E501
        :rtype: bool
        """
        return self._is_theme_font

    @is_theme_font.setter
    def is_theme_font(self, is_theme_font):
        """Sets the is_theme_font of this SharedText.


        :param is_theme_font: The is_theme_font of this SharedText.  # noqa: E501
        :type: bool
        """

        self._is_theme_font = is_theme_font

    @property
    def id(self):
        """Gets the id of this SharedText.  # noqa: E501


        :return: The id of this SharedText.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SharedText.


        :param id: The id of this SharedText.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def date_created(self):
        """Gets the date_created of this SharedText.  # noqa: E501


        :return: The date_created of this SharedText.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this SharedText.


        :param date_created: The date_created of this SharedText.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def user_created(self):
        """Gets the user_created of this SharedText.  # noqa: E501


        :return: The user_created of this SharedText.  # noqa: E501
        :rtype: str
        """
        return self._user_created

    @user_created.setter
    def user_created(self, user_created):
        """Sets the user_created of this SharedText.


        :param user_created: The user_created of this SharedText.  # noqa: E501
        :type: str
        """

        self._user_created = user_created

    @property
    def date_modified(self):
        """Gets the date_modified of this SharedText.  # noqa: E501


        :return: The date_modified of this SharedText.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this SharedText.


        :param date_modified: The date_modified of this SharedText.  # noqa: E501
        :type: datetime
        """

        self._date_modified = date_modified

    @property
    def user_modified(self):
        """Gets the user_modified of this SharedText.  # noqa: E501


        :return: The user_modified of this SharedText.  # noqa: E501
        :rtype: str
        """
        return self._user_modified

    @user_modified.setter
    def user_modified(self, user_modified):
        """Sets the user_modified of this SharedText.


        :param user_modified: The user_modified of this SharedText.  # noqa: E501
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
        if not isinstance(other, SharedText):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
