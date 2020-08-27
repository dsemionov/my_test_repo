import pytest

@pytest.fixture(scope="module")
def base_feature_path():
    print("taking base path...")
