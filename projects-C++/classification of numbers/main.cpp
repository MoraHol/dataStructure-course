#include <iostream>
#include <string.h>
#include <stdio.h>
#include <cstdlib>
using namespace std;
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	int m;
	cout<< "ingrese el valor de m: \n";
	cin >> m;
	//creacion de matriz
	int matriz[m][m];
	//llenado de matriz aleatoriamente
	for(int i = 0; i < m;i++){
		for (int j = 0;j < m;j++){
			matriz[i][j] = rand() % 50 - 25;
		}
	}
	//impresion de la matriz en pantalla
	for(int i = 0; i < m;i++){
		for (int j = 0;j < m;j++){
			cout<<matriz[i][j]<<" ";
		}
		cout<<endl;
	}
	cout<<endl;
	
	//guardar numero de pares
	int k = 0;
	for(int i = 0; i < m;i++){
		for (int j = 0;j < m;j++){
			if(matriz[i][j] % 2 == 0){
				k++;
			}
		}
	}
	//impresion de nuemero de pares
	cout << "la matriz tiene " << k << " numeros pares: \n";
	int pares[k];
	k=0;
	printf("[");
	for(int i = 0; i < m;i++){
		for (int j = 0;j < m;j++){
			if(matriz[i][j] % 2 == 0){
				printf("%i, ",matriz[i][j]) ;
			}	
		}
	}
	printf("]");
	
	cout<<endl;
	
	//guardar numero de impares
	k = 0;
	for(int i = 0; i < m;i++){
		for (int j = 0;j < m;j++){
			if(matriz[i][j] % 2 != 0){
				k++;
			}
		}
	}
	//impresion de nuemero de impares
	cout << "la matriz tiene " << k << " numeros impares: \n";
	k=0;
	printf("[");
	for(int i = 0; i < m;i++){
		for (int j = 0;j < m;j++){
			if(matriz[i][j] % 2 != 0){
				printf("%i, ",matriz[i][j]) ;
			}	
		}
	}
	printf("]");
	
	
		cout<<endl;
	
	//guardar numero de negativos
	k = 0;
	for(int i = 0; i < m;i++){
		for (int j = 0;j < m;j++){
			if(matriz[i][j] < 0){
				k++;
			}
		}
	}
	//impresion de nuemero de negativos
	cout << "la matriz tiene " << k << " numeros negativos: \n";
	k=0;
	printf("[");
	for(int i = 0; i < m;i++){
		for (int j = 0;j < m;j++){
			if(matriz[i][j]  < 0){
				printf("%i, ",matriz[i][j]) ;
			}	
		}
	}
	printf("]");
	
		cout<<endl;
	
	//guardar numero de positivos
	k = 0;
	for(int i = 0; i < m;i++){
		for (int j = 0;j < m;j++){
			if(matriz[i][j] > 0){
				k++;
			}
		}
	}
	//impresion de nuemero de positivos
	cout << "la matriz tiene " << k << " numeros positivos: \n";
	k=0;
	printf("[");
	for(int i = 0; i < m;i++){
		for (int j = 0;j < m;j++){
			if(matriz[i][j] > 0){
				printf("%i, ",matriz[i][j]) ;
			}	
		}
	}
	printf("]");
	
	
	system("pause");
}
