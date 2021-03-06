#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt
from pisi.actionsapi import get, pisitools, shelltools

NoStrip = '/'


def setup():
    shelltools.system("ar xf teams_%s_amd64.deb" % get.srcVERSION())
    shelltools.system("tar xf data.tar.xz")


def install():
    pisitools.insinto("/", "usr")
