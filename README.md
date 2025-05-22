# Code Repository for the Paper

**Are LLMs Reliable Translators of Logical Reasoning Across Lexically Diversified Contexts?**

This is the official code repository for the paper *"Are LLMs Reliable Translators of Logical Reasoning Across Lexically Diversified Contexts?"*

## Repository Structure

* **`data/`**: Contains the original datasets used in the paper.
* **`experiment/`**: Contains the core code and prompts used in the experiments.

### Prompting Strategies

* **`./experiment/direct-prompts/`**:
  Contains prompts for the *direct prompting* strategy used to translate formal logic formulas.

  * Associated script: `trans.py` (run with default parameters).

* **`./experiment/diversification-prompts/`**:
  Contains prompts used for *Logic-invariant Lexical Diversification* based on the **SCALe** method.

  * Associated script: `diversification.py`.

* **`./experiment/synonym-prompts/`**:
  Contains prompts used in the **MenTaL** strategy, which applies *in-context learning* with synonym substitution.

  * Associated script: `trans.py` (run with `--synonym True`).

* **`./experiment/symbolic_solvers/`**:
  Contains all symbolic solvers used during evaluation and inference.

## Other Scripts

* **`logic_inference.py`**:
  Executes the translated formal logic programs using LLM outputs to derive answers.

* **`err_detect.py`**:
  Identifies incorrect programs generated during inference and calculates accuracy.

* **`utils.py`**:
  Contains helper functions and LLM API parameter settings.

## Running SCALe-based Experiments

To run experiments on the SCALe benchmark:

1. Use `diversification.py` to generate diversified datasets for each task.
2. Then run `trans.py` with the `--disrupt True` flag to evaluate using the SCALe benchmark.

## Running MenTaL-Based Experiments

To run experiments using MenTaL:

1. Run `trans.py` with the `--synonym True` flag.