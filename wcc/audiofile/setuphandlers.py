from collective.grok import gs
from wcc.audiofile import MessageFactory as _

@gs.importstep(
    name=u'wcc.audiofile', 
    title=_('wcc.audiofile import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('wcc.audiofile.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
