# Running Deep-Live-Cum on Android

The app can be packaged as an APK using Qt's official `pyside6-android-deploy` tool.

## Requirements

- Linux host (or WSL) for the build
- Android SDK + NDK (the deploy tool can download them)
- Prebuilt PySide6 Android wheels (aarch64 recommended)

Download the wheels from:
https://download.qt.io/official_releases/QtForPython/

Look for `PySide6-*-android_aarch64.whl` and the matching `shiboken6` wheel.

## Build steps

1. Rename or use the provided `main.py` (required by the deploy tool).
2. Run:

```bash
pyside6-android-deploy \
  --name "DeepLiveCum" \
  --wheel-pyside=/path/to/PySide6-*-android_aarch64.whl \
  --wheel-shiboken=/path/to/shiboken6-*-android_aarch64.whl \
  --ndk-path=/path/to/android-ndk \
  --sdk-path=/path/to/android-sdk
```

3. The tool produces an APK. Install it with:

```bash
adb install DeepLiveCum-*-arm64-v8a-debug.apk
```

## Notes

- Camera permission is requested via Qt's `QCameraPermission` when the app is packaged.
- OpenCV `VideoCapture(0)` is used on Android as the capture backend.
- ONNX models are still downloaded on first run (same as desktop). Real-time performance on mobile is limited; CPU or NNAPI is used.
- Large models (inswapper, GFPGAN) may exceed device storage or memory on low-end phones.

## Limitations

This is experimental. Expect lower FPS than desktop CUDA, and some features (GPU providers, certain enhancers) may not work out of the box on Android.
