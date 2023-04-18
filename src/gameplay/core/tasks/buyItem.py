from src.features.refill.core import buyItem
from .baseTask import BaseTask


# TODO: check if item was bought
class BuyItemTask(BaseTask):
    def __init__(self, itemNameWithQuantity):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.name = 'buyItem'
        self.value = itemNameWithQuantity

    # TODO: add unit tests
    # TODO: add perf
    # TODO: add typings
    def shouldIgnore(self, _):
        _, itemQuantity = self.value
        ignore = itemQuantity <= 0
        return ignore

    # TODO: add unit tests
    # TODO: add perf
    # TODO: add typings
    def do(self, context):
        buyItem(context['screenshot'], self.value)
        return context
