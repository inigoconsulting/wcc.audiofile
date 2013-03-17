from five import grok
from plone.directives import dexterity, form
from wcc.audiofile.content.audiofile import IAudioFile

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IAudioFile)
    grok.require('zope2.View')
    grok.template('audiofile_view')
    grok.name('view')

