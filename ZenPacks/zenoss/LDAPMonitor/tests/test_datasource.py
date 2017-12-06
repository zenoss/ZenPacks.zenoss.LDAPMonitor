##############################################################################
#
# Copyright (C) Zenoss, Inc. 2015, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################

from Products.ZenTestCase.BaseTestCase import BaseTestCase

from Products.ZenUtils.Utils import binPath

from ZenPacks.zenoss.LDAPMonitor.datasources.LDAPMonitorDataSource import LDAPMonitorDataSource

class TestLDAPMonitorDataSource(BaseTestCase):
    def test_getCommand(self):
        ds = LDAPMonitorDataSource(None)
        context = lambda: 0
        dev = lambda: 0
        dev.id = 'adsf'
        context.device = lambda: dev
        context.zCommandPath = 'adsf'
        context.zLDAPBaseDN = 'DN=base'
        context.zLDAPBindDN = 'DN=bind'
        context.zLDAPBindPassword = 'password'

        res = ds.getCommand(context)

        self.assertEquals(res, binPath('check_ldap') + 
            ' -H adsf -b DN=base -D "DN=bind" -P "password" --ver2 -p 389 -t 60'
        )
