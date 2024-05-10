# Cell Count Analysis

## Project Overview
This project involves analyzing immune cell count data from various samples to determine relative frequencies of different cell populations and to explore differences between responders and non-responders to a specific treatment (tr1) in melanoma patients. The analysis is performed using Python with libraries like Pandas, Matplotlib, and Seaborn.

## Getting Started

### Prerequisites
- Docker
- Docker Compose
- Git (optional, for cloning the repository)

### Installation
1. **Clone the repository (optional):**
   ```bash
   git clone https://github.com/parthasarathydNU/cell-count-analysis.git
   cd cell-count-analysis
   ```

2. **Build and run the application using Docker Compose:**
   ```bash
   docker-compose up --build
   ```

### File Structure
- `scripts/`: Contains Python scripts for data analysis.
  - `analyze.py`: Script to calculate relative frequencies of cell counts.
  - `statistics_analysis.py`: Script to analyze differences in cell populations.
- `results/`: Contains outputs from the scripts, including CSV files and plots.
- `Dockerfile`: Defines the Docker container setup.
- `docker-compose.yml`: Configures services, networks, and volumes for Docker.
- `requirements.txt`: Lists Python package dependencies.

## Usage
With Docker Compose, your application will be built and started by running the command mentioned in the Installation section. This will execute the scripts as configured in `docker-compose.yml`. You can edit this file to change which scripts are run or to adjust other settings such as port mapping and volume mounting.

## Contributing
Feel free to fork the repository and submit pull requests. You can also open an issue if you find any bugs or have suggestions for further improvements.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

## Authors
- Dhruv Parthasarathy

## Acknowledgments
- Thanks to everyone who has contributed to the open-source packages used in this project.
