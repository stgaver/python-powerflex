# Copyright (c) 2022 Dell Inc. or its subsidiaries.
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from PyPowerFlex import exceptions
from PyPowerFlex.objects import utility
import tests


class TestPowerFlexUtility(tests.PyPowerFlexTestCase):
    def setUp(self):
        super(TestPowerFlexUtility, self).setUp()
        self.client.initialize()

        self.MOCK_RESPONSES = {
            self.RESPONSE_MODE.Valid: {
                '/types/StoragePool/instances/action/querySelectedStatistics':
                    {},
                '/types/Volume/instances/action/querySelectedStatistics':
                    {},
            }
        }

    def test_get_statistics_for_all_storagepools(self):
        self.client.utility.get_statistics_for_all_storagepools()

    def test_get_statistics_for_all_storagepools_bad_status(self):
        with self.http_response_mode(self.RESPONSE_MODE.BadStatus):
            self.assertRaises(exceptions.PowerFlexClientException,
                              self.client.utility.get_statistics_for_all_storagepools)

    def test_get_statistics_for_all_volumes(self):
        self.client.utility.get_statistics_for_all_volumes()

    def test_get_statistics_for_all_volumes_bad_status(self):
        with self.http_response_mode(self.RESPONSE_MODE.BadStatus):
            self.assertRaises(exceptions.PowerFlexClientException,
                              self.client.utility.get_statistics_for_all_volumes)
