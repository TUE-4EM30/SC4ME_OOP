---
layout: default
---

## Question 1: Engineering model analysis

You first perform the engineering model analysis for the battery and controller.

**Tasks:**
- Study the documentation of the battery model and the controller model — Understand the mathematical equations and physical/logical relationships
- Identify constraints — From the equations and physical laws, extract bounds, relationships, logical rules, and invariants

**Deliverables:**
- Complete the **constraints tables** in each model documentation section. For each constraint, document:
  - The constraint statement (mathematical or logical)
  - Physical or logical justification
  - Relevant parameters and bounds

---
layout: default
---

## Question 2: Battery module implementation

Construct a fully functioning and tested battery module using your engineering analysis as the foundation.

**Tasks:**
- Design and implement `battery.py`:
  - Define classes with appropriate attributes and methods
  - Implement functions specific to the battery module
  - Ensure each component respects the constraints from your analysis

- Develop comprehensive unit tests following the three-step test development approach

**Deliverables:**
- **(Step 1)** — Completion of a **test overview table** in the testing documentation of the battery
- **(Step 2)** — Fully documented unit tests in `tests/test_battery.py` following the AAA paradigm
- **(Step 3)** — Completion of a **coverage overview table** in the testing documentation

---
layout: default
---

## Question 3: Controller module implementation

Construct a fully functioning and tested controller module using your engineering analysis as the foundation.

**Tasks:**
- Design and implement `controller.py`:
  - Define classes with appropriate attributes and methods
  - Implement functions specific to the controller module
  - Ensure each component respects the constraints from your analysis

- Develop comprehensive unit tests following the three-step test development approach

**Deliverables:**
- **(Step 1)** — Completion of a **test overview table** in the testing documentation of the controller
- **(Step 2)** — Fully documented unit tests in `tests/test_controller.py` following the AAA paradigm
- **(Step 3)** — Completion of a **coverage overview table** in the testing documentation

---
layout: default
---

## Question 4: Thermal functionality extension

The provided code implements only the energy storage part of the battery model. Your task is to extend the system with the thermal dynamics of the battery.

**Tasks:**
- Study the thermal model documentation — Understand the mathematical equations and physical relationships governing heat generation, dissipation, and temperature dynamics
- Identify thermal constraints — Extract bounds, relationships, and invariants from the thermal model

- Design the implementation:
  - Choose whether to implement thermal functionality as a separate module or integrate it into existing modules
  - Define classes, attributes, and methods needed for thermal dynamics
  - Ensure all thermal constraints are respected

- Develop comprehensive unit tests following the three-step test development approach

---
layout: default
---

## Question 4: Thermal functionality extension (cont'd)

The provided code implements only the energy storage part of the battery model. Your task is to extend the system with the thermal dynamics of the battery.

**Deliverables:**
- **Updated Question 1:** Add thermal constraints to the battery model constraints table
- **Updated Question 2:** Extend `battery.py` (or create new thermal module) with thermal functionality
  - Updated test overview table
  - New/updated tests in `tests/test_battery.py` (or `tests/test_thermal.py`) following AAA paradigm
  - Updated coverage overview table
- **Updated Question 3:** If the controller logic depends on or uses thermal data, update `controller.py` and its tests accordingly

---

## Submission instructions

- The following deliverables are due on **Friday March 13, 2026, 18:00**:
    - All **source code** and **documentation files** must be developed in your team’s Gitlab repository. After the due date a snapshot of your repository will be taken. The latest push to the Gitlab repository main branch before the deadline will be assessed.
    - You can test the generation of the documentation and coverage reports locally (as instructed in the repository). Upon pushing your code to the Gitlab repository you can manually run the CI/CD pipeline to run the tests and generate documentation on the server.
    - A pdf copy of your online documentation should be uploaded to Canvas (for reference). See the `Quickstart` in the package documentation for detailed instructions.