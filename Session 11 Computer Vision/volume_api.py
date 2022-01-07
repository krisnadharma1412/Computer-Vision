from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER

class VolumeApi:
    def __init__(self):
        self.vol_obj = self.CreateVolumeInstance()

    def CreateVolumeInstance(self):
        audio_util = AudioUtilities.GetSpeakers()

        audio_interface = audio_util.Activate(
            IAudioEndpointVolume._iid_,
            CLSCTX_ALL, None
        )

        return cast(audio_interface, POINTER(IAudioEndpointVolume))

    def RetrieveVolumeRange(self):
        minVol, maxVol, _ = self.vol_obj.GetVolumeRange()
        return minVol, maxVol

if __name__ == '__main__':
    vol_api = VolumeApi()
    minVol, maxVol = vol_api.RetrieveVolumeRange()
    print(minVol, maxVol)
