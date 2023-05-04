from playwright_practices.example_ui_auto.page_factory.component import Component


class Link(Component):
    @property
    def type_of(self) -> str:
        return 'link'