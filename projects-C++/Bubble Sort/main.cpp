#include <iostream>
#include <stdio.h>
#include <string.h>
#include <vector>
#include <cstdlib>
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
using namespace std;
//prototipo
int* BubbleSort(int[],int);
vector<string> split(string , string );


int main() {
	vector<string> matInput;
	string input;
	
	
	cout << "ingrese los numeros separados por coma: \n";
	cin >> input;
	
	//llenado de arreglo en String de los numeros de la matriz
	matInput = split(input,",");
	int n = matInput.size();
	int array[n];
	//conversion del arreglo String a entero
	int k=0;
	for(int i = 0; i < matInput.size();i++){
		array[i] =  atoi((matInput[k]).c_str());
		k ++;
	}
	
	int* array1 = BubbleSort(array, n);
	cout<<"\n"<<"Arreglo ordenado: \n";
	for(int i = 0; i < matInput.size();i++){
		if (i < n -1)
			cout <<array[i] << ",";
		else{
			cout<< array[i];
		}
	}
	cout<<endl;
	system("pause");
}
int* BubbleSort (int array[],int TAM){
	for (int i=0; i < TAM; i++){
		bool swapped = false;
    	for (int j=0 ; j < TAM - 1; j++){
    		/* compare to adjacent elements */
    		 if (array[j] > array[j+1]){
    		 	/* swap them */
    		 	int swap = array[j];
                array[j] = array[j+1];
                array[j+1] = swap;
                swapped = true;
			 }     
		}
        /* if no number was swapped, the array is sorted now */
		if (not swapped){
			break;
		} 
		
	}
	return array;
		
}
//funcion que cumple como split
vector<string> split(string str, string sep){
    char* cstr=const_cast<char*>(str.c_str());
    char* current;
    vector<std::string> arr;
    current=strtok(cstr,sep.c_str());
    while(current != NULL){
        arr.push_back(current);
        current=strtok(NULL, sep.c_str());
    }
    return arr;
}
