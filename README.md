
# GoodJobHunting 👩‍🏭
A utility to help employees find a salaried job directly at a company (no LinkedIn/Indeed/ZipRecruiter etc.).  Also, it is for making the statistics of everyone's job search available to the public.  It's a sad time we live in where finding a job is more difficult than the jobs themselves, and the rampant proliferation of so-called "Ghost Jobs".

## Developer Setup

1. From a command prompt within the project's root directory, run `pip install -r requirements.txt`.  This will take care of installing most of the python library dependencies.
2. If you plan on editing the GUI: [Download [Standalone] Qt Designer for Windows, Mac and Linux](https://www.pythonguis.com/installation/install-qt-designer-standalone/). This project uses PyQt5 for lack of resources support in PyQt6, so it's best if you install the PyQt5 tools most likely.  This tool is merely used to edit the resource icons but more importantly to visually layout the GUI's (.ui form files)
3. __(Optional, but highly recommended)__ Download and install [Wing Pro Python IDE](https://wingware.com/downloads/wing-pro).
4. If you installed Wing Pro, open up the `GoodJobHunting.wpr` file located in the project's root using Wing Pro.   Otherwise, you're on your own with any other IDE. Wing Pro is really great for debugging Python code.  If your Wing Pro trial runs out and you can't afford to purchase a license, then perhaps you can hack it with Wing 101 or some other IDE.
        
### How to compile the .ui files
1. Make your changes in the Standalone Qt Designer of some .ui file.
2. Open up a command prompt in the `GoodJobHunting/ui` directory.
3. Run `pyuic5 --from-imports -o ui_main_window.py main_window.ui` for example.
4. Re-run your main application to see changes.

### How to compile the .qrc (resource) file
1. Make your (typically icon) edits in the Standalone Qt Designer file from within the Resource Editor.
2. Open up a command prompt in the `GoodJobHunting/ui` directory.
3. Run `pyrcc5 -o resources_rc.py resources.qrc`.
4. Compile any relevant .ui files:  `pyuic5 --from-imports -o ui_main_window.py main_window.ui`
5. Re-run your main application to see changes.