/*
* File: complex.c
* Author: Ruby Abrams
* Purpose: working with complex numbers, generates the Mandelbrot set
*/

#include <stdio.h>
#include <stdlib.h>
#include <complex.h>
#include <math.h>

#define grid_size 500

// defining a point/tuple
typedef struct{
	double x, y;
} Point;

// Iterative map that will 
double complex map(double complex z, double complex c){
	return z * z + c;
} 

// size of the complex number
double size_of(double complex z){
	return sqrt(creal(z)*creal(z)+cimag(z)*cimag(z));
}

// Converting a point into a complex number
double complex to_complex(Point p){
	return p.x + p.y * I;
}

int in_M(double complex z){
	double complex c = z;
	int count = 0;
	while(size_of(z) <= 2){
		if(count > 200){
			return 1;
		}
		z = map(z, c);
		++count;
	}
	return 0;
}

int main(){

	// making an axis
	double axis[grid_size];
	for (int i = 0; i < grid_size; ++i)
	{
		axis[i] = 4*((double) i)/grid_size - 2;
	}

	// making the grid
	Point grid[grid_size][grid_size];
	for (int i = 0; i < grid_size; ++i)
	{
		for (int j = 0; j < grid_size; ++j)
		{
			grid[i][j].x = axis[i];
			grid[i][j].y = axis[j];
		}
	}

	for (int i = 0; i < grid_size; ++i)
	{
		for (int j = 0; j < grid_size; ++j)
		{
			double complex c = to_complex(grid[i][j]);
			if (in_M(c))
			{
				printf("(%.3f,%.3f) ",creal(c), cimag(c));
			}
		}
		printf("\n");
	}
	printf("\n");
	
	return 0;
}
