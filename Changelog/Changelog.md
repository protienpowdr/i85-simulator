# i85 Simulator & IDE Changelog
All notable changes to i85 Simulator & IDE are listed here.

---
### 12-11-2026 &mdash; Baibhav Bhattacharya

- Initial Project Structure
- `Ui` : Added `Toolbar` , `Navbar` , `Sidebar` 
- `Ui` : Integrated fonts and images
- `Assembler` : Compiled `asm85` using MinGW for i85 Simulator & IDE

---
### 13-11-2026 &mdash; Baibhav Bhattacharya

- `Ui` : Added Modified CTkCodeBox based code editor
- `Ui` : Added Hardware Panel , Register and Flag Views
- `Ui` : Initial design for Memory and Port View


---
### 15-11-2026 &mdash; Baibhav Bhattacharya

- `Ui` : Added Memory & Register View
- `Simulator` : Designed Initial Structure
- `Simulator` : Class Definitions of CPU, Memory, IO and basic helper functions
- `Simulator` : Initial Structure of Opcodes & Instructions

---
### 16-11-2026 &mdash; Baibhav Bhattacharya

- `Simulator` : Implemented Instruction Table
- `Simulator` : Added support for `NOP` , `LXIB` , `STAXB` , `INXB` , `INRB` and `DCRB` instructions
- `Simulator` : Added flag evaluation functions for `CY`, `Z`, `P`, `S` and `AC` flags.

---
### 17-11-2026 &mdash; Baibhav Bhattacharya

- `Ui` : Added Listing View
- `Ui` : Fixed grid layouts and code organization
- `Simulator` : Added support for `INXB`, `RLC` instructions and flag evaluation functions for
`overflow (V) and x5 (K)` undocumented flags.

---
### 18-11-2026 &mdash; Baibhav Bhattacharya

- `Ui` : Added listner function to hide the application layout during resize to significantly 
improve animation speed while resizing. 
- `Ui` : Added main container for all widgets.

- `Simulator` : Added support for `DADB` Instruction, developed handling process for undefined instructions
like `DSUB` using the existing Event-Component Model
- `Docs`  Added `README`, `LICENSE` , `Changelogs` and `Documentations` 
- `dvcs`  Initial push on remote github repository and git integration.

