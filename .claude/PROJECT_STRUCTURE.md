# Labelme Project Structure & Status

**Auto-generated**: 2026-02-20  
**Purpose**: Token-efficient reference for future analysis sessions

## Quick Facts
- **Language**: Python 3.10+
- **GUI Framework**: PyQt5
- **Package Manager**: uv (not pip/poetry)
- **Python Files**: 35 modules
- **Core Code**: ~4210 LOC (app.py, shape.py, _label_file.py, canvas.py)
- **License**: GPL-3.0

## Core Architecture (3-Layer)

```
┌─────────────────────────────────────┐
│   GUI Layer (PyQt5)                 │
│   - MainWindow (app.py)             │
│   - Canvas, Dialogs, Toolbars       │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│   Data Layer                        │
│   - Shape (shape.py)                │
│   - LabelFile (_label_file.py)      │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│   Utility Layer                     │
│   - Image utils, Shape math         │
│   - AI automation (SAM2, YOLO)      │
└─────────────────────────────────────┘
```

## Module Map (35 files)

### 1. Core Application
| File | Classes | Purpose |
|------|---------|---------|
| `app.py` (2340 LOC) | `MainWindow`, `_ZoomMode` | Main GUI orchestrator, menu/toolbar setup, event handlers |
| `shape.py` | `Shape` | Data class: polygon/rect/circle/line/point annotations |
| `_label_file.py` | `LabelFile`, `ShapeDict`, `LabelFileError` | JSON I/O, serialization/deserialization |

### 2. Widgets (labelme/widgets/)
| Widget | Purpose |
|--------|---------|
| `canvas.py` | `Canvas`, `CanvasMode` - Drawing surface, shape rendering, mouse interaction |
| `label_list_widget.py` | `LabelListWidget`, `LabelListWidgetItem` - Shape list UI |
| `label_dialog.py` | `LabelDialog`, `LabelQLineEdit` - Label input dialog |
| `_ai_assisted_annotation_widget.py` | `AiAssistedAnnotationWidget` - SAM2 point-to-polygon UI |
| `_ai_text_to_annotation_widget.py` | `AiTextToAnnotationWidget` - YOLO text-to-bbox UI |
| `brightness_contrast_dialog.py` | `BrightnessContrastDialog` - Image adjustment |
| `file_dialog_preview.py` | `FileDialogPreview`, `ScrollAreaPreview` - File picker with preview |
| `tool_bar.py` | `ToolBar` - Custom toolbar |
| `zoom_widget.py` | `ZoomWidget` - Zoom control spinbox |
| `download.py` | `_AiModelDownloadWorker`, `_AiModelDownloadSignals` - Async model downloads |
| `unique_label_qlist_widget.py` | `UniqueLabelQListWidget` - Label suggestion list |
| `_info_button.py` | `InfoButton` - Help button widget |
| `_status.py` | `StatusStats` - Status bar stats display |

### 3. AI Automation (labelme/_automation/)
| Module | Function |
|--------|----------|
| `_osam_session.py` | SAM2/EfficientSAM session manager |
| `polygon_from_mask.py` | Convert AI mask → polygon points |
| `bbox_from_text.py` | YOLO-World text prompt → bounding boxes |

### 4. CLI Tools (labelme/cli/)
| Script | Entry Point | Purpose |
|--------|-------------|---------|
| `draw_json.py` | `labelme_draw_json` | Visualize annotations on image |
| `draw_label_png.py` | `labelme_draw_label_png` | Render label PNG from JSON |
| `export_json.py` | `labelme_export_json` | Batch export JSON files |
| `on_docker.py` | `labelme_on_docker` | Docker container helper |

### 5. Utilities (labelme/utils/)
| Module | Key Functions |
|--------|---------------|
| `image.py` | `img_arr_to_b64()`, `img_b64_to_arr()`, `img_pil_to_data()` - Image encoding |
| `shape.py` | `shape_to_mask()`, `masks_to_bboxes()`, `polygons_to_mask()` - Shape math |
| `qt.py` | `newIcon()`, `newAction()`, `addActions()` - Qt helpers |
| `_io.py` | `lblsave()` - Label file saving |

### 6. Config
| File | Purpose |
|------|---------|
| `config/__init__.py` | Load/validate config, merge with defaults |
| `config/default_config.yaml` | Default settings (labels, flags, shortcuts, etc.) |

### 7. Other
| File | Purpose |
|------|---------|
| `__main__.py` | CLI entry point: `labelme` command |
| `__init__.py` | Package metadata, version, exports |
| `testing.py` | Test utilities |

## Data Flow

### Annotation Creation
```
User draws on Canvas → Canvas.finalize() → Shape object created
→ MainWindow.addLabel() → LabelFile.shapes.append()
→ Save triggers LabelFile.save() → JSON written to disk
```

### File Loading
```
MainWindow.loadFile(path) → LabelFile.load(path)
→ Parse JSON → Create Shape objects → Canvas.loadShapes()
→ Render shapes on canvas
```

### AI-Assisted Annotation
```
User clicks "AI Polygon" → AiAssistedAnnotationWidget shown
→ User clicks point → _osam_session.prompt() [SAM2]
→ Mask returned → polygon_from_mask() → Shape created
```

## Key Data Structures

### Shape (shape.py)
```python
Shape(
    label: str,              # e.g., "person", "car"
    shape_type: Literal["polygon", "rectangle", "circle", "line", "point", "mask"],
    points: list[tuple[float, float]],  # Coordinates
    flags: dict[str, bool],  # Custom flags
    group_id: int | None,    # For instance grouping
    description: str,
    mask: np.ndarray | None  # For mask type
)
```

### LabelFile JSON Format
```json
{
  "version": "5.5.0",
  "flags": {},
  "shapes": [
    {
      "label": "person",
      "shape_type": "polygon",
      "points": [[x1,y1], [x2,y2], ...],
      "group_id": null,
      "description": "",
      "flags": {}
    }
  ],
  "imagePath": "image.jpg",
  "imageData": "base64...",  // Optional
  "imageHeight": 480,
  "imageWidth": 640
}
```

## Build & Test Commands

```bash
# Setup
make setup            # uv sync (install deps)

# Development
make format           # ruff format + auto-fix
make lint             # ruff format --check + ruff check + ty
make check            # lint + translation check
make test             # pytest -v tests/

# Run
uv run labelme                              # GUI
uv run labelme image.jpg                    # Open specific image
uv run labelme_draw_json input.json         # CLI visualization
```

## Dependencies (Key)

| Package | Purpose |
|---------|---------|
| `pyqt5>=5.14.0` | GUI framework |
| `osam>=0.3.1` | SAM2/EfficientSAM AI models |
| `numpy` | Array operations |
| `pillow>=2.8` | Image I/O |
| `imgviz>=2.0.0` | Visualization utilities |
| `loguru` | Logging (not stdlib logging) |
| `matplotlib` | Color maps, visualization |
| `scikit-image` | Image processing |
| `natsort>=7.1.0` | Natural sorting |
| `pyyaml` | Config file parsing |

## Code Style Quick Ref

```python
# Imports: single-line, sorted (ruff isort)
import json
from pathlib import Path
from typing import Literal

import numpy as np
from PyQt5 import QtCore

from labelme.shape import Shape

# Naming
class MyClass:           # PascalCase
    def publicMethod():  # camelCase (Qt legacy)
    def _private_new():  # _snake_case (new code)
    
my_variable = 42         # snake_case
CONSTANT = 100           # UPPER_SNAKE_CASE

# Type hints: modern syntax
def func(x: str | None) -> list[Shape]:
    ...

# Strings
user_msg = self.tr("Translated text")   # i18n
log_msg = f"Loaded {count} shapes"      # f-strings
logger.info("Count: {}", count)         # loguru positional
```

## Test Structure

```
tests/
├── conftest.py              # data_path fixture
├── data/                    # Test images/JSONs
│   ├── annotated/          # Sample annotations
│   ├── annotated_with_data/
│   └── raw/                # Plain images
├── e2e/                     # GUI tests (pytest-qt)
│   ├── conftest.py         # _isolated_qtsettings, show_window_and_wait_for_imagedata()
│   ├── smoke_test.py
│   ├── annotation_test.py
│   └── ...
└── unit/                    # Unit tests
    ├── _label_file_test.py
    ├── config_test.py
    ├── utils/
    └── widgets/
```

**Test naming**: `*_test.py` (not `test_*.py`)  
**Markers**: `@pytest.mark.gui` for GUI tests  
**CI**: Ubuntu only (needs Xvfb for headless Qt)

## Examples (7 use cases)

| Example | Purpose |
|---------|---------|
| `tutorial/` | Basic annotation walkthrough |
| `bbox_detection/` | Object detection (VOC XML export) |
| `semantic_segmentation/` | Semantic segmentation (VOC PNG masks) |
| `instance_segmentation/` | Instance segmentation (VOC + COCO) |
| `classification/` | Image-level flags |
| `video_annotation/` | Frame-by-frame video annotation |
| `primitives/` | All shape types demo |

## Translation

- **Languages**: 15 (zh_CN, zh_TW, ja_JP, ko_KR, de_DE, fr_FR, es_ES, fa_IR, nl_NL, pt_BR, it_IT, vi_VN, tr_TR, hu_HU)
- **Format**: Qt `.ts` (source) → `.qm` (compiled)
- **Update**: `make update_translate` (do NOT run `lrelease` manually)

## Git Workflow

**Conventional commits**:
```
feat: add shape rotation tool
fix: canvas zoom reset on file load
refactor: extract shape rendering logic
test: add label dialog unit tests
docs: update JSON format spec
chore: bump dependencies
perf: optimize polygon rendering
ci: add macOS test matrix
i18n: update Korean translation
```

## Known Patterns

1. **Actions**: `functools.partial` for callbacks, stored in `types.SimpleNamespace`
2. **Settings**: `QtCore.QSettings` for persistent user prefs
3. **Validation**: Properties with setters (e.g., `Shape.shape_type`)
4. **Errors**: `assert` for invariants, `ValueError` for bad input, `LabelFileError` for I/O
5. **Logging**: `from loguru import logger` (not stdlib)

## Performance Notes

- Large image handling: lazy loading, base64 optional (`--nodata`)
- Shape rendering: QPainter with caching
- AI models: downloaded on-demand, cached in `~/.cache/osam/`

## Future Refactor Opportunities

*Document potential improvements here after analysis:*
- [ ] TBD after refactor/optimization phase

---

**Last Updated**: 2026-02-20  
**Version**: Extracted from labelme main branch
