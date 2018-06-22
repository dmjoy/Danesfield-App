#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
#  Copyright Kitware Inc.
#
#  Licensed under the Apache License, Version 2.0 ( the "License" );
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
##############################################################################


class DanesfieldJobKey(object):
    """
    Keys for metadata attached to Danesfield jobs and related objects.
    """
    API_URL = 'danesfieldJobUrl'
    ID = 'danesfieldJobId'
    SOURCE = 'danesfieldJobSource'
    TOKEN = 'danesfieldJobToken'
    TRIGGER = 'danesfieldJobTrigger'


class DockerImage(object):
    """
    Names of Docker images to run Danesfield algorithms.
    """
    DANESFIELD = 'core3d/danesfield'
    P3D = 'p3d_gw'