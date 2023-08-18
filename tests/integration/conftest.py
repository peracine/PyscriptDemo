from pathlib import Path
import pytest
from subprocess import Popen, PIPE
from playwright.async_api import async_playwright, Page

class PytestConf:
    SERVER_DOMAIN = 'localhost'
    SERVER_PORT = 8000    
    SPLASH_ELEMENT = 'py-splashscreen'    
    SPLASH_TIMEOUT = 10000 #Make sure 'autoclose' in settings is true

@pytest.fixture(scope='class')
def server_start() -> None:
    with Popen(['python', '-m', 'http.server', f'{PytestConf.SERVER_PORT}', '--directory', f'{Path.cwd()}/src'], stdout=PIPE) as process:
        yield
        process.terminate()
        process.kill()        

@pytest.fixture
async def pw_page() -> Page:
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context()
        yield await context.new_page()
        await context.close()
        await browser.close()