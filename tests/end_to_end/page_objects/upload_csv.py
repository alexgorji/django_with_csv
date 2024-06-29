from pathlib import Path

from playwright.async_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str) -> None:
        self.page.goto(url)


class UploadCSVPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.upload_input = page.locator('#csv_upload')
        self.submit_button = page.locator('#csv_submit')
        self.success_message = page.locator('#csv_success')

    def upload_file(self, csv_path: Path):
        self.upload_input.set_input_files(str(csv_path))

    def click_submit_button(self):
        self.submit_button.click()

    def get_success_message(self):
        return self.success_message.inner_text()
