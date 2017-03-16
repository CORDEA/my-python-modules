##!/usr/bin/env python
# encoding:utf-8
#
# Copyright [2014] [Yoshihiro Tanaka]
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
__date__   =  "2015-01-13"

import smtplib
from email.mime.text import MIMEText

def sendMail(sub, msg, address):
    From    = "your gmail address"
    To      = address
    Subject = sub
    Message = msg

    msg  = MIMEText(Message)
    msg['Subject'] = Subject
    msg['From']    = From
    msg['To']      = To

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(From, "your gmail password")
    s.sendmail(From, To, msg.as_string())
    s.close()
