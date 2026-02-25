# Labelme - Quick Start Guide

Quick reference for new polygon editing features.

---

## 🎯 Quick Reference Card

| Action | Shortcut | How To Use |
|--------|----------|------------|
| **Add 1 Point** | `Alt + Click` | Hover over edge → Alt+Click where you want point |
| **Add N Points** | `Ctrl + M` | Hover over edge → Ctrl+M → Enter number → OK |
| **Remove Point** | `Backspace` or `Alt+Shift+Click` | Click point → Press Backspace (or Alt+Shift+Click) |
| **Merge Polygons** | `Ctrl + Shift + M` | Select polygons (Ctrl+Click each) → Ctrl+Shift+M |

---

## 📝 Common Tasks

### Task 1: Make a Polygon More Detailed
**Problem**: Polygon edge is too rough, needs more points

**Solution**:
1. Press `Ctrl + J` (Edit mode)
2. Hover over the rough edge
3. Press `Ctrl + M`
4. Enter `5` (or any number)
5. Adjust the new points to fit the actual boundary

---

### Task 2: Fix an Over-Detailed Polygon
**Problem**: Too many points, making editing slow

**Solution**:
1. Press `Ctrl + J` (Edit mode)
2. Click unwanted points
3. Press `Backspace` for each point to remove

---

### Task 3: Combine Multiple Polygons
**Problem**: Same object annotated as multiple polygons

**Solution**:
1. Press `Ctrl + J` (Edit mode)
2. Hold `Ctrl` and click each polygon to select
3. Press `Ctrl + Shift + M` to merge
4. Done! Single polygon with same label

---

### Task 4: Apply Same Label to Multiple Objects
**Problem**: 10 cars, want them all labeled "car" quickly

**Solution**:
1. Draw rough boxes around each car
2. Select all 10 boxes (Ctrl + Click each)
3. Press `Ctrl + Shift + M`
4. Result: 10 separate car polygons, all labeled "car"

---

## 🔧 Configuration

Edit `~/.labelmerc` (Linux) or `C:\Users\YourName\.labelmerc` (Windows):

```yaml
# Change default number of points to add
default_num_points_to_add: 3

# Change shortcuts
shortcuts:
  add_multiple_points: Ctrl+M
  merge_polygons: Ctrl+Shift+M
  remove_selected_point: [Meta+H, Backspace]
```

---

## ⚠️ Tips & Tricks

### 💡 Point Addition
- **Curved edges**: Use 5-10 points for smooth curves
- **Straight edges**: Use 1-2 points to straighten
- **Even spacing**: Multiple points are evenly distributed automatically

### 💡 Polygon Merge
- **Disconnected objects**: All are kept as separate polygons with same label
- **Overlapping polygons**: Automatically unions them correctly
- **Mixed scenarios**: Some connected, some not → Multiple results
- **Info dialog**: Shows how many polygons were created if > 1

### 💡 General
- **Edit mode**: Always press `Ctrl + J` first to enter edit mode
- **Selection**: Hold `Ctrl` while clicking to select multiple polygons
- **Undo**: `Ctrl + Z` works for most operations

---

## 🐛 Troubleshooting

### "Add Multiple Points" menu is grayed out
- ✅ Make sure you're hovering over an **edge** (not a vertex)
- ✅ Check you're in **Edit mode** (`Ctrl + J`)
- ✅ Only works on **polygons** (not rectangles, circles, etc.)

### Merge doesn't work
- ✅ Select **at least 2 polygons**
- ✅ Make sure shapes are **polygons** (not other types)
- ✅ Check status bar for error messages

### Shortcut conflicts
- ✅ Check `~/.labelmerc` for conflicting shortcuts
- ✅ `Ctrl + Shift + A` was changed to `Ctrl + M` to avoid conflict

---

## 📖 More Info

- **Full docs**: See `POINT_ADDITION_FEATURE.md` and `POLYGON_MERGE_FEATURE.md`
- **Complete overview**: See `FEATURES_SUMMARY.md`
- **User guide**: See `USAGE_GUIDE.md`

---

## 🚀 Install on Another Machine

**Linux/Ubuntu**:
```bash
cd /path/to/labelme
pip install -e .
labelme
```

**Windows**:
```cmd
cd C:\path\to\labelme
pip install -e .
labelme
```

---

**Happy Annotating! 🎉**
