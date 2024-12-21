# Two Point Perspective

## Overview

**Two Point Perspective** is a Blender add-on that replaces the active camera with a copy that utilizes two-point perspective. 
This add-on is particularly useful for architectural visualizations and other scenarios where minimizing distortion is essential.
  ![imgResult](https://github.com/user-attachments/assets/b358d914-0e90-4982-aa19-4f9fabcd27ca)

## Features

- Converts a 3-point perspective camera to a 2-point perspective.
- Allows manual setting of the target angle.

## Installation

There are different ways to install an extension:

### Install from the Website
1. Drag the installation URL into Blender.

### Install from Blender
1. Open Blender and go to `Edit > Preferences > Get Extensions`.
2. Search for "Two Point Perspective" and click on Install.

### Install from Disk
1. Use the drop-down menu in the top right, or drag-and-drop the extension .zip package into Blender.

More detailed instructions can be found in the [Blender Manual](https://docs.blender.org/manual/en/latest/editors/preferences/extensions.html).

## Usage

1. Ensure your scene has at least one camera.
2. In the Properties panel, navigate to the `Scene` tab.
3. Find the `Two Point Perspective` section.
4. Optionally, set a custom target angle by checking the "Custom target angle" box and adjusting the angle value.
5. Click the "Create Two Point Perspective Camera" button.

## Code Overview

- **core.py**: Contains the core functionality for converting the camera perspective.
- **two_point_perspective_ot.py**: Defines the operator for the add-on.
- **two_point_perspective_pt.py**: Implements the panel layout in Blender's interface.
- **__init__.py**: Registers the add-on and its classes with Blender.

## Author

**Athina Syntychaki**

## License

This add-on is licensed under the GNU General Public License v3.0 or later.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests on the [GitHub repository](https://github.com/your-username/your-repo).

## Repository

You can find the source code and contribute to the project on GitHub: [GitHub Repository](https://github.com/synathena/two-point-perspective).
