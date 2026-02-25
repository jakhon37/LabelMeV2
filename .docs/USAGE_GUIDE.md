# Point Addition Feature - Quick Usage Guide

## ✅ What's Implemented

### 1. **Single Point Addition** (Existing - Already Working)
- **Action**: Hold `Alt` and click on an edge
- **What happens**: Adds one point at the exact cursor position
- **Status indicator**: When hovering over edge, status shows "ALT + Click to create point on shape"

### 2. **Multiple Point Addition** (NEW)
- **Action**: Hover over edge, then press `Ctrl+M`
- **What happens**: Dialog appears asking for number of points (1-100, default: 1)
- **Result**: Points are evenly distributed along the edge
- **Status indicator**: When hovering over edge, status shows "Ctrl+M to add multiple points"

### 3. **Point Removal** (Existing)
- **Action**: Hold `Alt+Shift` and click on a vertex, OR press `Meta+H` / `Backspace` when vertex is selected
- **What happens**: Removes the selected point
- **Status indicator**: When hovering over vertex, status shows "ALT + SHIFT + Click to delete point"

---

## 📋 Step-by-Step Instructions

### To add a SINGLE point:
1. Switch to **Edit Mode** (press `Ctrl+J` or click Edit Polygons button)
2. Move mouse over polygon **edge** (the line between two points)
   - Edge will highlight
   - Status bar shows: "ALT + Click to create point on shape"
3. Hold `Alt` and click
4. Point is added at cursor position

### To add MULTIPLE points:
1. Switch to **Edit Mode** (`Ctrl+J`)
2. Move mouse over polygon **edge**
   - Edge will highlight
   - Status bar shows: "Ctrl+M to add multiple points"
3. Press `Ctrl+M`
4. Enter number of points in dialog (e.g., 5)
5. Click OK
6. Points are automatically distributed evenly along the edge

### To REMOVE a point:
1. Switch to **Edit Mode** (`Ctrl+J`)
2. Move mouse over a **vertex** (existing point)
   - Vertex will highlight
   - Status bar shows: "ALT + SHIFT + Click to delete point"
3. Hold `Alt+Shift` and click
   - OR just press `Backspace` or `Meta+H`
4. Point is removed

---

## 🔍 Troubleshooting

### "Alt+Click doesn't work"
**Checklist**:
- ✅ Are you in Edit mode? (`Ctrl+J`)
- ✅ Are you hovering over an **edge** (line), not a vertex (point)?
- ✅ Does the edge highlight when you hover?
- ✅ Does status bar say "ALT + Click to create point"?
- ✅ Are you clicking a polygon/linestrip shape? (Works on those, not rectangles/circles)

### "Ctrl+M doesn't work"
**Checklist**:
- ✅ Are you in Edit mode?
- ✅ Are you hovering over an edge (should be highlighted)?
- ✅ Is the shortcut configured? Check `~/.labelmerc` for `add_multiple_points: Ctrl+M`

### "I don't see the 'Add Multiple Points' menu item"
- The menu item is only **enabled** when you're hovering over an edge
- Try: Right-click on canvas → you should see it in the menu (but grayed out unless edge is selected)

---

## ⚙️ Configuration

Edit `~/.labelmerc` or `labelme/config/default_config.yaml`:

```yaml
# Default number of points when dialog opens
default_num_points_to_add: 1  # Change to 3, 5, etc.

# Keyboard shortcuts
shortcuts:
  add_multiple_points: Ctrl+M  # Change to your preference
  remove_selected_point: [Meta+H, Backspace]
```

---

## 🪟 Windows Installation

Yes, you can install on Windows the same way:

```cmd
cd path\to\labelme
pip install -e .
```

Or if you're using a virtual environment:
```cmd
python -m venv venv
venv\Scripts\activate
pip install -e .
labelme
```

---

## 📝 Summary Table

| Action | Shortcut/Method | Works On | Result |
|--------|----------------|----------|---------|
| Add 1 point | `Alt+Click` on edge | Edge | Point at cursor |
| Add N points | Hover edge, press `Ctrl+M` | Edge | N evenly-spaced points |
| Remove point | `Alt+Shift+Click` or `Backspace` | Vertex | Delete point |

---

## 💡 Tips

1. **Hover carefully**: Make sure you're on the edge (line) not near a vertex (point)
2. **Edge highlighting**: The edge should highlight when you hover correctly
3. **Status bar**: Always check the status bar at the bottom - it tells you what actions are available
4. **Menu items**: Both "Remove Selected Point" and "Add Multiple Points" appear in Edit menu, but are only enabled when hovering over the correct element

---

**Still not working?** 
- Try restarting labelme
- Check console for error messages
- Make sure you have the latest code (the changes we just made)
