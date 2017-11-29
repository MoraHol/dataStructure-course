#include <iostream>
#include <stdio.h>
#include <string.h>
#include <vector>
#include <cstdlib>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
using namespace std;
// prototype
int LinealSearch(int [], int, int);
vector<string> split(string , string );
int main() {
	vector<string> matInput;
	string input;
	int value;
	
	cout << "ingrese los numeros separados por coma: \n";
	cin >> input;
	cout<< "ingrese el numero a buscar: \n";
	cin >> value;
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
	int size = sizeof(array) / sizeof(array[0]);
	int index = LinealSearch(array,value,size);
	cout << "el numero buscado esta en la posicion " << index + 1; 
	return 0;
}
int LinealSearch(int array[],int data, int size){
	int index = -1;
	
	/* compare with all elements of the array*/
	for (int i = 0; i < size;i++){
		if (array[i] == data){
			index = i;
			break;
		}
	}
	return index;
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
