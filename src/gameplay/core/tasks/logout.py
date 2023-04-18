import numpy as np
from ..tasks.closeProcess import CloseProcessTask
from ..tasks.pauseBot import PauseBotTask
from ..tasks.pressLogoutKeys import PressLogoutKeys
from ..typings import Task
from .groupTaskExecutor import GroupTaskExecutor


class LogoutTask(GroupTaskExecutor):
    def __init__(self, context):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.name = 'logout'
        self.tasks = self.generateTasks(context)

    # TODO: add unit tests
    # TODO: add perf
    # TODO: add typings
    def generateTasks(self, context):
        return np.array([
            # ('pauseBot', PauseBotTask()),
            ('pressKeys', PressLogoutKeys(['ctrl', 'q'])),
            ('closeProcess', CloseProcessTask())
        ], dtype=Task)
