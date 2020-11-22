{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Script to calculate Basic Statistics"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Equation for the mean:   $\\mu_x = \\sum_{i=1}^{N}\\frac{x_i}{N}$\n",
    "\n",
    "### Equation for the standard deviation:  $\\sigma_x = \\sqrt{\\sum_{i=1}^{N}\\left(x_i - \\mu \\right)^2}\\frac{1}{N-1}$\n",
    "\n",
    "\n",
    "**Instructions:**\n",
    "\n",
    "**(1) Before you write code, write an algorithm that describes the sequence of steps you will take to compute the mean and standard deviation for your samples.  The algorithm can be written in pseudocode or as an itemized list.***\n",
    "\n",
    "**(2) Use 'for' loops to help yourself compute the average and standard deviation.**\n",
    "\n",
    "**(3) Use for loops and conditional operators to count the number of samples within $1\\sigma$ of the mean.**\n",
    "\n",
    "**Note:** It is not acceptable to use the pre-programmed routines for mean and st. dev., e.g. numpy.mean()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Edit this box to write an algorithm for computing the mean and std. deviation.\n",
    "\n",
    "~~~\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "~~~"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Write your code using instructions in the cells below."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Put your Header information here.  Name, creation date, version, etc.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import the matplotlib module here.  No other modules should be used.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a list variable that contains at least 25 elements.  You can create this list any number of ways.  \n",
    "# This will be your sample.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Pretend you do not know how long x is; compute it's length, N, without using functions or modules.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Compute the mean of the elements in list x.\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Compute the std deviation, using the mean and the elements in list x.\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use the 'print' command to report the values of average (mu) and std. dev. (sigma).\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Count the number of values that are within +/- 1 std. deviation of the mean.  \n",
    "# A normal distribution will have approx. 68% of the values within this range.  \n",
    "# Based on this criteria is the list normally distributed?\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use print() and if statements to report a message about whether the data is normally distributed.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "### Use Matplotlb.pyplot to make a histogram of x.\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "### OCG 593 students, look up an equation for Skewness and write code to compute the skewness. \n",
    "#### Compute the skewness and report whether the sample is normally distributed."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
