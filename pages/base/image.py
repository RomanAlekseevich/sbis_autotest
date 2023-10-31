from pages.base.component import Component


class Image(Component):
    
    @property
    def type_of(self) -> str:
        return 'image'
    
    
    def get_sizes(self, **kwargs) -> list[tuple]:
        elements = self.get_presence_all_elements(**kwargs)
        sizes = []
        for element in elements:
            sizes.append(
                (element.get_attribute('height'), 
                 element.get_attribute('width'))
            )
        return sizes
           