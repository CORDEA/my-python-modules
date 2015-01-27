#!/usr/bin/env python
# encoding:utf-8
#
# Copyright [2015] [Yoshihiro Tanaka]
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

__Author__ =  "Yoshihiro Tanaka"
__date__   =  "2015-01-27"

import json
import urllib, urllib2

def getTags(apikey, query, page=1):
    #ref. http://docs.python.jp/2/howto/urllib2.html 
    url   = 'https://api.flickr.com/services/rest/'

    params = {
        'method': 'flickr.photos.search',
        'api_key': key,
        'text': query,
        'tags': query,
        'per_page': str(page),
        'format': 'json',
        'nojsoncallback': '1'
        }
    url_values = urllib.urlencode(params)
    full_url = url + '?' + url_values

    jsondata = urllib2.urlopen(full_url)
    data     = json.load(jsondata)["photos"]["photo"][0]

    _farm   = data["farm"]
    _server = data["server"]
    _secret = data["secret"]
    _id     = data["id"]
    return {"farm": _farm,
            "server": _server,
            "secret": _secret,
            "id": _id}
