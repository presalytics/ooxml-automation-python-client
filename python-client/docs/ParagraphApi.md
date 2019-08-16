# presalytics_ooxml_automation.ParagraphApi

All URIs are relative to *http://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**paragraph_get_id**](ParagraphApi.md#paragraph_get_id) | **GET** /shared/Paragraph/{id} | Paragraph: Get by Id


# **paragraph_get_id**
> SharedParagraph paragraph_get_id(id)

Paragraph: Get by Id

Get by Id: Use this method to retrieve a Paragraph object by its primary key (id)

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.ParagraphApi()
id = 56 # int | The primary key (Id) of the Paragraph object

try:
    # Paragraph: Get by Id
    api_response = api_instance.paragraph_get_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParagraphApi->paragraph_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The primary key (Id) of the Paragraph object | 

### Return type

[**SharedParagraph**](SharedParagraph.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

