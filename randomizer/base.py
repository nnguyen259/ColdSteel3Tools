class BaseRandomizer():
    def __init__(self, projectName=None, seed=None, programMode=True) -> None:
        self.seed = seed

        if programMode:
            self.inputPath = f'projects/{projectName}/tmp/text/'
        else:
            self.inputPath = f'projects/{projectName}/text/'