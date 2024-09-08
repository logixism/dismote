from pyaudiodevice import DefaultCommunicationPlayback, AudioCommon

volume_control = DefaultCommunicationPlayback()
device_control = AudioCommon()


def set_volume(level: int):
    return volume_control.set_volume(level)


def get_volume():
    return volume_control.get_volume()


def get_active_device_data():
    return device_control.get_default_device()


def set_active_device(device_id: str):
    return device_control.set_default_only_device_by_id(device_id)
