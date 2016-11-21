import regex


class Tag:
    def __init__(self, tag_name, dom_id, classes):
        self.tag_name = tag_name
        self.dom_id = dom_id
        self.classes = classes

    def __eq__(self, other):
        return self.tag_name == other.tag_name \
               and self.dom_id == other.dom_id \
               and self.classes == other.classes

TAG_REGEX = r'(?P<name>\w+)(#(?P<id>\w+))?(\.(?P<classes>\w+))*'


def parse_hierarchy(hierarchy_string):
    results = []
    tags = hierarchy_string.split(' ')

    for tag in tags:
        match = regex.match(TAG_REGEX, tag)
        tag_name = match.group("name")
        id_name = match.group("id")
        classes = match.captures("classes")
        classes_set = set()
        for c in classes:
            classes_set.add(c)
        results += [Tag(tag_name, id_name, classes_set)]
        print(tag_name, id_name, classes)

    return results
