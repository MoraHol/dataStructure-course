import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Random;

public class InteriorRombo {

	public static void main(String[] args) throws NumberFormatException, IOException {
		Random rd = new Random();
		BufferedReader br = new BufferedReader (new InputStreamReader (System.in));
		
		// ingreso de m
		System.out.println("ingrese el valor de m");
		int m= Integer.parseInt(br.readLine());
		// inicializacion de matrizes
		int[][] matriz = new int[m][m];
		int [][] matriz2 = new int[m][m];
		//llenado de matriz aleatoriamente
		for(int i = 0; i < matriz.length ;i++) {
			for(int j = 0; j < matriz.length;j++) {
				matriz[i][j] = rd.nextInt(9)+1;
			}
		}
		// muestra la matriz en pantalla
		for(int i = 0; i < matriz.length ;i++) {
			for(int j = 0; j < matriz.length;j++) {
				System.out.print(matriz[i][j] + " ");
			}
			System.out.println();
		}
		int k;
		
		// muestra el rombor si m es par o impar
		if(m % 2 == 0)
		{
			matriz2 = RomboPar(matriz, m);
			k = matriz.length /2;
		}
		else
		{
			matriz2 = RomboImpar(matriz, m); 
			k = matriz.length /2 + 1;
		}
		int i,j;
		
		
		System.out.println();
		// imprime el rombo interior de la matriz
		MostrarMAtriz(matriz2);
	}
	public static int [][] RomboPar(int [][] matriz, int m){
		int k = matriz.length /2 ;
		int u = k-1,i,j;
		
		int[][] matriz2 = new int [m][m];
		// superior izquierda
		for(i = 0;i < k;i++) {
			for(j = u;j < k;j++) {
				matriz2[i][j] = matriz[i][j]; 
			}
			u--;
		}	
		// inferior izquierda
		u=0;
		for(i = k; i < matriz.length;i++) {
			for(j = u; j < k;j++) {
				matriz2[i][j] = matriz[i][j];  
			}
			u++;
		}
		// superior derecha
		u = k;
		for(i = 0; i < k;i++) {
			for(j = k; j <= u;j++) {
				matriz2[i][j] = matriz[i][j];  
			}
			u++;
		}
		// inferior derecha
		u = matriz.length;
		for(i = k; i < matriz.length;i++) {
			for(j = k; j < u;j++) {
				matriz2[i][j] = matriz[i][j];  
			}
			u--;
		}
		return matriz2;
	}
	public static int [][] RomboImpar(int [][] matriz, int m){
		int k = matriz.length /2 ;
		int u = k-1,i,j;
		
		int[][] matriz2 = new int [m][m];
		// superior izquierda
		for(i = 0;i < k;i++) {
			for(j = u+1;j < k;j++) {
				matriz2[i][j] = matriz[i][j]; 
			}
			u--;
		}	
		// inferior izquierda
		u=0;
		for(i = k; i < matriz.length;i++) {
			for(j = u; j < k;j++) {
				matriz2[i][j] = matriz[i][j];  
			}
			u++;
		}
		// superior derecha
		u = k;
		for(i = 0; i < k;i++) {
			for(j = k; j <= u;j++) {
				matriz2[i][j] = matriz[i][j];  
			}
			u++;
		}
		// inferior derecha
		u = matriz.length;
		for(i = k; i < matriz.length;i++) {
			for(j = k; j < u;j++) {
				matriz2[i][j] = matriz[i][j];  
			}
			u--;
		}
		return matriz2;
	}
	// metodo para mostrar solo la parte del rombo interior de la matriz
	
	public static void MostrarMAtriz(int [][] matriz){
		for(int i = 0; i < matriz.length ;i++) {
			for( int j = 0; j < matriz.length;j++) {
				if(matriz[i][j] == 0) // cuadno los numeros son ceros no se muestran en pantalla
				{
					System.out.print("  ");
				}else 
				{
					System.out.print(matriz[i][j] + " ");
				}
			}
			System.out.println();
		}
	}
	
}
