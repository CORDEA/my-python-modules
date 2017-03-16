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
__date__ = "2015-02-02"


def progress(sent, flag):
    import sys, commands

    _SUC = '[SUCCEED]'
    _FAL = '[FAILED]'

    # ref. http://d.hatena.ne.jp/heavenshell/20090909/1252509749
    colors = {'clear': '\033[0m', 'red': '\033[31m', 'green': '\033[32m'}

    width = int(commands.getoutput('stty size').split()[1])

    if flag:
        result = _SUC
        color = 'green'
    else:
        result = _FAL
        color = 'red'

    spaces = width - (len(sent) + len(result))

    sys.stdout.write('%s%s' % (colors['clear'], sent + (' ' * spaces)))
    sys.stdout.write('%s%s%s\n' % (colors[color], result, colors['clear']))
