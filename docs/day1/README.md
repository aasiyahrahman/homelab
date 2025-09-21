# Day 1 — Ubuntu Desktop (UTM on M2)

**Goal:** Install a working Ubuntu 24.04.3 Desktop VM inside UTM on my MacBook Air M2 and capture proof-of-install artifacts.

## Summary
I created an Ubuntu (ARM64) virtual machine in UTM, completed the installer, logged in, and performed initial system updates and package installs required for later days.

## What I did (steps)
1. Created VM in UTM:
   - Virtualize → Linux → Boot from ISO (`~/Downloads/ubuntu-24.04.3-desktop-arm64.iso`)
   - Memory: 4096 MiB, Disk: 30 GB, Enable display.
2. Installed Ubuntu (Normal installation; install third-party drivers).
3. First boot → logged in as `student` (or my chosen username).
4. Opened Terminal and updated system, installed tools:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y git htop curl python3-pip wireshark nmap
cat > docs/day1/README.md <<'EOF'
# Day 1 — Ubuntu Desktop (UTM on M2)

**Goal:** Install a working Ubuntu 24.04.3 Desktop VM inside UTM on my MacBook Air M2 and capture proof-of-install artifacts.

## Summary
I created an Ubuntu (ARM64) virtual machine in UTM, completed the installer, logged in, and performed initial system updates and package installs required for later days.

## What I did (steps)
1. Created VM in UTM:
   - Virtualize → Linux → Boot from ISO (`~/Downloads/ubuntu-24.04.3-desktop-arm64.iso`)
   - Memory: 4096 MiB, Disk: 30 GB, Enable display.
2. Installed Ubuntu (Normal installation; install third-party drivers).
3. First boot → logged in as `student` (or my chosen username).
4. Opened Terminal and updated system, installed tools:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y git htop curl python3-pip wireshark nmap  
cat > docs/day1/README.md <<'EOF'
# Day 1 — Ubuntu Desktop (UTM on M2)

**Goal:** Install a working Ubuntu 24.04.3 Desktop VM inside UTM on my MacBook Air M2 and capture proof-of-install artifacts.

## Summary
I created an Ubuntu (ARM64) virtual machine in UTM, completed the installer, logged in, and performed initial system updates and package installs required for later days.

## What I did (steps)
1. Created VM in UTM:
   - Virtualize → Linux → Boot from ISO (`~/Downloads/ubuntu-24.04.3-desktop-arm64.iso`)
   - Memory: 4096 MiB, Disk: 30 GB, Enable display.
2. Installed Ubuntu (Normal installation; install third-party drivers).
3. First boot → logged in as `student` (or my chosen username).
4. Opened Terminal and updated system, installed tools:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y git htop curl python3-pip wireshark nmap
```
