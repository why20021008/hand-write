"""Shared pytest fixtures and configuration."""

import os
import tempfile
from pathlib import Path
from typing import Generator

import pytest
from unittest.mock import Mock, MagicMock


@pytest.fixture
def temp_dir() -> Generator[Path, None, None]:
    """Create a temporary directory for test files."""
    with tempfile.TemporaryDirectory() as temp_dir:
        yield Path(temp_dir)


@pytest.fixture
def mock_config() -> dict:
    """Provide a mock configuration dictionary."""
    return {
        "font_path": "Fonts/heroType.ttf",
        "background_path": "Backgrang/white-A4.jpeg",
        "output_dir": "output",
        "line_spacing": 1.5,
        "left_margin": 50,
        "top_margin": 50,
        "right_margin": 50,
        "bottom_margin": 50,
        "font_size": 30,
        "font_color": (0, 0, 0),
    }


@pytest.fixture
def mock_image():
    """Create a mock PIL Image object."""
    from PIL import Image
    return MagicMock(spec=Image.Image)


@pytest.fixture
def sample_text() -> str:
    """Provide sample Chinese text for testing."""
    return "这是一个测试文本。This is a test text."


@pytest.fixture
def mock_font():
    """Create a mock font object."""
    font = Mock()
    font.getbbox = Mock(return_value=(0, 0, 100, 30))
    font.getlength = Mock(return_value=100)
    return font


@pytest.fixture(autouse=True)
def setup_test_env(monkeypatch):
    """Set up test environment variables."""
    monkeypatch.setenv("PYTEST_CURRENT_TEST", "true")
    

@pytest.fixture
def mock_qt_app(monkeypatch):
    """Mock Qt application for UI tests."""
    mock_app = Mock()
    mock_app.exec = Mock(return_value=0)
    monkeypatch.setattr("PySide6.QtWidgets.QApplication", Mock(return_value=mock_app))
    return mock_app


@pytest.fixture
def isolated_filesystem(tmp_path) -> Path:
    """Create an isolated filesystem for testing with project structure."""
    # Create necessary directories
    (tmp_path / "Fonts").mkdir()
    (tmp_path / "Backgrang").mkdir()
    (tmp_path / "output").mkdir()
    
    # Create dummy files
    (tmp_path / "Fonts" / "test_font.ttf").write_bytes(b"dummy font data")
    (tmp_path / "Backgrang" / "test_bg.png").write_bytes(b"dummy image data")
    
    return tmp_path


@pytest.fixture
def mock_handright():
    """Mock handright module."""
    mock_template = Mock()
    mock_template.handwrite = Mock(return_value=[Mock()])
    
    mock_handright_module = Mock()
    mock_handright_module.Template = Mock(return_value=mock_template)
    
    return mock_handright_module


@pytest.fixture(scope="session")
def test_data_dir() -> Path:
    """Get the path to test data directory."""
    return Path(__file__).parent / "test_data"


def pytest_configure(config):
    """Configure pytest with custom settings."""
    # Register custom markers
    config.addinivalue_line(
        "markers", "unit: mark test as a unit test"
    )
    config.addinivalue_line(
        "markers", "integration: mark test as an integration test"
    )
    config.addinivalue_line(
        "markers", "slow: mark test as slow running"
    )


def pytest_collection_modifyitems(config, items):
    """Modify test collection to add markers based on test location."""
    for item in items:
        # Add markers based on test file location
        if "unit" in str(item.fspath):
            item.add_marker(pytest.mark.unit)
        elif "integration" in str(item.fspath):
            item.add_marker(pytest.mark.integration)