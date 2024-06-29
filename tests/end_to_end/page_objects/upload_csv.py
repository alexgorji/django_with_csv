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
        self.upload_input = page.locator('input[type="file"]')
        self.submit_button = page.locator('input[type="submit"]')
        self.success_message = page.locator('#success_message')

    def upload_file(self, csv_path: Path):
        self.upload_input.set_input_files(csv_path)

    def click_submit_button(self):
        self.submit_button.click()

    def get_success_message(self):
        return self.success_message.inner_text()
