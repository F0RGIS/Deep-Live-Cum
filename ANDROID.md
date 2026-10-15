# Running Deep-Live-Cum on Android

## Automated build (GitHub Actions)

The workflow `.github/workflows/build-android.yml`:

1. Downloads the essential models (`inswapper_128_fp16.onnx` + buffalo_l pack) into `models/`.
2. Downloads official PySide6 Android wheels.
3. Runs `pyside6-android-deploy` to produce an APK.
4. Uploads the APK as an artifact.

Trigger it manually from the Actions tab, or it runs on pushes that touch `main.py` or `modules/`.

## Model packaging

- Models are placed in `models/` before packaging so they can be included as app assets.
- On first launch the app copies any bundled model into the writable app storage (`MODELS_DIR`).
- If a model is missing or incomplete, it falls back to downloading from Hugging Face.

Required for basic face swap:
- `inswapper_128_fp16.onnx`
- `buffalo_l/buffalo_l/*.onnx` (InsightFace detection pack)

Optional enhancers (`gfpgan-1024.onnx`, GPEN models) are downloaded only if selected.

## Manual build

See the previous instructions. The entry point is `main.py`. Camera permission is requested via Qt when the APK is packaged.

## Limitations

- Real-time FPS on mobile is much lower than desktop CUDA.
- Large models increase APK size significantly.
- OpenCV camera access on Android is basic; permission must be granted.
