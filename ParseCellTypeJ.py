#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def ParseCellTypeJ(code, modeSystem):
    cellType = "Unknown"
    if code != '':
        if modeSystem == 'LTE FDD' or modeSystem == 'LTE TDD':
            if code == '0':
                cellType = 'PCell'
            elif code == '1':
                cellType = 'SCell 0'
            elif code == '2':
                cellType = 'SCell 1'
    return cellType

