# Polygon Merge Feature - Usage Guide

## ✅ What I Fixed

1. **Added merge option to Edit menu** - Now appears below "Add Multiple Points"
2. **Added merge to right-click context menu** - Available when 2+ shapes selected
3. **Improved user feedback** - Clear messages explaining what happened

## 🎯 How to Use Merge

### Step 1: Select Polygons
1. Switch to Edit mode (`Ctrl+J`)
2. Hold `Ctrl` and click on each polygon you want to merge
3. You need at least 2 polygons selected

### Step 2: Merge
Use any of these methods:
- **Keyboard**: Press `Ctrl+Shift+M`
- **Menu**: Go to Edit → Merge Polygons
- **Right-click**: Right-click and select "Merge Polygons"

### Step 3: Save
Press `Ctrl+S` to save the changes (or enable auto-save)

## 🔍 Understanding Merge Results

### ✅ Touching/Overlapping Polygons → Merge into 1
```
Before:  [Polygon A][Polygon B]  (adjacent)
After:   [   Merged Polygon   ]  (1 polygon)
```
**Message**: "Merged 2 polygons into 1 polygon"

### ⚠️ Disconnected Polygons → Stay Separate
```
Before:  [Polygon A]    [Polygon B]  (separated)
After:   [Polygon A]    [Polygon B]  (still 2 polygons)
```
**Message**: "The selected 2 polygons are not touching each other... To merge polygons into one, they must be adjacent or overlapping."

### 🔀 Mixed (Some Touch, Some Don't) → Partial Merge
```
Before:  [A][B]    [C]  (A & B touch, C separate)
After:   [A+B]     [C]  (2 polygons)
```
**Message**: "Merged 3 polygons into 2 polygons. Some polygons were not touching so they remain separate."

## 💡 Key Points

1. **Polygons must be touching to merge into one**
   - Adjacent (sharing an edge) ✓
   - Overlapping ✓
   - Completely separate ✗

2. **All merged shapes inherit the label from the first selected polygon**

3. **The merge processes all selected polygons** even if they're disconnected
   - Cleans up geometry
   - Fixes self-intersections
   - But cannot combine disconnected regions into a single polygon (this is a geometric constraint, not a bug!)

4. **Changes are in memory until you save**
   - Press `Ctrl+S` to save
   - Or enable "Save Automatically" in File menu
   - Otherwise changes are lost when you reload the file

## 🐛 Troubleshooting

### "Nothing happened after merge"
**Cause**: You selected disconnected polygons that don't touch each other.
**Solution**: Only select polygons that are adjacent or overlapping if you want them to combine into one.

### "Changes disappeared when I reopened the file"
**Cause**: You didn't save the file after merging.
**Solution**: Press `Ctrl+S` to save, or enable auto-save.

### "Merge Failed" error
**Cause**: You selected non-polygon shapes (rectangles, circles, lines, points).
**Solution**: Only polygon shapes can be merged. Convert other shapes to polygons first.

## 📋 Quick Reference

| Action | Shortcut |
|--------|----------|
| Select multiple shapes | Hold `Ctrl` + Click |
| Merge selected polygons | `Ctrl+Shift+M` |
| Save file | `Ctrl+S` |
| Switch to Edit mode | `Ctrl+J` |

## ✨ Example Workflow

1. Open an image with multiple adjacent polygons of the same object
2. Press `Ctrl+J` to enter Edit mode
3. Hold `Ctrl` and click each polygon you want to merge
4. Press `Ctrl+Shift+M` to merge them
5. Check the message dialog to see the result
6. Press `Ctrl+S` to save your changes

---

**Note**: The merge feature uses Shapely's geometric union operation, which is mathematically accurate. If two polygons don't touch, they cannot be merged into a single polygon - this is a fundamental geometric constraint, not a limitation of the software.
