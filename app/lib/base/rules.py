import os


class RulesManager:
    def __init__(self, filesystem, rules_path):
        self.filesystem = filesystem
        self.rules_path = rules_path

    def get_rules(self):
        return self.filesystem.get_files(self.rules_path)

    def is_valid_rule(self, rule):
        rules = self.get_rules()
        if not type(rule) == list:
            return rule in rules
        else:
            for i in rule:
                name = i[i.rindex("/")+1:] if "/" in i else i
                if name not in rules:
                    return False
        return True

    def get_rule_path(self, rule):
        if not self.is_valid_rule(rule):
            return ''
        paths = []
        rules = self.get_rules()
        if not type(rule) == list:
            return rules[rule]['path']

        for i in rule:
            name = i[i.rindex("/") + 1:] if "/" in i else i
            paths.append(rules[name]['path'])
        return paths

    def get_names_from_path(self, path):
        names = []
        for rule in path:
            names.append(rule.replace(self.rules_path, '').lstrip(os.sep))
        return names
