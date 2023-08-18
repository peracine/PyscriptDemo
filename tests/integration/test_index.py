import pytest
from playwright.async_api import expect
from tests.integration.conftest import PytestConf

#>python -m pytest tests/integration/test_index.py --capture=tee-sys
class TestIndexPage():

    @property
    def page_url(self) -> str:
        #index.html by default 
        return f'http://{PytestConf.SERVER_DOMAIN}:{PytestConf.SERVER_PORT}/'
    
    @pytest.mark.asyncio
    async def test_img_after_select(self, pw_page, server_start) -> None:
        await pw_page.goto(self.page_url)
        await expect(pw_page.locator(PytestConf.SPLASH_ELEMENT)).to_have_count(0, timeout=PytestConf.SPLASH_TIMEOUT)

        await pw_page.locator('#slctYear').select_option('2020')

        await expect(pw_page.locator('img')).to_have_count(1)