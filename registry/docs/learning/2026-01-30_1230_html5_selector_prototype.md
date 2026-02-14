# User Query
Create a simple HTML5 selector example and save it as a prototype.

# Technical Deep Dive
The prototype demonstrates modern JavaScript DOM selection techniques using the Selector API.

## Core Selectors
- `document.querySelector()`: Returns the first element matching a CSS selector. Highly versatile for IDs, classes, and complex attributes.
- `document.querySelectorAll()`: Returns a static `NodeList` of all matching elements. Unlike older methods (e.g., `getElementsByClassName`), `NodeList` can be directly iterated with `.forEach()` in modern browsers.

## Implementation Details
- **Path**: `projects/p_prototypes/selector_demo/`
- **Logic**:
    - Selects the main title by ID to change color.
    - Selects the first list item by class to add a highlight.
    - Uses a button to toggle a selection state across multiple items using `querySelectorAll`.
- **CSS**: Uses standard class-based styling to separate concerns from the JavaScript logic.

# Tool Usage
- `run_shell_command`: Used to create the project directory.
- `write_file`: Used to create `index.html` and `README.md`.
