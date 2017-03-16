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

__Author__ = "Yoshihiro Tanaka"
__date__ = "2015-02-10"

from requests_oauthlib import OAuth1Session
import sys


def post_twitter(keys, status):
    key, c_secret, token, t_secret = keys
    url = "https://api.twitter.com/1.1/statuses/update.json"

    params = {"status": status}

    twitter = OAuth1Session(key, c_secret, token, t_secret)
    request = twitter.post(url, params=params)

    if request.status_code != 200:
        sys.stderr.write(str(request.status_code) + '\n')
