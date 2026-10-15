"""Android-specific camera permission handling for PySide6."""
from __future__ import annotations

import sys


def is_android() -> bool:
    return sys.platform == "android" or "android" in sys.platform.lower()


def request_camera_permission(callback=None) -> bool:
    """Request CAMERA permission via Qt. Returns True if already granted.

    On Android the permission API only works inside a packaged APK
    (pyside6-android-deploy). In interpreted mode this is a no-op.
    """
    if not is_android():
        return True

    try:
        from PySide6.QtCore import QCameraPermission, Qt
        from PySide6.QtWidgets import QApplication

        app = QApplication.instance()
        if app is None:
            return False

        perm = QCameraPermission()
        status = app.checkPermission(perm)
        if status == Qt.PermissionStatus.Granted:
            return True
        if status == Qt.PermissionStatus.Denied:
            print("[Android] Camera permission denied")
            return False

        # Undetermined — request it
        if callback:
            app.requestPermission(perm, callback)
        else:
            app.requestPermission(perm)
        return False
    except Exception as exc:
        print(f"[Android] Camera permission request failed: {exc}")
        return False
