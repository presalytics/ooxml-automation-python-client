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


class SlideColorMaps(object):
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
        'slide_master_id': 'str',
        'slide_master': 'object',
        'accent1': 'int',
        'accent2': 'int',
        'accent3': 'int',
        'accent4': 'int',
        'accent5': 'int',
        'accent6': 'int',
        'text1': 'int',
        'text2': 'int',
        'background1': 'int',
        'background2': 'int',
        'hyperlink': 'int',
        'followed_hyperlink': 'int',
        'id': 'str',
        'date_created': 'datetime',
        'user_created': 'str',
        'date_modified': 'datetime',
        'user_modified': 'str'
    }

    attribute_map = {
        'slide_master_id': 'slideMasterId',
        'slide_master': 'slideMaster',
        'accent1': 'accent1',
        'accent2': 'accent2',
        'accent3': 'accent3',
        'accent4': 'accent4',
        'accent5': 'accent5',
        'accent6': 'accent6',
        'text1': 'text1',
        'text2': 'text2',
        'background1': 'background1',
        'background2': 'background2',
        'hyperlink': 'hyperlink',
        'followed_hyperlink': 'followedHyperlink',
        'id': 'id',
        'date_created': 'dateCreated',
        'user_created': 'userCreated',
        'date_modified': 'dateModified',
        'user_modified': 'userModified'
    }

    def __init__(self, slide_master_id=None, slide_master=None, accent1=None, accent2=None, accent3=None, accent4=None, accent5=None, accent6=None, text1=None, text2=None, background1=None, background2=None, hyperlink=None, followed_hyperlink=None, id=None, date_created=None, user_created=None, date_modified=None, user_modified=None, local_vars_configuration=None):  # noqa: E501
        """SlideColorMaps - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._slide_master_id = None
        self._slide_master = None
        self._accent1 = None
        self._accent2 = None
        self._accent3 = None
        self._accent4 = None
        self._accent5 = None
        self._accent6 = None
        self._text1 = None
        self._text2 = None
        self._background1 = None
        self._background2 = None
        self._hyperlink = None
        self._followed_hyperlink = None
        self._id = None
        self._date_created = None
        self._user_created = None
        self._date_modified = None
        self._user_modified = None
        self.discriminator = None

        self.slide_master_id = slide_master_id
        if slide_master is not None:
            self.slide_master = slide_master
        if accent1 is not None:
            self.accent1 = accent1
        if accent2 is not None:
            self.accent2 = accent2
        if accent3 is not None:
            self.accent3 = accent3
        if accent4 is not None:
            self.accent4 = accent4
        if accent5 is not None:
            self.accent5 = accent5
        if accent6 is not None:
            self.accent6 = accent6
        if text1 is not None:
            self.text1 = text1
        if text2 is not None:
            self.text2 = text2
        if background1 is not None:
            self.background1 = background1
        if background2 is not None:
            self.background2 = background2
        if hyperlink is not None:
            self.hyperlink = hyperlink
        if followed_hyperlink is not None:
            self.followed_hyperlink = followed_hyperlink
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
    def slide_master_id(self):
        """Gets the slide_master_id of this SlideColorMaps.  # noqa: E501


        :return: The slide_master_id of this SlideColorMaps.  # noqa: E501
        :rtype: str
        """
        return self._slide_master_id

    @slide_master_id.setter
    def slide_master_id(self, slide_master_id):
        """Sets the slide_master_id of this SlideColorMaps.


        :param slide_master_id: The slide_master_id of this SlideColorMaps.  # noqa: E501
        :type: str
        """

        self._slide_master_id = slide_master_id

    @property
    def slide_master(self):
        """Gets the slide_master of this SlideColorMaps.  # noqa: E501


        :return: The slide_master of this SlideColorMaps.  # noqa: E501
        :rtype: object
        """
        return self._slide_master

    @slide_master.setter
    def slide_master(self, slide_master):
        """Sets the slide_master of this SlideColorMaps.


        :param slide_master: The slide_master of this SlideColorMaps.  # noqa: E501
        :type: object
        """

        self._slide_master = slide_master

    @property
    def accent1(self):
        """Gets the accent1 of this SlideColorMaps.  # noqa: E501


        :return: The accent1 of this SlideColorMaps.  # noqa: E501
        :rtype: int
        """
        return self._accent1

    @accent1.setter
    def accent1(self, accent1):
        """Sets the accent1 of this SlideColorMaps.


        :param accent1: The accent1 of this SlideColorMaps.  # noqa: E501
        :type: int
        """

        self._accent1 = accent1

    @property
    def accent2(self):
        """Gets the accent2 of this SlideColorMaps.  # noqa: E501


        :return: The accent2 of this SlideColorMaps.  # noqa: E501
        :rtype: int
        """
        return self._accent2

    @accent2.setter
    def accent2(self, accent2):
        """Sets the accent2 of this SlideColorMaps.


        :param accent2: The accent2 of this SlideColorMaps.  # noqa: E501
        :type: int
        """

        self._accent2 = accent2

    @property
    def accent3(self):
        """Gets the accent3 of this SlideColorMaps.  # noqa: E501


        :return: The accent3 of this SlideColorMaps.  # noqa: E501
        :rtype: int
        """
        return self._accent3

    @accent3.setter
    def accent3(self, accent3):
        """Sets the accent3 of this SlideColorMaps.


        :param accent3: The accent3 of this SlideColorMaps.  # noqa: E501
        :type: int
        """

        self._accent3 = accent3

    @property
    def accent4(self):
        """Gets the accent4 of this SlideColorMaps.  # noqa: E501


        :return: The accent4 of this SlideColorMaps.  # noqa: E501
        :rtype: int
        """
        return self._accent4

    @accent4.setter
    def accent4(self, accent4):
        """Sets the accent4 of this SlideColorMaps.


        :param accent4: The accent4 of this SlideColorMaps.  # noqa: E501
        :type: int
        """

        self._accent4 = accent4

    @property
    def accent5(self):
        """Gets the accent5 of this SlideColorMaps.  # noqa: E501


        :return: The accent5 of this SlideColorMaps.  # noqa: E501
        :rtype: int
        """
        return self._accent5

    @accent5.setter
    def accent5(self, accent5):
        """Sets the accent5 of this SlideColorMaps.


        :param accent5: The accent5 of this SlideColorMaps.  # noqa: E501
        :type: int
        """

        self._accent5 = accent5

    @property
    def accent6(self):
        """Gets the accent6 of this SlideColorMaps.  # noqa: E501


        :return: The accent6 of this SlideColorMaps.  # noqa: E501
        :rtype: int
        """
        return self._accent6

    @accent6.setter
    def accent6(self, accent6):
        """Sets the accent6 of this SlideColorMaps.


        :param accent6: The accent6 of this SlideColorMaps.  # noqa: E501
        :type: int
        """

        self._accent6 = accent6

    @property
    def text1(self):
        """Gets the text1 of this SlideColorMaps.  # noqa: E501


        :return: The text1 of this SlideColorMaps.  # noqa: E501
        :rtype: int
        """
        return self._text1

    @text1.setter
    def text1(self, text1):
        """Sets the text1 of this SlideColorMaps.


        :param text1: The text1 of this SlideColorMaps.  # noqa: E501
        :type: int
        """

        self._text1 = text1

    @property
    def text2(self):
        """Gets the text2 of this SlideColorMaps.  # noqa: E501


        :return: The text2 of this SlideColorMaps.  # noqa: E501
        :rtype: int
        """
        return self._text2

    @text2.setter
    def text2(self, text2):
        """Sets the text2 of this SlideColorMaps.


        :param text2: The text2 of this SlideColorMaps.  # noqa: E501
        :type: int
        """

        self._text2 = text2

    @property
    def background1(self):
        """Gets the background1 of this SlideColorMaps.  # noqa: E501


        :return: The background1 of this SlideColorMaps.  # noqa: E501
        :rtype: int
        """
        return self._background1

    @background1.setter
    def background1(self, background1):
        """Sets the background1 of this SlideColorMaps.


        :param background1: The background1 of this SlideColorMaps.  # noqa: E501
        :type: int
        """

        self._background1 = background1

    @property
    def background2(self):
        """Gets the background2 of this SlideColorMaps.  # noqa: E501


        :return: The background2 of this SlideColorMaps.  # noqa: E501
        :rtype: int
        """
        return self._background2

    @background2.setter
    def background2(self, background2):
        """Sets the background2 of this SlideColorMaps.


        :param background2: The background2 of this SlideColorMaps.  # noqa: E501
        :type: int
        """

        self._background2 = background2

    @property
    def hyperlink(self):
        """Gets the hyperlink of this SlideColorMaps.  # noqa: E501


        :return: The hyperlink of this SlideColorMaps.  # noqa: E501
        :rtype: int
        """
        return self._hyperlink

    @hyperlink.setter
    def hyperlink(self, hyperlink):
        """Sets the hyperlink of this SlideColorMaps.


        :param hyperlink: The hyperlink of this SlideColorMaps.  # noqa: E501
        :type: int
        """

        self._hyperlink = hyperlink

    @property
    def followed_hyperlink(self):
        """Gets the followed_hyperlink of this SlideColorMaps.  # noqa: E501


        :return: The followed_hyperlink of this SlideColorMaps.  # noqa: E501
        :rtype: int
        """
        return self._followed_hyperlink

    @followed_hyperlink.setter
    def followed_hyperlink(self, followed_hyperlink):
        """Sets the followed_hyperlink of this SlideColorMaps.


        :param followed_hyperlink: The followed_hyperlink of this SlideColorMaps.  # noqa: E501
        :type: int
        """

        self._followed_hyperlink = followed_hyperlink

    @property
    def id(self):
        """Gets the id of this SlideColorMaps.  # noqa: E501


        :return: The id of this SlideColorMaps.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SlideColorMaps.


        :param id: The id of this SlideColorMaps.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def date_created(self):
        """Gets the date_created of this SlideColorMaps.  # noqa: E501


        :return: The date_created of this SlideColorMaps.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this SlideColorMaps.


        :param date_created: The date_created of this SlideColorMaps.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def user_created(self):
        """Gets the user_created of this SlideColorMaps.  # noqa: E501


        :return: The user_created of this SlideColorMaps.  # noqa: E501
        :rtype: str
        """
        return self._user_created

    @user_created.setter
    def user_created(self, user_created):
        """Sets the user_created of this SlideColorMaps.


        :param user_created: The user_created of this SlideColorMaps.  # noqa: E501
        :type: str
        """

        self._user_created = user_created

    @property
    def date_modified(self):
        """Gets the date_modified of this SlideColorMaps.  # noqa: E501


        :return: The date_modified of this SlideColorMaps.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this SlideColorMaps.


        :param date_modified: The date_modified of this SlideColorMaps.  # noqa: E501
        :type: datetime
        """

        self._date_modified = date_modified

    @property
    def user_modified(self):
        """Gets the user_modified of this SlideColorMaps.  # noqa: E501


        :return: The user_modified of this SlideColorMaps.  # noqa: E501
        :rtype: str
        """
        return self._user_modified

    @user_modified.setter
    def user_modified(self, user_modified):
        """Sets the user_modified of this SlideColorMaps.


        :param user_modified: The user_modified of this SlideColorMaps.  # noqa: E501
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
        if not isinstance(other, SlideColorMaps):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SlideColorMaps):
            return True

        return self.to_dict() != other.to_dict()
