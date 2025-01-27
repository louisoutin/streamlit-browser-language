import os
import time
import streamlit as st
from typing import Union
import streamlit.components.v1 as components

_RELEASE = True

if not _RELEASE:
    _browser_language_detector = components.declare_component(
        "browser_language_detector", url="http://localhost:3001"
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _browser_language_detector = components.declare_component(
        "browser_language_detector", path=build_dir
    )


def detect_browser_language(
    timeout: Union[int, float] = 5,
    interval: Union[int, float] = 0.1,
    key: str = "browser_language",
):
    """
    Detect the user's browser language.

    Args:
        timeout (Union[int, float]): Maximum time to wait for the language detection (default: 5 seconds).
        interval (Union[int, float]): Interval to check for the language detection result (default: 0.1 seconds).
        key (str): A unique key for the component (default: "browser_language").

    Returns:
        str: The detected browser language (e.g., "en", "es", "fr").
    """
    value = _browser_language_detector(key=key, default=None)
    start_time = time.time()
    while time.time() - start_time < timeout:
        value = st.session_state.get(key)
        if value is not None:
            return value
        time.sleep(interval)

    st.warning(
        f"Timeout reached while waiting for browser language detection. Using default value: {None}"
    )
    return value
