'''
segment-context

generic tools for working with segments
'''
import idc,idautils

def getName(ea):
    return idc.SegName(ea)
def getRange(ea):
    return idc.GetSegmentAttr(ea, idc.SEGATTR_START), idc.GetSegmentAttr(ea, idc.SEGATTR_END)

def get(name):
    for x in idautils.Segments():
        if getName(x) == name:
            return x
        continue
    raise KeyError(name)