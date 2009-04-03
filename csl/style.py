

class Info:
    """
    >>> info = Info()
    >>> info.title = "ABC Style"
    >>> print(info.title)
    ABC Style
    >>> info.add_category('author-date')
    >>> print(info.categories[0])
    author-date
    """
    def __init__(self, title=None, id=None, updated=None):
        self.title = title
        self.id = id
        self.updated = updated
        self.categories = []

    def add_category(self, category):
        self.categories.append(category)


class Option:
    """
    >>> option = Option('et-al-min', '4')
    >>> print(option.value)
    4
    """
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Context:
    """
    >>> context = Context()
    >>> len(context.options)
    0
    >>> context.add_option('et-al-min', 5)
    >>> len(context.options)
    1
    """
    def __init__(self):
        self.options = []
        self.sort = []
        self.layout = []

    def add_option(self, name, value):
        self.options.append(Option(name, value))


class Citation(Context):
    """
    >>> citation = Citation()
    >>> len(citation.options)
    0
    >>> citation.add_option('et-al-min', 5)
    >>> len(citation.options)
    1
    """
    pass



class Bibliography(Context):
    """
    >>> bib = Bibliography()
    >>> len(bib.options)
    0
    >>> bib.add_option('et-al-min', 5)
    >>> len(bib.options)
    1
    """
    pass



class Template:
    def __init__(self, content=None):
        self.content = content



class Macro(Template):
    """
    >>> macro = Macro()
    >>> macro.name = "foo"
    >>> print(macro.name)
    foo
    >>> print(macro.content)
    None
    """
    def __new__(self, name=None):
        self.name = name


class Style:
    """
    >>> style = Style()
    >>> print(style.info)
    None
    """
    def __init__(self, info=None, macros=[], 
                 citation=None, bibliography=None):
        self.info = info
        self.macros = macros
        self.citation = citation
        self.bibliography = bibliography


