# Event Log User Report Generator

## Overview

This Python script serves the purpose of processing a list of Event objects, extracting information about currently logged-in users, and generating a detailed report. The script aims to provide insights into user sessions on the machines based on the attributes of the Event objects.

## Project Objective

The primary goal of this project is to implement a Python script capable of:

1. Processing a list of Event objects, each containing attributes representing various events.
2. Extracting relevant information related to user logins from the Event objects.
3. Generating a comprehensive report that lists all users currently logged in to the machines.

## Problem Statement

The script will tackle the challenge of interpreting diverse Event objects, focusing on those pertinent to user login events. By analyzing the attributes of these objects, the script will distill meaningful information to compile an informative report about the current user sessions on the systems.

## Input

The input to the script consists of a list of Event objects. Each Event object encapsulates details about various events, with the script specifically targeting attributes associated with user logins.

## Output

Upon execution, the script will produce a report in a specified format. The report will include essential details, such as:

- Usernames of currently logged-in users.
- Timestamps or additional pertinent information about the login events.

## Usage

To utilize the script, follow these steps:

1. Provide the list of Event objects as input to the script.
2. Execute the script using the appropriate Python interpreter.

<!--Example usage:

```bash
python event_log_user_report.py <input_file_path>
-->
