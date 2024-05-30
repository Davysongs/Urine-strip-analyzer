# Urine Test Strip Analyzer

This project is a web application that allows users to upload an image of their urine test strip, processes the image to identify the colors on the strip, and returns the results in JSON format.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Usage](#usage)
- [About Urine Test Strips](#about-urine-test-strips)
- [License](#license)

## Overview

Urine test strips are a convenient and quick way to test for various substances in urine. This web application aims to automate the analysis of these strips by identifying the colors on the strip and returning the results as RGB values.

## Features

- Upload an image of a urine test strip.
- Analyze the image to identify and extract colors.
- Return the results as a JSON object containing the RGB values of each color on the strip.
- Responsive web interface.

## Technologies Used

- **Backend**: Django, Django REST framework
- **Frontend**: Bootstrap, Vanilla JavaScript
- **Image Processing**: OpenCV
- **Other**: Git for version control

## Setup

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Virtual environment (optional but recommended)

### Installation

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd urine_test_strip
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `.\venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Django server**:
    ```bash
    python manage.py runserver
    ```

5. **Access the application**:
    Open your web browser and go to `http://127.0.0.1:8000`.

## Usage

1. **Open the web application**:
    Navigate to `http://127.0.0.1:8000` in your web browser.

2. **Upload an image**:
    Click on the "Select Image" button and choose an image of a urine test strip.

3. **Analyze the image**:
    Click on the "Upload" button to upload the image. The application will process the image and display the RGB values of each color on the strip.

## About Urine Test Strips

Urine test strips are a common diagnostic tool used to detect various substances in urine. Each strip contains multiple pads or reagents that change color when exposed to urine, indicating the presence of specific substances. For more information, you can refer to the [Wikipedia article on urine test strips](https://en.wikipedia.org/wiki/Urine_test_strip).
