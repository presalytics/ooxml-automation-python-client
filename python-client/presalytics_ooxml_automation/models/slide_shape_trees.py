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


class SlideShapeTrees(object):
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
        'slide_id': 'int',
        'elements': 'str',
        'group_element_id': 'int',
        'name': 'str',
        'hidden': 'bool',
        'title': 'str',
        'ooxml_id': 'int',
        'svg_blob_location': 'str',
        'oo_xml_blob_url': 'str',
        'id': 'int',
        'date_created': 'datetime',
        'user_created': 'str',
        'date_modified': 'datetime',
        'user_modified': 'str'
    }

    attribute_map = {
        'slide_id': 'SlideId',
        'elements': 'Elements',
        'group_element_id': 'GroupElementId',
        'name': 'Name',
        'hidden': 'Hidden',
        'title': 'Title',
        'ooxml_id': 'OoxmlId',
        'svg_blob_location': 'SvgBlobLocation',
        'oo_xml_blob_url': 'OoXmlBlobUrl',
        'id': 'Id',
        'date_created': 'DateCreated',
        'user_created': 'UserCreated',
        'date_modified': 'DateModified',
        'user_modified': 'UserModified'
    }

    def __init__(self, slide_id=None, elements=None, group_element_id=None, name=None, hidden=None, title=None, ooxml_id=None, svg_blob_location=None, oo_xml_blob_url=None, id=None, date_created=None, user_created=None, date_modified=None, user_modified=None):  # noqa: E501
        """SlideShapeTrees - a model defined in OpenAPI"""  # noqa: E501

        self._slide_id = None
        self._elements = None
        self._group_element_id = None
        self._name = None
        self._hidden = None
        self._title = None
        self._ooxml_id = None
        self._svg_blob_location = None
        self._oo_xml_blob_url = None
        self._id = None
        self._date_created = None
        self._user_created = None
        self._date_modified = None
        self._user_modified = None
        self.discriminator = None

        if slide_id is not None:
            self.slide_id = slide_id
        if elements is not None:
            self.elements = elements
        if group_element_id is not None:
            self.group_element_id = group_element_id
        if name is not None:
            self.name = name
        if hidden is not None:
            self.hidden = hidden
        if title is not None:
            self.title = title
        if ooxml_id is not None:
            self.ooxml_id = ooxml_id
        if svg_blob_location is not None:
            self.svg_blob_location = svg_blob_location
        if oo_xml_blob_url is not None:
            self.oo_xml_blob_url = oo_xml_blob_url
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
    def slide_id(self):
        """Gets the slide_id of this SlideShapeTrees.  # noqa: E501


        :return: The slide_id of this SlideShapeTrees.  # noqa: E501
        :rtype: int
        """
        return self._slide_id

    @slide_id.setter
    def slide_id(self, slide_id):
        """Sets the slide_id of this SlideShapeTrees.


        :param slide_id: The slide_id of this SlideShapeTrees.  # noqa: E501
        :type: int
        """

        self._slide_id = slide_id

    @property
    def elements(self):
        """Gets the elements of this SlideShapeTrees.  # noqa: E501


        :return: The elements of this SlideShapeTrees.  # noqa: E501
        :rtype: str
        """
        return self._elements

    @elements.setter
    def elements(self, elements):
        """Sets the elements of this SlideShapeTrees.


        :param elements: The elements of this SlideShapeTrees.  # noqa: E501
        :type: str
        """

        self._elements = elements

    @property
    def group_element_id(self):
        """Gets the group_element_id of this SlideShapeTrees.  # noqa: E501


        :return: The group_element_id of this SlideShapeTrees.  # noqa: E501
        :rtype: int
        """
        return self._group_element_id

    @group_element_id.setter
    def group_element_id(self, group_element_id):
        """Sets the group_element_id of this SlideShapeTrees.


        :param group_element_id: The group_element_id of this SlideShapeTrees.  # noqa: E501
        :type: int
        """

        self._group_element_id = group_element_id

    @property
    def name(self):
        """Gets the name of this SlideShapeTrees.  # noqa: E501


        :return: The name of this SlideShapeTrees.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SlideShapeTrees.


        :param name: The name of this SlideShapeTrees.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def hidden(self):
        """Gets the hidden of this SlideShapeTrees.  # noqa: E501


        :return: The hidden of this SlideShapeTrees.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this SlideShapeTrees.


        :param hidden: The hidden of this SlideShapeTrees.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def title(self):
        """Gets the title of this SlideShapeTrees.  # noqa: E501


        :return: The title of this SlideShapeTrees.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this SlideShapeTrees.


        :param title: The title of this SlideShapeTrees.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def ooxml_id(self):
        """Gets the ooxml_id of this SlideShapeTrees.  # noqa: E501


        :return: The ooxml_id of this SlideShapeTrees.  # noqa: E501
        :rtype: int
        """
        return self._ooxml_id

    @ooxml_id.setter
    def ooxml_id(self, ooxml_id):
        """Sets the ooxml_id of this SlideShapeTrees.


        :param ooxml_id: The ooxml_id of this SlideShapeTrees.  # noqa: E501
        :type: int
        """

        self._ooxml_id = ooxml_id

    @property
    def svg_blob_location(self):
        """Gets the svg_blob_location of this SlideShapeTrees.  # noqa: E501


        :return: The svg_blob_location of this SlideShapeTrees.  # noqa: E501
        :rtype: str
        """
        return self._svg_blob_location

    @svg_blob_location.setter
    def svg_blob_location(self, svg_blob_location):
        """Sets the svg_blob_location of this SlideShapeTrees.


        :param svg_blob_location: The svg_blob_location of this SlideShapeTrees.  # noqa: E501
        :type: str
        """

        self._svg_blob_location = svg_blob_location

    @property
    def oo_xml_blob_url(self):
        """Gets the oo_xml_blob_url of this SlideShapeTrees.  # noqa: E501


        :return: The oo_xml_blob_url of this SlideShapeTrees.  # noqa: E501
        :rtype: str
        """
        return self._oo_xml_blob_url

    @oo_xml_blob_url.setter
    def oo_xml_blob_url(self, oo_xml_blob_url):
        """Sets the oo_xml_blob_url of this SlideShapeTrees.


        :param oo_xml_blob_url: The oo_xml_blob_url of this SlideShapeTrees.  # noqa: E501
        :type: str
        """

        self._oo_xml_blob_url = oo_xml_blob_url

    @property
    def id(self):
        """Gets the id of this SlideShapeTrees.  # noqa: E501


        :return: The id of this SlideShapeTrees.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SlideShapeTrees.


        :param id: The id of this SlideShapeTrees.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def date_created(self):
        """Gets the date_created of this SlideShapeTrees.  # noqa: E501


        :return: The date_created of this SlideShapeTrees.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this SlideShapeTrees.


        :param date_created: The date_created of this SlideShapeTrees.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def user_created(self):
        """Gets the user_created of this SlideShapeTrees.  # noqa: E501


        :return: The user_created of this SlideShapeTrees.  # noqa: E501
        :rtype: str
        """
        return self._user_created

    @user_created.setter
    def user_created(self, user_created):
        """Sets the user_created of this SlideShapeTrees.


        :param user_created: The user_created of this SlideShapeTrees.  # noqa: E501
        :type: str
        """

        self._user_created = user_created

    @property
    def date_modified(self):
        """Gets the date_modified of this SlideShapeTrees.  # noqa: E501


        :return: The date_modified of this SlideShapeTrees.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this SlideShapeTrees.


        :param date_modified: The date_modified of this SlideShapeTrees.  # noqa: E501
        :type: datetime
        """

        self._date_modified = date_modified

    @property
    def user_modified(self):
        """Gets the user_modified of this SlideShapeTrees.  # noqa: E501


        :return: The user_modified of this SlideShapeTrees.  # noqa: E501
        :rtype: str
        """
        return self._user_modified

    @user_modified.setter
    def user_modified(self, user_modified):
        """Sets the user_modified of this SlideShapeTrees.


        :param user_modified: The user_modified of this SlideShapeTrees.  # noqa: E501
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
        if not isinstance(other, SlideShapeTrees):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
