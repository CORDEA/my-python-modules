#!/usr/bin/env python
# encoding:utf-8
#
# Copyright 2015-2017 Yoshihiro Tanaka
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__Author__ = "Yoshihiro Tanaka"
__date__ = "2015-01-30"

import json
import urllib, urllib2, base64


def getImageUrl(apikey, query, count=1):
    url = 'https://api.datamarket.azure.com/Bing/Search/v1/Image'
    params = {'$format': 'json', 'Query': "'%s'" % query, 'Adult': "'Strict'"}

    url_values = urllib.urlencode(params)
    full_url = url + '?' + url_values
    u""" Basic Authentication

    ref. http://www.voidspace.org.uk/python/articles/authentication.shtml
    ref. http://www.guguncube.com/2771/python-using-the-bing-search-api
    """

    base64string = (':%s' % (apikey)).encode('base64')[:-1]

    request = urllib2.Request(full_url)
    request.add_header('Authorization', 'Basic ' + base64string)

    jsondata = urllib2.urlopen(request)
    data = json.load(jsondata)['d']['results']

    returnList = []
    for i in range(count):
        returnList.append(data[i]['MediaUrl'])
    return returnList
