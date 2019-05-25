# Copyright 2018 Capital One Services, LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging

from c7n_azure.filters import FirewallRulesFilter
from c7n_azure.provider import resources
from c7n_azure.resources.arm import ArmResourceManager
from netaddr import IPRange


@resources.register('sqlserver')
class SqlServer(ArmResourceManager):

    class resource_type(ArmResourceManager.resource_type):
        service = 'azure.mgmt.sql'
        client = 'SqlManagementClient'
        enum_spec = ('servers', 'list', None)


@SqlServer.filter_registry.register('firewall-rules')
class SqlServerFirewallRulesFilter(FirewallRulesFilter):

    def __init__(self, data, manager=None):
        super(SqlServerFirewallRulesFilter, self).__init__(data, manager)
        self._log = logging.getLogger('custodian.azure.sqlserver')
        self.client = None

    @property
    def log(self):
        return self._log

    def process(self, resources, event=None):
        self.client = self.manager.get_client()
        return super(SqlServerFirewallRulesFilter, self).process(resources, event)

    def _query_rules(self, resource):
        query = self.client.firewall_rules.list_by_server(
            resource['resourceGroup'],
            resource['name'])

        resource_rules = set([IPRange(r.start_ip_address, r.end_ip_address) for r in query])

        return resource_rules
