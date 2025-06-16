"""Validation tests to ensure the testing infrastructure is set up correctly."""

import sys
import pytest
from pathlib import Path


def test_pytest_is_installed():
    """Test that pytest is installed and importable."""
    import pytest
    assert pytest.__version__


def test_pytest_cov_is_installed():
    """Test that pytest-cov is installed."""
    import pytest_cov
    assert pytest_cov


def test_pytest_mock_is_installed():
    """Test that pytest-mock is installed."""
    import pytest_mock
    assert pytest_mock


def test_project_structure_exists():
    """Test that the expected project structure exists."""
    root = Path(__file__).parent.parent
    
    # Check main directories
    assert root.exists()
    assert (root / "tests").exists()
    assert (root / "tests" / "unit").exists()
    assert (root / "tests" / "integration").exists()
    
    # Check configuration files
    assert (root / "pyproject.toml").exists()
    assert (root / ".gitignore").exists()


def test_conftest_fixtures_available(temp_dir, mock_config, sample_text):
    """Test that conftest fixtures are available."""
    # Test temp_dir fixture
    assert temp_dir.exists()
    assert temp_dir.is_dir()
    
    # Test mock_config fixture
    assert isinstance(mock_config, dict)
    assert "font_path" in mock_config
    assert "output_dir" in mock_config
    
    # Test sample_text fixture
    assert isinstance(sample_text, str)
    assert len(sample_text) > 0


@pytest.mark.unit
def test_unit_marker():
    """Test that unit marker works."""
    assert True


@pytest.mark.integration
def test_integration_marker():
    """Test that integration marker works."""
    assert True


@pytest.mark.slow
def test_slow_marker():
    """Test that slow marker works."""
    assert True


def test_coverage_configuration():
    """Test that coverage is properly configured."""
    import coverage
    assert coverage.__version__


def test_python_path_configured():
    """Test that Python path is correctly configured for imports."""
    # The project root should be in sys.path
    root = Path(__file__).parent.parent
    root_str = str(root)
    assert any(root_str in path for path in sys.path)


class TestMockingCapabilities:
    """Test that mocking capabilities work correctly."""
    
    def test_unittest_mock_available(self):
        """Test that unittest.mock is available."""
        from unittest.mock import Mock, MagicMock, patch
        
        mock_obj = Mock()
        mock_obj.test_method.return_value = "test"
        assert mock_obj.test_method() == "test"
    
    def test_pytest_mock_fixture(self, mocker):
        """Test that pytest-mock mocker fixture works."""
        mock_func = mocker.Mock(return_value=42)
        assert mock_func() == 42
        mock_func.assert_called_once()


def test_isolated_filesystem_fixture(isolated_filesystem):
    """Test that isolated filesystem fixture works correctly."""
    assert isolated_filesystem.exists()
    assert (isolated_filesystem / "Fonts").exists()
    assert (isolated_filesystem / "Backgrang").exists()
    assert (isolated_filesystem / "output").exists()
    assert (isolated_filesystem / "Fonts" / "test_font.ttf").exists()


def test_poetry_scripts_configured():
    """Test that poetry scripts are configured in pyproject.toml."""
    import toml
    
    root = Path(__file__).parent.parent
    pyproject_path = root / "pyproject.toml"
    
    with open(pyproject_path, "r") as f:
        config = toml.load(f)
    
    # Check that test scripts are configured
    assert "tool" in config
    assert "poetry" in config["tool"]
    assert "scripts" in config["tool"]["poetry"]
    assert "test" in config["tool"]["poetry"]["scripts"]
    assert "tests" in config["tool"]["poetry"]["scripts"]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])