# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.desktopvirtualization.aio import DesktopVirtualizationMgmtClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDesktopVirtualizationMgmtScalingPlanPersonalSchedulesOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(DesktopVirtualizationMgmtClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get(self, resource_group):
        response = await self.client.scaling_plan_personal_schedules.get(
            resource_group_name=resource_group.name,
            scaling_plan_name="str",
            scaling_plan_schedule_name="str",
            api_version="2024-04-03",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_create(self, resource_group):
        response = await self.client.scaling_plan_personal_schedules.create(
            resource_group_name=resource_group.name,
            scaling_plan_name="str",
            scaling_plan_schedule_name="str",
            scaling_plan_schedule={
                "daysOfWeek": ["str"],
                "id": "str",
                "name": "str",
                "offPeakActionOnDisconnect": "str",
                "offPeakActionOnLogoff": "str",
                "offPeakMinutesToWaitOnDisconnect": 0,
                "offPeakMinutesToWaitOnLogoff": 0,
                "offPeakStartTime": {"hour": 0, "minute": 0},
                "offPeakStartVMOnConnect": "str",
                "peakActionOnDisconnect": "str",
                "peakActionOnLogoff": "str",
                "peakMinutesToWaitOnDisconnect": 0,
                "peakMinutesToWaitOnLogoff": 0,
                "peakStartTime": {"hour": 0, "minute": 0},
                "peakStartVMOnConnect": "str",
                "rampDownActionOnDisconnect": "str",
                "rampDownActionOnLogoff": "str",
                "rampDownMinutesToWaitOnDisconnect": 0,
                "rampDownMinutesToWaitOnLogoff": 0,
                "rampDownStartTime": {"hour": 0, "minute": 0},
                "rampDownStartVMOnConnect": "str",
                "rampUpActionOnDisconnect": "str",
                "rampUpActionOnLogoff": "str",
                "rampUpAutoStartHosts": "str",
                "rampUpMinutesToWaitOnDisconnect": 0,
                "rampUpMinutesToWaitOnLogoff": 0,
                "rampUpStartTime": {"hour": 0, "minute": 0},
                "rampUpStartVMOnConnect": "str",
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "type": "str",
            },
            api_version="2024-04-03",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_delete(self, resource_group):
        response = await self.client.scaling_plan_personal_schedules.delete(
            resource_group_name=resource_group.name,
            scaling_plan_name="str",
            scaling_plan_schedule_name="str",
            api_version="2024-04-03",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_update(self, resource_group):
        response = await self.client.scaling_plan_personal_schedules.update(
            resource_group_name=resource_group.name,
            scaling_plan_name="str",
            scaling_plan_schedule_name="str",
            api_version="2024-04-03",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list(self, resource_group):
        response = self.client.scaling_plan_personal_schedules.list(
            resource_group_name=resource_group.name,
            scaling_plan_name="str",
            api_version="2024-04-03",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
