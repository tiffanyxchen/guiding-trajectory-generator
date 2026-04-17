# Guiding Trajectory Generator

A modular Python framework for generating guiding trajectories for multi-link pendulum systems.

## Features
- Config-driven trajectory generation (YAML)
- Triangle-wave motion profiles
- Forward kinematics (angles → positions)
- Experiment-based pipeline
- CSV export of trajectories

## Project Structure
configs/        # system + motion configs
experiments/    # experiment scripts
src/            # core modules

## Example
python -m experiments.generate_reach_floor