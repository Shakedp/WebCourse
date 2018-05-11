# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Install any needed packages specified in requirements.txt
RUN pip3 install Flask
