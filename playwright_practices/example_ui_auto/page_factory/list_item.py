from playwright_practices.example_ui_auto.page_factory.component import Component


class ListItem(Component):
    @property
    def type_of(self) -> str:
        return 'list item'