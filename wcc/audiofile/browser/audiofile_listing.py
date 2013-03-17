from five import grok
from Products.ATContentTypes.interfaces.folder import IATFolder
from Products.ATContentTypes.interfaces.topic import IATTopic
from plone.app.collection.interfaces import ICollection

grok.templatedir('templates')

class AudioFileListing(grok.View):
    grok.context(IATFolder)
    grok.name('audiofile_listing')
    grok.template('audiofile_listing')

class CollectionAudioFileListing(AudioFileListing):
    grok.context(ICollection)

class TopicSongListing(AudioFileListing):
    grok.context(IATTopic)
