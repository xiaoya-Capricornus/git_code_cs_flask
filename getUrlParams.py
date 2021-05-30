#!/usr/bin/env python
# -*- coding: utf-8 -*-
import readConfig

READ_CONFIG = readConfig.ReadConfig()

class GetUrlParams():
    def get_url(self):
        new_url = READ_CONFIG.get_http('scheme') + '://' + READ_CONFIG.get_http('baseurl') + ':' + READ_CONFIG.get_http('port') + '/login'
        return new_url

if __name__ == '__main__':
    new_url = GetUrlParams().get_url()
    print(new_url)




