from pages.base.component import Component


class List(Component):
    
    @property
    def type_of(self) -> str:
        return 'list'
