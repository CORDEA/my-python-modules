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

from jinja2 import Environment, FileSystemLoader
from bing import bing
import sys

tmpldir = './'
env = Environment(
    loader=FileSystemLoader(tmpldir, encoding='utf-8'), autoescape=False)
tmpl = env.get_template('template.html')

key = "bing api key"

sp_dict = {}
with open(sys.argv[1]) as f:
    for line in f:
        species = line.rstrip()
        sp_dict[species] = bing.get_image_url(key, species)[0]

with open("result.html", 'w') as f:
    f.write(tmpl.render(species=sp_dict))
