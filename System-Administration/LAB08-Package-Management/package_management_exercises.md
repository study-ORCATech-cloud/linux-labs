# LAB08 - Package Management Exercises

These exercises will help you practice installing, updating, and managing software packages on a Linux system. Complete each task to build essential package management skills for system administration.

## Exercise 1: Package Manager Basics

### TODO:
1. Determine your Linux distribution and package manager.

2. Update the package repository information for your system.

3. List all available upgrades for your installed packages.

4. Count how many packages are currently installed on your system.

5. Display information about your package manager.

6. Review your package management logs to see recent installations and removals.

## Exercise 2: Installing and Removing Packages

### TODO:
1. Install the "htop" system monitoring tool.

2. Run htop to verify it installed correctly (press q to exit).

3. Check which package provides the htop command.

4. Find the location of htop's configuration files.

5. Remove htop but keep its configuration files.

6. Completely remove htop including configuration files.

## Exercise 3: Package Searching and Information

### TODO:
1. Search for packages related to Python.

2. Get detailed information about a specific package (e.g., "python3").

3. List all files installed by a package (install if needed).

4. Find which package provides a specific file.

5. List packages by size (largest first).

6. Find packages containing a specific string in their description.

## Exercise 4: Dependency Management

### TODO:
1. Identify dependencies for a specific package.

2. Check which packages depend on a specific package.

3. Clean up orphaned packages (not required by other packages).

4. Identify if any broken dependencies exist in your system.

5. Install a package without its recommended dependencies.

6. Hold a package at its current version (prevent automatic updates).

## Exercise 5: Package Management Files and Repositories

### TODO:
1. Examine your package manager's repository configuration.

2. Add a new repository (use an appropriate one for your distro).

3. Update your package lists after adding the repository.

4. Check your package cache size and location.

5. Clean your package manager cache.

6. Verify package authenticity (check GPG keys).

## Exercise 6: Package Upgrades and Maintenance

### TODO:
1. Perform a distribution upgrade simulation (without actually upgrading).

2. Install security updates only.

3. Configure automatic updates (investigate the files or packages needed).

4. Create a log of all installed packages.

5. Use your package manager's history feature to see recent operations.

6. Check for obsolete packages.

## Exercise 7: Package Building Basics

### TODO:
1. Install package building tools.

2. Download the source of a simple package.

3. Inspect the package build files.

4. Install a package from a local .deb or .rpm file.

5. Verify a package after installation.

6. Check the integrity of all installed packages.

## Bonus Challenge:
Create a shell script called `package_manager.sh` that:
1. Detects the Linux distribution and available package manager
2. Provides a menu with common package management tasks:
   - Update system
   - Install a package
   - Remove a package
   - Search for a package
   - Clean package cache
   - List recently installed packages
3. Executes the chosen task with the appropriate command for the detected package manager
4. Logs all operations to a file with timestamps 