from zang.exceptions.zang_exception import ZangException
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from zang.domain.enums.recording_audio_direction import RecordingAudioDirection
from zang.domain.enums.recording_file_format import RecordingFileFormat
from zang.domain.enums.transcribe_quality import TranscribeQuality


from docs.examples.credentials import sid, authToken
url = 'https://api.zang.io/v2'

configuration = Configuration(sid, authToken, url=url)
recordingsConnector = ConnectorFactory(configuration).recordingsConnector

# record call
try:
    recording = recordingsConnector.recordCall(
        callSid='CallSid',
        record=True,
        direction=RecordingAudioDirection.OUT,
        timeLimit=1337,
        callbackUrl='webhookr.com/testtransc',
        fileFormat=RecordingFileFormat.WAV,
        trimSilence=True,
        transcribe=True,
        transcribeQuality=TranscribeQuality.HYBRID,
        transcribeCallback='webhookr.com/testtransc'),
    print("Recording!")
except ZangException as ze:
    print(ze)
