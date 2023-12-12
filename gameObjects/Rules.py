from rulesData.defaultRules import defaultRules

class Rules:

    def __init__(self):
        default = defaultRules
        self.setRules(default)

    def setRules(self, rules):
        for key, value in vars(rules).items():
            if key.startswith('__'):
                continue
            else:
                setattr(self, key, value)





