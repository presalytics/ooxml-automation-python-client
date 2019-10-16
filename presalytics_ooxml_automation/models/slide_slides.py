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


class SlideSlides(object):
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
        'document_id': 'str',
        'document': 'Document',
        'slide_master': 'SlideSlideMasters',
        'number': 'int',
        'ooxml_id': 'int',
        'svg_blob_url': 'str',
        'slide_document_url': 'str',
        'theme': 'ThemeThemes',
        'shape_tree': 'SlideShapeTrees',
        'base_element_blob_url': 'str',
        'changed_base_element_blob_url': 'str',
        'package_uri': 'str',
        'id': 'str',
        'date_created': 'datetime',
        'user_created': 'str',
        'date_modified': 'datetime',
        'user_modified': 'str'
    }

    attribute_map = {
        'document_id': 'documentId',
        'document': 'document',
        'slide_master': 'slideMaster',
        'number': 'number',
        'ooxml_id': 'ooxmlId',
        'svg_blob_url': 'svgBlobUrl',
        'slide_document_url': 'slideDocumentUrl',
        'theme': 'theme',
        'shape_tree': 'shapeTree',
        'base_element_blob_url': 'baseElementBlobUrl',
        'changed_base_element_blob_url': 'changedBaseElementBlobUrl',
        'package_uri': 'packageUri',
        'id': 'id',
        'date_created': 'dateCreated',
        'user_created': 'userCreated',
        'date_modified': 'dateModified',
        'user_modified': 'userModified'
    }

    def __init__(self, document_id=None, document=None, slide_master=None, number=None, ooxml_id=None, svg_blob_url=None, slide_document_url=None, theme=None, shape_tree=None, base_element_blob_url=None, changed_base_element_blob_url=None, package_uri=None, id=None, date_created=None, user_created=None, date_modified=None, user_modified=None):  # noqa: E501
        """SlideSlides - a model defined in OpenAPI"""  # noqa: E501

        self._document_id = None
        self._document = None
        self._slide_master = None
        self._number = None
        self._ooxml_id = None
        self._svg_blob_url = None
        self._slide_document_url = None
        self._theme = None
        self._shape_tree = None
        self._base_element_blob_url = None
        self._changed_base_element_blob_url = None
        self._package_uri = None
        self._id = None
        self._date_created = None
        self._user_created = None
        self._date_modified = None
        self._user_modified = None
        self.discriminator = None

        self.document_id = document_id
        if document is not None:
            self.document = document
        if slide_master is not None:
            self.slide_master = slide_master
        if number is not None:
            self.number = number
        if ooxml_id is not None:
            self.ooxml_id = ooxml_id
        self.svg_blob_url = svg_blob_url
        self.slide_document_url = slide_document_url
        if theme is not None:
            self.theme = theme
        if shape_tree is not None:
            self.shape_tree = shape_tree
        self.base_element_blob_url = base_element_blob_url
        self.changed_base_element_blob_url = changed_base_element_blob_url
        self.package_uri = package_uri
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
    def document_id(self):
        """Gets the document_id of this SlideSlides.  # noqa: E501


        :return: The document_id of this SlideSlides.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this SlideSlides.


        :param document_id: The document_id of this SlideSlides.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def document(self):
        """Gets the document of this SlideSlides.  # noqa: E501


        :return: The document of this SlideSlides.  # noqa: E501
        :rtype: Document
        """
        return self._document

    @document.setter
    def document(self, document):
        """Sets the document of this SlideSlides.


        :param document: The document of this SlideSlides.  # noqa: E501
        :type: Document
        """

        self._document = document

    @property
    def slide_master(self):
        """Gets the slide_master of this SlideSlides.  # noqa: E501


        :return: The slide_master of this SlideSlides.  # noqa: E501
        :rtype: SlideSlideMasters
        """
        return self._slide_master

    @slide_master.setter
    def slide_master(self, slide_master):
        """Sets the slide_master of this SlideSlides.


        :param slide_master: The slide_master of this SlideSlides.  # noqa: E501
        :type: SlideSlideMasters
        """

        self._slide_master = slide_master

    @property
    def number(self):
        """Gets the number of this SlideSlides.  # noqa: E501


        :return: The number of this SlideSlides.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this SlideSlides.


        :param number: The number of this SlideSlides.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def ooxml_id(self):
        """Gets the ooxml_id of this SlideSlides.  # noqa: E501


        :return: The ooxml_id of this SlideSlides.  # noqa: E501
        :rtype: int
        """
        return self._ooxml_id

    @ooxml_id.setter
    def ooxml_id(self, ooxml_id):
        """Sets the ooxml_id of this SlideSlides.


        :param ooxml_id: The ooxml_id of this SlideSlides.  # noqa: E501
        :type: int
        """

        self._ooxml_id = ooxml_id

    @property
    def svg_blob_url(self):
        """Gets the svg_blob_url of this SlideSlides.  # noqa: E501


        :return: The svg_blob_url of this SlideSlides.  # noqa: E501
        :rtype: str
        """
        return self._svg_blob_url

    @svg_blob_url.setter
    def svg_blob_url(self, svg_blob_url):
        """Sets the svg_blob_url of this SlideSlides.


        :param svg_blob_url: The svg_blob_url of this SlideSlides.  # noqa: E501
        :type: str
        """

        self._svg_blob_url = svg_blob_url

    @property
    def slide_document_url(self):
        """Gets the slide_document_url of this SlideSlides.  # noqa: E501


        :return: The slide_document_url of this SlideSlides.  # noqa: E501
        :rtype: str
        """
        return self._slide_document_url

    @slide_document_url.setter
    def slide_document_url(self, slide_document_url):
        """Sets the slide_document_url of this SlideSlides.


        :param slide_document_url: The slide_document_url of this SlideSlides.  # noqa: E501
        :type: str
        """

        self._slide_document_url = slide_document_url

    @property
    def theme(self):
        """Gets the theme of this SlideSlides.  # noqa: E501


        :return: The theme of this SlideSlides.  # noqa: E501
        :rtype: ThemeThemes
        """
        return self._theme

    @theme.setter
    def theme(self, theme):
        """Sets the theme of this SlideSlides.


        :param theme: The theme of this SlideSlides.  # noqa: E501
        :type: ThemeThemes
        """

        self._theme = theme

    @property
    def shape_tree(self):
        """Gets the shape_tree of this SlideSlides.  # noqa: E501


        :return: The shape_tree of this SlideSlides.  # noqa: E501
        :rtype: SlideShapeTrees
        """
        return self._shape_tree

    @shape_tree.setter
    def shape_tree(self, shape_tree):
        """Sets the shape_tree of this SlideSlides.


        :param shape_tree: The shape_tree of this SlideSlides.  # noqa: E501
        :type: SlideShapeTrees
        """

        self._shape_tree = shape_tree

    @property
    def base_element_blob_url(self):
        """Gets the base_element_blob_url of this SlideSlides.  # noqa: E501


        :return: The base_element_blob_url of this SlideSlides.  # noqa: E501
        :rtype: str
        """
        return self._base_element_blob_url

    @base_element_blob_url.setter
    def base_element_blob_url(self, base_element_blob_url):
        """Sets the base_element_blob_url of this SlideSlides.


        :param base_element_blob_url: The base_element_blob_url of this SlideSlides.  # noqa: E501
        :type: str
        """

        self._base_element_blob_url = base_element_blob_url

    @property
    def changed_base_element_blob_url(self):
        """Gets the changed_base_element_blob_url of this SlideSlides.  # noqa: E501


        :return: The changed_base_element_blob_url of this SlideSlides.  # noqa: E501
        :rtype: str
        """
        return self._changed_base_element_blob_url

    @changed_base_element_blob_url.setter
    def changed_base_element_blob_url(self, changed_base_element_blob_url):
        """Sets the changed_base_element_blob_url of this SlideSlides.


        :param changed_base_element_blob_url: The changed_base_element_blob_url of this SlideSlides.  # noqa: E501
        :type: str
        """

        self._changed_base_element_blob_url = changed_base_element_blob_url

    @property
    def package_uri(self):
        """Gets the package_uri of this SlideSlides.  # noqa: E501


        :return: The package_uri of this SlideSlides.  # noqa: E501
        :rtype: str
        """
        return self._package_uri

    @package_uri.setter
    def package_uri(self, package_uri):
        """Sets the package_uri of this SlideSlides.


        :param package_uri: The package_uri of this SlideSlides.  # noqa: E501
        :type: str
        """

        self._package_uri = package_uri

    @property
    def id(self):
        """Gets the id of this SlideSlides.  # noqa: E501


        :return: The id of this SlideSlides.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SlideSlides.


        :param id: The id of this SlideSlides.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def date_created(self):
        """Gets the date_created of this SlideSlides.  # noqa: E501


        :return: The date_created of this SlideSlides.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this SlideSlides.


        :param date_created: The date_created of this SlideSlides.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def user_created(self):
        """Gets the user_created of this SlideSlides.  # noqa: E501


        :return: The user_created of this SlideSlides.  # noqa: E501
        :rtype: str
        """
        return self._user_created

    @user_created.setter
    def user_created(self, user_created):
        """Sets the user_created of this SlideSlides.


        :param user_created: The user_created of this SlideSlides.  # noqa: E501
        :type: str
        """

        self._user_created = user_created

    @property
    def date_modified(self):
        """Gets the date_modified of this SlideSlides.  # noqa: E501


        :return: The date_modified of this SlideSlides.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this SlideSlides.


        :param date_modified: The date_modified of this SlideSlides.  # noqa: E501
        :type: datetime
        """

        self._date_modified = date_modified

    @property
    def user_modified(self):
        """Gets the user_modified of this SlideSlides.  # noqa: E501


        :return: The user_modified of this SlideSlides.  # noqa: E501
        :rtype: str
        """
        return self._user_modified

    @user_modified.setter
    def user_modified(self, user_modified):
        """Sets the user_modified of this SlideSlides.


        :param user_modified: The user_modified of this SlideSlides.  # noqa: E501
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
        if not isinstance(other, SlideSlides):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other