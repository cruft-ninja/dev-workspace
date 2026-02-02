---
title: x11vnc Permissions Deep Dive
date: 2026-01-30
tags: [linux, x11vnc, permissions, security]
---

# User Query
What are the necessary permissions for an x11vnc server?

# Technical Deep Dive

To run `x11vnc` securely and effectively, the following permissions and configurations are typically required:

## 1. X11 Authentication (The `.Xauthority` file)
The server must be able to read the Xauthority file of the active session to prove it has permission to capture the screen.
- **User session:** If running as the logged-in user, it defaults to `~/.Xauthority`.
- **System service:** If running as `root` or a system user, you must explicitly point to the user's authority file using the `-auth` flag.
    - *Example (GDM):* `-auth /run/user/1000/gdm/Xauthority`
    - *Example (Standard):* `-auth /home/user/.Xauthority`

## 2. Input Device Access (`/dev/uinput`)
For remote control (mouse/keyboard injection), `x11vnc` often requires write access to the uinput device.
- **Requirement:** Either run as `root` or ensure the user is in the `input` group.
- **Security Note:** Avoid `chmod 777 /dev/uinput`. Instead, use a udev rule or proper group membership.

## 3. Display Connection
The process needs to know which X display to attach to.
- **Requirement:** Access to the Unix socket in `/tmp/.X11-unix/X0` (for display `:0`).
- **Configuration:** Usually handled by setting the `DISPLAY=:0` environment variable or using the `-display :0` flag.

## 4. VNC Password File
If using authentication (highly recommended), the process needs read access to your VNC password.
- **Requirement:** Read access to `~/.vnc/passwd` (default) or the path specified by `-rfbauth`.

## 5. Recommended Secure Execution
Execution as root for a user session (e.g., in a systemd service):
```bash
sudo x11vnc -auth /home/user/.Xauthority -display :0 -rfbauth /home/user/.vnc/passwd -loop -noxdamage -repeat -rfbport 5900 -shared
```

# Tool Usage
The agent searched the codebase for existing references to `x11vnc` and found none, then performed a technical synthesis based on Linux system administration standards and the Habitat's `AI_SECURITY_POLICY.md`.
