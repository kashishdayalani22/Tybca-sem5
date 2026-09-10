import java.util.Scanner;

public class  bubblesort{
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);

        System.out.print("Enter number of elements: ");
        int n = scan.nextInt();

        int arr[] = new int[n];

        for(int a = 0; a < n; a++){
            System.out.println("Enter an element (int) : ");
            int ele = scan.nextInt();
            arr[a] = ele;

        }
        InsertionSort(arr);

        for (int x : arr){
            System.out.print( x + " ");
        }
    }

    public static void BubbleSort(int[] arr){
        int n = arr.length;
        for(int i = 0; i < n - 1; i++){
            for(int j = 0; j < n - i - 1; j++){
                if ( arr[j + 1] < arr[j ]){
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }
}
