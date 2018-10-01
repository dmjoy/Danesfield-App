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

from ..algorithms import segmentByHeight
from ..constants import DanesfieldStep
from ..workflow_step import DanesfieldWorkflowStep
from ..workflow_utilities import getOptions, getWorkingSet


class SegmentByHeightStep(DanesfieldWorkflowStep):
    """
    Step that runs segment by height.

    Supports the following options:
    - <none>
    """
    def __init__(self):
        super(SegmentByHeightStep, self).__init__(
            DanesfieldStep.SEGMENT_BY_HEIGHT)
        self.addDependency(DanesfieldStep.GENERATE_DSM)
        self.addDependency(DanesfieldStep.FIT_DTM)
        self.addDependency(DanesfieldStep.GET_ROAD_VECTOR)
        self.addDependency(DanesfieldStep.COMPUTE_NDVI)

    def run(self, jobInfo, outputFolder):
        # Get working sets
        initWorkingSet = getWorkingSet(DanesfieldStep.INIT, jobInfo)
        dsmWorkingSet = getWorkingSet(DanesfieldStep.GENERATE_DSM, jobInfo)
        dtmWorkingSet = getWorkingSet(DanesfieldStep.FIT_DTM, jobInfo)
        ndviWorkingSet = getWorkingSet(DanesfieldStep.COMPUTE_NDVI, jobInfo)
        getRoadVectorWorkingSet = getWorkingSet(
            DanesfieldStep.GET_ROAD_VECTOR,
            jobInfo)

        # Get DSM
        dsmFile = self.getSingleFile(dsmWorkingSet)

        # Get DTM
        dtmFile = self.getSingleFile(dtmWorkingSet)

        # Get Road Vector
        roadVectorFile = self.getSingleFile(
            getRoadVectorWorkingSet,
            lambda item: item['name'] == 'road_vector.geojson')

        # Get NDVI
        ndviFile = self.getSingleFile(ndviWorkingSet)

        # Get options
        segmentByHeightOptions = getOptions(self.name, jobInfo)

        # Run algorithm
        segmentByHeight(
            initWorkingSetName=initWorkingSet['name'],
            stepName=self.name,
            requestInfo=jobInfo.requestInfo,
            jobId=jobInfo.jobId,
            outputFolder=outputFolder,
            dsmFile=dsmFile,
            dtmFile=dtmFile,
            ndviFile=ndviFile,
            roadVectorFile=roadVectorFile,
            **segmentByHeightOptions)
