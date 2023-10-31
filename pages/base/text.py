from pages.base.component import Component


class Text(Component):
    
    @property
    def type_of(self) -> str:
        return 'text'
