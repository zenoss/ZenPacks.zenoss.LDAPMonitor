###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2009, Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version as published by
# the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################


import logging
log = logging.getLogger("zen.migrate")

import Globals
from Products.ZenModel.migrate.Migrate import Version
from Products.ZenModel.ZenPack import ZenPackMigration
from Products.ZenModel.migrate.MigrateUtils import migratePropertyType

class MigratePassword(ZenPackMigration):
    version = Version(1, 2, 0)

    def migrate(self, dmd):
        log.info("Migrating zLDAPBindPassword")
        migratePropertyType("zLDAPBindPassword", dmd, "string")
        
MigratePassword()
