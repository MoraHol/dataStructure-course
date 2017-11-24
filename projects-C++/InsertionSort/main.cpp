#include <iostream>
#include <stdio.h>
#include <string.h>
#include <vector>
#include <cstdlib>
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
using namespace std;
//prototipo
int* InsertionSort(int[],int);
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
	
	int* array1 = InsertionSort(array, n);
	cout<<"\n"<<"Arreglo ordenado: \n";
	for(int i = 0; i < matInput.size();i++){
		if (i < n - 1){
			cout <<array1[i] << ",";
		}
		else
		{
			cout<< array1[i];
		}
	}
	cout<<endl;
	system("pause");
}
int* InsertionSort(int array[],int n){
	int x; //valueToinsert
	int index; //holePosition
	for (int i = 0; i < n;i++){
		/*select value to moved*/
		x = array[i];
		index = i;
		while (index > 0 && array[index -1] > x){
			array[index] = array[index -1];
			index = index - 1;
		}
		/* insert the value at hole position*/
		array[index] = x;
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
