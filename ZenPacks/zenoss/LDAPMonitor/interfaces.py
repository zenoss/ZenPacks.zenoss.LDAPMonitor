###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2010, Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 as published by
# the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################
from Products.Zuul.interfaces import IRRDDataSourceInfo
from Products.Zuul.form import schema
from Products.Zuul.utils import ZuulMessageFactory as _t


class ILDAPMonitorDataSourceInfo(IRRDDataSourceInfo):
    cycletime = schema.Int(title=_t(u'Cycle Time (seconds)'))
    timeout = schema.Int(title=_t(u'Timeout (seconds)'))
    ldapServer = schema.Text(title=_t(u'LDAP Server'), group=_t(u'LDAP'))
    ldapBindDN = schema.Text(title=_t(u'Bind Distinguished Name'), group=_t(u'LDAP'))
    useSSL = schema.Bool(title=_t(u'Use SSL?'), group=_t(u'LDAP'))
    ldapBaseDN = schema.Text(title=_t(u'Base Distinguished Name'), group=_t(u'LDAP'))
    ldapBindVersion = schema.Text(title=_t(u'Bind Version'), group=_t(u'LDAP'))
    ldapBindPassword = schema.Password(title=_t(u'Bind Password'), group=_t(u'LDAP'))
    port = schema.Int(title=_t(u'Port'), group=_t(u'LDAP'))
    
    

