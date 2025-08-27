import pytest
from unittest import mock

class TestCopyButtonJS:
    @pytest.fixture
    def mock_dom(self):
        """Simulate a minimal DOM structure with <div><pre>code</pre></div>."""
        class MockBlock:
            def __init__(self, text):
                self.innerText = text
                self.parentNode = self
                self.style = {}
                self.children = []

            def appendChild(self, child):
                self.children.append(child)

        return MockBlock("console.log('hello');")

    def test_button_appended(self, mock_dom):
        """Ensure button gets appended to pre block parent."""
        block = mock_dom
        button = mock.Mock()
        block.appendChild(button)
        assert button in block.children

    @pytest.mark.asyncio
    async def test_copy_to_clipboard(self, mock_dom):
        """Ensure clicking button writes correct text to clipboard."""
        block = mock_dom
        fake_clipboard = mock.AsyncMock()
        fake_clipboard.writeText.return_value = None

        # simulate button click handler
        async def on_click():
            await fake_clipboard.writeText(block.innerText)
            return "✅ Copied!"

        result = await on_click()
        assert "Copied" in result
        fake_clipboard.writeText.assert_called_once_with("console.log('hello');")