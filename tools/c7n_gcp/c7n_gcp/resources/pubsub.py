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
from c7n_gcp.provider import resources
from c7n_gcp.query import QueryResourceManager, TypeInfo

"""
todo, needs detail_spec
"""


@resources.register('pubsub-topic')
class PubSubTopic(QueryResourceManager):

    class resource_type(TypeInfo):
        service = 'pubsub'
        version = 'v1'
        component = 'projects.topics'
        enum_spec = ('list', 'topics[]', None)
        scope_template = "projects/{}"
        id = "name"

        @staticmethod
        def get(client, resource_info):
            return client.execute_command(
                'get', {'topic': resource_info['topic_id']})


@resources.register('pubsub-subscription')
class PubSubSubscription(QueryResourceManager):

    class resource_type(TypeInfo):
        service = 'pubsub'
        version = 'v1'
        component = 'projects.subscriptions'
        enum_spec = ('list', 'subscriptions[]', None)
        scope_template = 'projects/{}'
        id = 'name'

        @staticmethod
        def get(client, resource_info):
            return client.execute_command(
                'get', {'subscription': resource_info['name']})


@resources.register('pubsub-snapshot')
class PubSubSnapshot(QueryResourceManager):
    class resource_type(TypeInfo):
        service = 'pubsub'
        version = 'v1'
        component = 'projects.snapshots'
        enum_spec = ('list', 'snapshots[]', None)
        scope_template = 'projects/{}'
        id = 'name'
