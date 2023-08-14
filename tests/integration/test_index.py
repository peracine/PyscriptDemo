import asyncio
from playwright.async_api import async_playwright, expect

url_index_page = 'http://localhost:8000/' 
splash_timeout = 10_000

#>python -m pytest tests/integration/test_index.py --capture=tee-sys
async def test_img_after_select(page) -> None:
    await page.get_by_label('Year:').select_option('2020')
    await expect(page.locator('img')).to_have_count(1)

async def main() -> None:
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(url_index_page)
        await expect(page.locator('py-splashscreen')).to_have_count(0, timeout=splash_timeout)
        
        await test_img_after_select(page)
        
        await context.close()
        await browser.close()

asyncio.run(main())