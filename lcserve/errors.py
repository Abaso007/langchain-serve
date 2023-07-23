class InvalidInstanceError(ValueError):
    def __init__(self, instance):
        super().__init__(f"Invalid instance: {instance}")
        self.instance = instance


class InvalidAutoscaleMinError(ValueError):
    def __init__(self, min):
        super().__init__(f"Invalid autoscale.min: {min}")
        self.min = min


class InvalidAutoscaleMaxError(ValueError):
    def __init__(self, max):
        super().__init__(f"Invalid autoscale.max: {max}")
        self.max = max


class InvalidDiskSizeError(ValueError):
    def __init__(self, disk_size):
        super().__init__(f"Invalid disk size: {disk_size}")
        self.disk_size = disk_size
