# coding: utf-8

# flake8: noqa

"""
    OOXML Automation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0-no-tags
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "0.2.16"

# import apis into sdk package
from presalytics_ooxml_automation.api.default_api import DefaultApi

# import ApiClient
from presalytics_ooxml_automation.api_client import ApiClient
from presalytics_ooxml_automation.configuration import Configuration
from presalytics_ooxml_automation.exceptions import OpenApiException
from presalytics_ooxml_automation.exceptions import ApiTypeError
from presalytics_ooxml_automation.exceptions import ApiValueError
from presalytics_ooxml_automation.exceptions import ApiKeyError
from presalytics_ooxml_automation.exceptions import ApiException
# import models into sdk package
from presalytics_ooxml_automation.models.bad_request import BadRequest
from presalytics_ooxml_automation.models.chart_axes import ChartAxes
from presalytics_ooxml_automation.models.chart_axis_data_types import ChartAxisDataTypes
from presalytics_ooxml_automation.models.chart_chart_data import ChartChartData
from presalytics_ooxml_automation.models.chart_charts import ChartCharts
from presalytics_ooxml_automation.models.chart_column_collections import ChartColumnCollections
from presalytics_ooxml_automation.models.chart_columns import ChartColumns
from presalytics_ooxml_automation.models.chart_data_points import ChartDataPoints
from presalytics_ooxml_automation.models.chart_plot_type import ChartPlotType
from presalytics_ooxml_automation.models.chart_row_col import ChartRowCol
from presalytics_ooxml_automation.models.chart_row_collections import ChartRowCollections
from presalytics_ooxml_automation.models.chart_row_name_format_types import ChartRowNameFormatTypes
from presalytics_ooxml_automation.models.chart_rows import ChartRows
from presalytics_ooxml_automation.models.document_type import DocumentType
from presalytics_ooxml_automation.models.shared_color_transformation_attributes import SharedColorTransformationAttributes
from presalytics_ooxml_automation.models.shared_color_transformations import SharedColorTransformations
from presalytics_ooxml_automation.models.shared_color_types import SharedColorTypes
from presalytics_ooxml_automation.models.shared_dash_types import SharedDashTypes
from presalytics_ooxml_automation.models.shared_effect_attributes import SharedEffectAttributes
from presalytics_ooxml_automation.models.shared_effect_types import SharedEffectTypes
from presalytics_ooxml_automation.models.shared_effects import SharedEffects
from presalytics_ooxml_automation.models.shared_fill_map import SharedFillMap
from presalytics_ooxml_automation.models.shared_fill_types import SharedFillTypes
from presalytics_ooxml_automation.models.shared_gradient_fills import SharedGradientFills
from presalytics_ooxml_automation.models.shared_gradient_stops import SharedGradientStops
from presalytics_ooxml_automation.models.shared_image_fills import SharedImageFills
from presalytics_ooxml_automation.models.shared_line_end_sizes import SharedLineEndSizes
from presalytics_ooxml_automation.models.shared_line_end_types import SharedLineEndTypes
from presalytics_ooxml_automation.models.shared_lines import SharedLines
from presalytics_ooxml_automation.models.shared_paragraph import SharedParagraph
from presalytics_ooxml_automation.models.shared_pictures import SharedPictures
from presalytics_ooxml_automation.models.shared_solid_fills import SharedSolidFills
from presalytics_ooxml_automation.models.shared_text import SharedText
from presalytics_ooxml_automation.models.shared_text_container import SharedTextContainer
from presalytics_ooxml_automation.models.slide_color_maps import SlideColorMaps
from presalytics_ooxml_automation.models.slide_graphic_types import SlideGraphicTypes
from presalytics_ooxml_automation.models.slide_graphics import SlideGraphics
from presalytics_ooxml_automation.models.slide_group_element_types import SlideGroupElementTypes
from presalytics_ooxml_automation.models.slide_group_elements import SlideGroupElements
from presalytics_ooxml_automation.models.slide_groups import SlideGroups
from presalytics_ooxml_automation.models.slide_shape_trees import SlideShapeTrees
from presalytics_ooxml_automation.models.slide_slide_masters import SlideSlideMasters
from presalytics_ooxml_automation.models.slide_slides import SlideSlides
from presalytics_ooxml_automation.models.table_borders import TableBorders
from presalytics_ooxml_automation.models.table_cells import TableCells
from presalytics_ooxml_automation.models.table_columns import TableColumns
from presalytics_ooxml_automation.models.table_rows import TableRows
from presalytics_ooxml_automation.models.table_tables import TableTables
from presalytics_ooxml_automation.models.theme_background_fills import ThemeBackgroundFills
from presalytics_ooxml_automation.models.theme_colors import ThemeColors
from presalytics_ooxml_automation.models.theme_custom_colors import ThemeCustomColors
from presalytics_ooxml_automation.models.theme_effect_map import ThemeEffectMap
from presalytics_ooxml_automation.models.theme_fills import ThemeFills
from presalytics_ooxml_automation.models.theme_fonts import ThemeFonts
from presalytics_ooxml_automation.models.theme_intensity import ThemeIntensity
from presalytics_ooxml_automation.models.theme_line_map import ThemeLineMap
from presalytics_ooxml_automation.models.theme_themes import ThemeThemes

