#include <iostream>
#include <stdio.h>
#include <string.h>
#include <vector>
#include <cstdlib>
using namespace std;
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
//prototipo
vector<string> split(string , string );

 
int main(int argc, char** argv) {
	int m, AreaMatriz;
	
	vector<string> matInput;
	string input;
	cout << "ingrese el valor de m : \n";
	cin >> m;
	int matriz[m][m];
	AreaMatriz = m * m;
	cout << "ingrese los " <<AreaMatriz<<" numeros de la matriz separados por coma \n";
	cin >> input;
	
	//llenado de arreglo en String de los numeros de la matriz
	matInput = split(input,",");
	
	//conversion del arreglo String a entero
	int k=0;
	for(int i = 0; i < m;i++){
		for(int j = 0; j < m;j++){
			matriz[i][j] =  atoi((matInput[k]).c_str());
			k ++;
		}
		cout<<endl;
	}
	
	//impresion de matriz en pantalla
	for(int i = 0; i < m;i++){
		for(int j = 0; j < m;j++){
			cout<<matriz[i][j]<<" "; 
		}
		cout<<endl;
	}
	cout<<endl;
	puts("matriz transpuesta: \n");
	//impresion de matriz en pantalla transpuesta
	for(int i = 0; i < m;i++){
		for(int j = 0; j < m;j++){
			cout<<matriz[j][i]<<" "; 
		}
		cout<<endl;
	}
	system("pause");
	
	
	
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




